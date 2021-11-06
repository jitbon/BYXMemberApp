# Group 5
# Jason Kim (jason.j.kim@vanderbilt.edu)
# Blaine Mitchell (blaine.z.mitchell@vanderbilt.edu)
# Bo Peng (bo.peng@vanderbilt.edu)
# Paul Woo (paul.woo@vanderbilt.edu)
# Homework 3

# make website folder a python package

from flask import Flask, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from os import path
from flask_login import LoginManager

from flask_migrate import Migrate
from flask_script import Manager 

from .models import *

from flask_security import login_required
from flask_security import SQLAlchemyUserDatastore
from flask_security import Security
from flask_security import current_user

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .announcements import announcements

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(announcements, url_prefix='/announcements')

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    migrate = Migrate(app, db)
    
    manager.add_command('db', MigrateCommand)
    # commands for the Admin's access to the app
    admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView(name='Home'))
    admin.add_view(ModelView(Post, db.session))
    
    #Flask security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)
    

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
        
# Admin permissions, what they can access
class AdminMixin:
    def isAccessible(self):
        return current_user.has_role('admin')
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', 
                                next=request.url))
        
# Pages will be set up differently for the admin.
# For example, only admins can make announcements, add/remove members
class AdminView(AdminMixin, ModelView):
    pass
        
class HomeAdminView(AdminMixin, AdminIndexView):
    pass

class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        if is_created:
            model.generate_slug()
        return super().on_model_change(form, model, is_created)
    
class AnnouncementModelView(AdminMixin, BaseModelView):
    form_columns = ['title', 'body', 'tags']
            