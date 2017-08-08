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
    comment = db.Column(db.String(100))
    discr_count = db.Column(db.Integer)
    discretes = db.relationship('DiscrDef',backref='parent_object',lazy=True)
    analog_count = db.Column(db.Integer)
    analogs = db.relationship('AnalogDef',backref='parent_object',lazy=True)
    message_count = db.Column(db.Integer)
    messages = db.relationship('MessageDef',backref='parent_object',lazy=True)
    
    
    def __init__(self, name,comment,discr_count,analog_count,message_count):
        self.name = name
        self.comment = comment
        self.discr_count = discr_count
        self.analog_count = analog_count
        self.message_count = message_count
    
    def __repr__(self):
        return '<Name %r>' % self.name
    
class InpData(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.LargeBinary(500))
    upd_time = db.Column(db.DateTime)
    obj_id = db.Column(db.Integer, db.ForeignKey('objects.id'),nullable=False)
    parent_object = db.relationship('ObjDef',backref='input_data')
    
    def __init__(self,data,upd_time,obj):
        self.data = data
        self.upd_time = upd_time
        self.obj_id = obj.id
        
    def __repr__(self):
        return '<Data %r>' %self.data
    
class DiscrDef(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    comment = db.Column(db.String(100))
    offset = db.Column(db.Integer)
    obj_id = db.Column(db.Integer, db.ForeignKey('objects.id'),nullable=False)
    
    def __init__(self,name,comment,offset,obj):
        self.name = name
        self.comment = comment
        self.offset = offset
        self.obj_id = obj.id
        
    def __repr__(self):
        return '<Name %r>' %self.name
    
class AnalogDef(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    comment = db.Column(db.String(100))
    measure = db.Column(db.String(50))
    offset = db.Column(db.Integer)
    sign = db.Column(db.Boolean)
    coeff = db.Column(db.Float)
    obj_id = db.Column(db.Integer, db.ForeignKey('objects.id'),nullable=False)
    
    def __init__(self,name,comment,measure,offset,sign,coeff,obj):
        self.name = name
        self.comment = comment
        self.measure = measure
        self.offset = offset
        self.sign = sign
        self.coeff = coeff
        self.obj_id = obj.id
    
    def __repr__(self):
        return '<Name> %r' %self.name

class MessageDef(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    message = db.Column(db.String(200),nullable=False)
    alarm_level = db.Column(db.Integer)
    offset = db.Column(db.Integer)
    obj_id = db.Column(db.Integer, db.ForeignKey('objects.id'),nullable=False)
    
    def __init__(self,message,offset,obj,alarm_level=0):
        self.message = message
        self.offset = offset
        self.alarm_level = alarm_level
        self.obj_id = obj.id
        
    def __repr__(self):
        return '<Message> %r' %self.message
        
    

    



