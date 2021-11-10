# Group 5
# Jason Kim (jason.j.kim@vanderbilt.edu)
# Blaine Mitchell (blaine.z.mitchell@vanderbilt.edu)
# Bo Peng (bo.peng@vanderbilt.edu)
# Paul Woo (paul.woo@vanderbilt.edu)
# Homework 3

# The announcements file, handling announcements made by administrators and viewable by standard members

from wtforms import Form, StringField, TextAreaField
from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db

from .models import *


announcements = Blueprint('announcements', __name__)

class AnnouncementForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')