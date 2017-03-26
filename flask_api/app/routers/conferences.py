from flask_restful import Resource

class ConferencesAPIView(Resource):
	
    def get(self):
        return {'hello': 'world'}


