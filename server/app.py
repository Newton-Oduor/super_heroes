from flask import Flask, request
from flask_restful import Api, Resource
from flask_migrate import Migrate

from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)


# GET all heroes
class Heroes(Resource):
    def get(self):
        return [hero.to_dict() for hero in Hero.query.all()], 200

# GET hero by ID
class HeroByID(Resource):
    def get(self, id):
        hero = Hero.query.get(id)
        if not hero:
            return {'error': 'Hero not found'}, 404
        return hero.to_dict(), 200
    

# GET all powers
class Powers(Resource):
    def get(self):
        return [power.to_dict() for power in Power.query.all()], 200
    
# GET power by ID
class PowerByID(Resource):
    def get(self, id):
        power = Power.query.get(id)
        if not power:
            return {'error': 'Power not found'}, 404
    
# POST hero power
class HeroPowers(Resource):
    def post(self):
        data = request.get_json()

        try:
            hero_power = HeroPower(strength=data["strength"], hero_id=data["hero_id"], power_id=data["power_id"])
            db.session.add(hero_power)
            db.session.commit()

            return hero_power.hero.to_dict(), 201
        
        except ValueError as e:
            return {'errors': [str(e)]}, 400
        

api.add_resource(Heroes, "/heroes")
api.add_resource(HeroByID, "/heroes/<int:id>")
api.add_resource(Powers, "/powers")
api.add_resource(PowerByID, "/powers/<int:id>")
api.add_resource(HeroPowers, "/hero_powers")


if __name__ == "__main__":
    app.run(debug=True)