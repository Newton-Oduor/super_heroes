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
            return{'error': 'Hero not found'}, 404
        return hero.to_dict(), 200


if __name__ == "__main__":
    app.run(debug=True)