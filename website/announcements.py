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

@announcements.route('/create', methods=['POSTS', 'GET'])
def announcement_create():
    form = PostForm()
    
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        
        try:
            post = Post(title=title, body=body)
            db.session.add(announcement)
            db.session.commit()
        except:
            print('Very long traceback')
        return redirect(url_for('announcements.announcement_detail', slug=post.slug))
            
    return render_template('announcement_create.html', form=form)

@announcements.route('/')
def announcements_list():
    q = request.args.get('q')
    
    if q:
        announcements = Post.query.filter(Post.title.contains(q) | Post.body.contains(q))
    else: 
        announcements = Post.query.order_by(Post.created.desc())
        
    return render_template('announcements.html', announcements=announcements)
    
@announcements.route('/<slug>/edit', methods=['POST','GET'])
def announcement_update(slug):
    announcement = Post.query.filter(Post.slug==slug).first()
    
    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=announcement)
        form.populate_obj(announcement)
        db.session.commit()
        return redirect(url_for('announcements.announcement_detail',slug=announcement.slug))
    
    form=PostForm(obj=post)
    
    return render_template('announcements_edit.html', post=post, form=form)