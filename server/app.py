#!/usr/bin/env python3
import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, make_response, request,jsonify, render_template
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Heroes, Heroes_Powers, Powers

app = Flask(__name__,
     static_url_path='',
     static_folder='../client/build',
     template_folder='../client/build'

)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

api = Api(app)

db.init_app(app)


@app.errorhandler(404)
def index(id=0):
    return render_template("index.html")


""" @app.route('/')
def home():
    return "<h1>DC COMICS</h1" """

class HeroesResource(Resource):

     def get (self):
          hero =  Heroes.query.all()
          index = []
          for n in hero:
               data = {
                    "id":n.id,
                    "name":n.name,
                    "super_name":n.super_name
               }

               index.append(data)

     
          return make_response(jsonify(index),200)       

api.add_resource(HeroesResource, "/heroes")        

class HeroesIdResource(Resource):
     def get (self,id):
          hero = Heroes.query.filter_by(id = id).first()
          if hero:
               data = {
                    "id":hero.id,
                    "name":hero.name,
                    "super_name":hero.super_name,
                    "powers": [
                         {
                         "id": hero_power.power.id,
                         "name":hero_power.power.name,
                         "description":hero_power.power.description
                         }
                         for hero_power in hero.heroes_power
                    ],

               }

               return make_response(jsonify(data),200)

          else:
               return make_response(jsonify({ "error": "Hero not found"}),404)     

api.add_resource(HeroesIdResource, "/heroes/<int:id>")               


class PowersResource(Resource):
     def get (self):
          power = Powers.query.all()
          index = []     
          for n in power:
               data = {
                    "id":n.id,
                    "name":n.name,
                    "description":n.description
               }
               index.append(data)
          return make_response(jsonify(index),200)     
api.add_resource(PowersResource, "/powers")          



class PowersIdResource(Resource):
     def get(self,id):
          power = Powers.query.filter(id==id).first()
          if power:
               data = {
                    "id": power.id,
                    "name": power.name,
                    "description": power.description
               } 

               return make_response(jsonify(data),200)

          else:
               return make_response ({ "error": "Power not found"},404) 


     def patch (self,id ):
          data = request.get_json()
          power = Powers.query.get(id)

          if power:

            for attr in data:
               setattr(power,attr,data[attr])  

               db.session.add(power) 
               db.session.commit()  

               response = {
                    "id": power.id,
                    "name": power.name,
                    "description": power.description
               }

            return make_response(jsonify(response), 201) 

          
          else: 
               return make_response ({ "error": "Power not found"},404)



api.add_resource(PowersIdResource, "/powers/<int:id>")


class HeroPowerResource(Resource):

     def post(self):
          data = request.get_json()
          power = Powers.query.filter_by(id = data["power_id"]).first()
          hero = Heroes.query.filter_by(id = data["hero_id"]).first()

          if power and hero:
               new_hero_power = Heroes_Powers(strength=data['strength'], power_id = data["power_id"], heroes_id =data["hero_id"])
               db.session.add(new_hero_power)
               db.session.commit()

               response = HeroesIdResource().get(hero.id)

               return make_response(response, 201) 

          else:
               return make_response ({ "error": "Power or hero not found"},404)
          
   
api.add_resource(HeroPowerResource, "/heropower")




if __name__ == "__main__":
    app.run(port=5555, debug=True)
