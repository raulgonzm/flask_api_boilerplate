# Python imports
import os
import sys
# Core Flask imports
from flask import Flask
# Third-Party imports
from flask_restful import Api
# Apps Imports
from app.routers.routers import Router

app = Flask(__name__)
app.config.from_object('config')

Router(Api(app))


