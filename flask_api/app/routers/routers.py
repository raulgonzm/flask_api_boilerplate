# Python imports

# Core Flask imports

# Third-Party imports

# Apps Imports
from .conferences import ConferencesListCreateAPIView, ConferencesRetrieveUpdateDeleteAPIView


class Router(object):

	def __init__(self, api):
		self.__init_conferences_router(api)

	def __init_conferences_router(self, api):
		api.add_resource(ConferencesListCreateAPIView, '/conferences/')
		api.add_resource(ConferencesRetrieveUpdateDeleteAPIView, '/conferences/<conference_id>/')