from project import db
from project.models import User,Role
 
 
# create the database and the database table
db.drop_all()
db.create_all()
 
role1 = Role('admin')
role2 = Role('guest')

db.session.add(role1)
db.session.add(role2)

db.session.commit()

user1 = User('kontel@mail.ru', 'admin', role1)
user2 = User('guest@mail.ru', 'guest', role2)

db.session.add(user1)
db.session.add(user2)
 
db.session.commit()