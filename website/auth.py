# Group 5
# Jason Kim (jason.j.kim@vanderbilt.edu)
# Blaine Mitchell (blaine.z.mitchell@vanderbilt.edu)
# Bo Peng (bo.peng@vanderbilt.edu)
# Paul Woo (paul.woo@vanderbilt.edu)
# Homework 3

# auth.py handles the login/signup functionality, as well as the paths to go after doing so. 

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from quickstart import scheduleEvent
from datetime import datetime

auth = Blueprint('auth', __name__)

# Loggin into an account
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

# Logging out
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# Signing up for an account, creating a new one
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)

# Navigation to search page after authorization
@auth.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'POST':
        email = request.form.get('email')
        profile = User.query.filter_by(email=email).first()
        if profile:
            return render_template("home.html", user=profile)
        else:
            flash('Error: user not found', category='error')

    return render_template("search.html", user=current_user)

# Navigation to schedule page after authorization
@auth.route('/schedule', methods=['GET', 'POST'])
@login_required
def schedule():
    if request.method == 'POST':
        summary = request.form.get('summary', type=str)
        location = request.form.get('location', type=str)
        description = request.form.get('description', type=str)
        startTime = request.form.get('start time', type=str)
        endTime = request.form.get('end time', type=str)
        startConv = datetime.strptime(startTime, '%Y-%m-%dT%H:%M')
        endConv = datetime.strptime(endTime, '%Y-%m-%dT%H:%M')

        if startConv > endConv:
            flash('start time is later than end time', category='error')
        else:
            scheduleEvent(summary, location, description, startTime, endTime)

    return render_template("schedule.html", user=current_user)

# Handling when the user updates their profile
@auth.route('/updateProfile', methods=['GET', 'POST'])
@login_required
def update_profile():
    if request.method == 'POST':
        current_user.first_name = request.form.get('first_name')
        current_user.last_name = request.form.get('last_name')
        current_user.email = request.form.get('email')

    return render_template("home.html", user=current_user)


# return redirect(url_for('views.home'))
