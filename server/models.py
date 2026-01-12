from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)



class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    id = db.column(db.integer, primary_key=True)
    name = db.column(db.string, nullable=False)
    super_name = db.Column(db.String, nullable=False)

    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade='all, delete-orphan')

    serialize_rules = ('-hero_powers.hero',)