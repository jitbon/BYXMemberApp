# stores main views/url endpoints - standard routes for websites (where users can go to - homepage, etc.)

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json
from models import *
from .announcements import PostForm


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

announcements = Blueprint('announcements', __name__, template_folder='templates')

@views.route('/create')
def post_create():
    announcement = PostForm()
    return render_template('announcements.html')
    

@views.route('/announcements', methods=['POST', 'GET'])
@login_required
def announcement_create():
    
    return render_template("announcements.html", user=current_user)