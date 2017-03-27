# Python imports

# Core Flask imports
from flask import Flask
# Third-Party imports
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
# Apps Imports
from app.routers.routers import Router

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

Router(Api(app))
