import os
import sys

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app.routers.conferences import mod as ConferencesModule
app.register_blueprint(ConferencesModule)
