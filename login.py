import re
from main import app
from flask import request
import mysql.connector
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


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

def call_add_member():
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()

        args = ["last name", "first name", "role", "class", num]
        result_args = cursor.callproc('addMember', args)

        print(result_args)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def call_delete_member():
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()

        args = ["last name", "first name"]
        result_args = cursor.callproc('deleteMember', args)

        print(result_args)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def call_find_member():
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()

        args = ["last name", "first name"]
        result_args = cursor.callproc('findMember', args)

        print(result_args)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()