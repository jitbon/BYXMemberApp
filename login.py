from main import app
from flask import request
import mysql.connector
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api

api = Api(app)

@app.route("/api/login", methods=['GET'])
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    # TODO: if database contains username/password combo
    if True:
        return "Logged in", 200
    return "Incorrect username or password", 401

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin",
    database="mydatabase"
)