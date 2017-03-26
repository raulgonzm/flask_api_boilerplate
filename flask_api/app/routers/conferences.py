from flask_restful import Resource

class ConferencesListCreateAPIView(Resource):

    def get(self):
        return {'hello': 'world'}

    def post(self):
    	pass


class ConferencesRetrieveUpdateDeleteAPIView(Resource):

	def get(self, conference_id):
		pass

	def put(self, conference_id):
		pass

	def delete(self, conference_id):
		pass


