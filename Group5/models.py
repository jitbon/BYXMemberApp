from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from Group5 import db, login_manager, app
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    # User to UserProfile relationship
    # user_profile_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=True, default=None)
    # user_profile = db.relationship('UserProfile', uselist=False)

    # roles = db.relationship('Role', secondary='user_roles',
    #                         backref=db.backref('users', lazy='dynamic'))

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


# class Role(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(50), unique=True)
#
#
# # Define the UserRoles data model
# class UserRoles(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
#     role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))
class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Extra model fields
    first_name = db.Column(db.String(50), nullable=False, default='')
    last_name = db.Column(db.String(50), nullable=False, default='')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # # Define the Role data model
    # class Role(db.Model):
    #     id = db.Column(db.Integer(), primary_key=True)
    #     name = db.Column(db.String(50), unique=True)
    #
    # # Define the UserRoles data model
    # class UserRoles(db.Model):
    #     id = db.Column(db.Integer(), primary_key=True)
    #     user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    #     role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))

    #
    # class Role(db.Model):
    #     __tablename__ = 'roles'
    #     id = db.Column(db.Integer(), primary_key=True)
    #     name = db.Column(db.String(50), unique=True)
    #
    #
    # class UserRoles(db.Model):
    #     year = db.Column(db.String(120), default='')
    #     major = db.Column(db.String(120), default='')

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
#
# # Use User and UserProfile objects
# db_adapter = SQLAlchemyAdapter(db, UserClass=User, UserProfileClass=Member)
