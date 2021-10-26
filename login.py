import re
from main import app
from flask import request
import mysql.connector
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api

api = Api(app)

@app.route("api/login/", methods=['GET'])
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    # TODO: if database contains username/password combo
    if True:
        return "Logged in", 200
    return "Incorrect username or password", 401

@app.route("api/members/", methods=['GET'])
def get_members():
    # TODO: poll database for all members and return them
    return "", 200

@app.route("api/members/", methods=['POST'])
def add_new_member():
    # TODO: add member to database
    return "", 200

@app.route("api/members/", methods=['PUT'])
def update_member():
    #TODO: update member in database
    return "", 200

@app.route("api/members", methods=['DELETE'])
def delete_member():
    # TODO: delete member from database
    return "", 200

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin",
    database="mydatabase"
)