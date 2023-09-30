from faker import Faker
from app import app # Import your Flask app and SQLAlchemy db instance
from models import db, Heroes, Heroes_Powers, Powers  # Import your models
import random

# Your hero and power data
hero_names = [
    "Superhero1",
    "Superhero2",
    "Superhero3",
    "Superhero4",
    "Superhero5",
]

powers = [
    "Flight",
    "Super Strength",
    "Telekinesis",
    "Invisibility",
    "Teleportation",
]

with app.app_context():
    fake = Faker()

    # Clear existing data from specific tables
    Heroes.query.delete()
    Heroes_Powers.query.delete()
    Powers.query.delete()

    # Populate heroes
    heroes = []

    for _ in range(50):
        new_hero = Heroes()
        new_hero.name = fake.name()
        new_hero.super_name = fake.first_name()
        heroes.append(new_hero)

    db.session.add_all(heroes)
    db.session.commit()
    print("Heroes successfully populated")

    # Populate powers
    powers_list = []

    for power_name in powers:
        new_power = Powers(name=power_name,description=fake.sentence())
        powers_list.append(new_power)

    db.session.add_all(powers_list)
    db.session.commit()
    print("Powers successfully populated")

    # Populate heroes_powers (many-to-many relationship)
    heroes_powers = []

    for hero in Heroes.query.all():
        random_power_count = random.randint(1, len(powers))
        random_powers = random.sample(powers_list, random_power_count)
      
        strengths = ["Strong", "Average", "Weak"] 

        for power in random_powers:
            new_hero_power = Heroes_Powers(
                heroes_id=hero.id,
                power_id=power.id, 
                strength = random.choice(strengths)
            )
            heroes_powers.append(new_hero_power)

    db.session.add_all(heroes_powers)
    db.session.commit()
    print("Heroes Powers successfully populated")
