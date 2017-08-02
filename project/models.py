from project import db
from werkzeug.security import generate_password_hash, \
     check_password_hash
from flask_login import UserMixin
 

owners = db.Table('owners',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('object_id', db.Integer, db.ForeignKey('objects.id'))
)
 
class User(UserMixin, db.Model):
 
    __tablename__ = "users"
     
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'),nullable=False)
    objects = db.relationship('ObjDef',secondary = owners, backref = db.backref('users',lazy='dynamic'))
     
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
    
class ObjDef(db.Model):
    __tablename__ = "objects"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(100), nullable=False)
    upd_time = db.Column(db.DateTime, nullable=True)
    
    def __init__(self, name,comment,upd_time):
        self.name = name
        self.comment = comment
        self.upd_time = upd_time
    
    def __repr__(self):
        return '<Name %r>' % self.name