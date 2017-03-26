from flask import Blueprint

mod = Blueprint('conferences', __name__)

@mod.route('/conferences/')
def get_routes():
	return "Hello World"