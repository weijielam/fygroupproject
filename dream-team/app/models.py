# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app import db, login_manager

class User(UserMixin, db.Model):
    """
    Create a User table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    needs = db.Column(db.String(300))
    is_subscribed = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prdepartment pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)


     #### PASSWORD RESET CODE ######
    def get_token(self, expiration=1800):
        s = Serializer('SECRET_KEY', expiration)
        return s.dumps({'user': self.id}).decode('utf-8')

    @staticmethod
    def verify_token(token):
        s = Serializer('SECRET_KEY') #####YOU CHANGED THIS IT MAY BE BROKE
        try:
            data = s.loads(token)
        except:
            return None
        id = data.get('user')
        if id:
            return User.query.get(id)
        return None

    #### END PASSWORD RESET CODE #####   

    def __repr__(self):
        return '<User: {}>'.format(self.username)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Event(db.Model):
    """
    Create an events table
    """

    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    timeD = db.Column(db.String(60))
    date = db.Column(db.String(60))
    location = db.Column(db.String(60))
    description = db.Column(db.String(200))
    menus = db.Column(db.String(200))

    def __repr__(self):
        return '<event: {}>'.format(self.name)

'''
Create guest list
'''
class GuestList(db.Model):
    """
    Create guest list table
    """

    __tablename__ = 'guestLists'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    guest_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    is_attending = db.Column(db.Boolean, default=False)
    

    def __repr__(self):
        return '<GuestList: {}>'.format(self.id)



'''
Create payments
'''
class Payments(db.Model):
    """
    Create payments table
    """
    __tablename__= 'payments'  
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    payment_type = db.Column(db.String(20))
    purpose = db.Column(db.String(100))
    date = db.Column(db.String(100))


    def __repr__(self):
        return '<Payment: {}>'.format(self.id)