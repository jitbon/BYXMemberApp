from main import app
from flask_restful import Api, Resource

api = Api(app)

class Login(Resource):
    pass

api.add_resource(Login, '/login')