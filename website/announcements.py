from wtforms import Form, StringField, TextAreaField
from flask import Blueprint, render_template, request, flash, redirect, url_for

announcements = Blueprint('announcements', __name__)

class AnnouncementForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')
    