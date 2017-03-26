# Python imports

# Core Flask imports

# Third-Party imports

# Apps Imports
from app.controllers.conferences import ConferencesListCreateAPIView, ConferencesRetrieveUpdateDeleteAPIView


def init_conferences_routes(api):
	api.add_resource(ConferencesListCreateAPIView, '/conferences/')
	api.add_resource(ConferencesRetrieveUpdateDeleteAPIView, '/conferences/<conference_id>/')
	return api