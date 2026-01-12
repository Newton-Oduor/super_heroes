from flask import Flask
from flask_restful import Api
from flask_alchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Hero, Power, HeroPower


