# Python imports

# Core Flask imports

# Third-Party imports

# Apps Imports
from .conferences import init_conferences_routes


class Router(object):

	def __init__(self, api):
		self.__init_conferences_router(api)

	def __init_conferences_router(self, api):
		init_conferences_routes(api)