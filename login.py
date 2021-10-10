from main import app
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api, Resource

api = Api(app)

class Login(Resource):
    pass

api.add_resource(Login, '/login')

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin"
)

print(mydb)