import os
import sys

from flask import Flask
from flask_restful import Api

from app.routers.routers import Router

app = Flask(__name__)
app.config.from_object('config')

Router(Api(app))


