import os
import sys

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
app.config.from_object('config')

api = Api(app)

from app.routers.conferences import ConferencesAPIView

api.add_resource(ConferencesAPIView, '/conferences/')
