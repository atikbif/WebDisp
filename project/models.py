from project import db
from werkzeug.security import generate_password_hash, \
     check_password_hash
from flask_login import UserMixin
 
 
class User(UserMixin, db.Model):
 
    __tablename__ = "users"
     
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'),nullable=False)

     
    def __init__(self, email, password, user_role):
        self.email = email
        self.password = generate_password_hash(password)
        self.role_id = user_role.id
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
     
    def __repr__(self):
        return '<User %r>' % self.email

class Role(db.Model):
    __tablename__ = "roles"
    
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(50), nullable=False)
    users = db.relationship('User', backref='role', lazy=True)

    
    def __init__(self, role):
        self.role = role
    
    def __repr__(self):
        return '<Role %r>' % self.role