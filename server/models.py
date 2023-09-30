from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

####################################################### HEROES ###############################################################
class Heroes(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique = True, nullable=False)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime,server_default=db.func.now()) 
    updated_at = db.Column(db.DateTime,onupdate=db.func.now())
    heroes_power = db.relationship("Heroes_Powers", back_populates="heroes")

################################################## HEROES_POWER################################################################
class Heroes_Powers(db.Model): 
    __tablename__ = 'heroes_powers'
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    heroes_id = db.Column(db.Integer, db.ForeignKey("heroes.id"))
    power_id = db.Column(db.Integer, db.ForeignKey("powers.id"))
    created_at = db.Column(db.DateTime,server_default=db.func.now()) 
    updated_at = db.Column(db.DateTime,onupdate=db.func.now())

    heroes = db.relationship("Heroes", back_populates="heroes_power")
    power = db.relationship("Powers", back_populates="heroes_power")

@validates("strength")
def validates_strength(self,key,strength):
    if strength not in ["Strong", "Weak", "Average"]:
        raise ValidationError("Strength must be Strong,Weak or Average")
    return strength    


############################################################### POWERS #################################################

class Powers(db.Model):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime,server_default=db.func.now())
    updated_at = db.Column(db.DateTime,onupdate=db.func.now())
    heroes_power = db.relationship("Heroes_Powers", back_populates="power")

@validates("description")
def validates_description(self,key,description):

    descriptions = db.session.query(Powers.description).all()
    if description not in descriptions:
        raise ValueError("Description must be Present")
    elif len(description) < 20:
        raise ValueError("Description must be less than 20 characters")
    return description    

