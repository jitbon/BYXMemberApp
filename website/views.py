# Group 5
# Jason Kim (jason.j.kim@vanderbilt.edu)
# Blaine Mitchell (blaine.z.mitchell@vanderbilt.edu)
# Bo Peng (bo.peng@vanderbilt.edu)
# Paul Woo (paul.woo@vanderbilt.edu)
# Homework 3

# stores main views/url endpoints - standard routes for websites (where users can go to - homepage, etc.)

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json


views = Blueprint('views', __name__)


# Navigation to login page
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

announcements = Blueprint('announcements', __name__, template_folder='templates')

# Route for creating an announcement
@views.route('/create')
def post_create():
    return render_template('announcements.html')
    
# Route for viewing announcements
@views.route('/announcements', methods=['POST', 'GET'])
@login_required
def announcement_create():
    
    return render_template("announcements.html", user=current_user)