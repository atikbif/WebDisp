from project import db
from project.models import User,Role,ObjDef
from datetime import datetime
 
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

object1 = ObjDef('котельная Пушкина, 10','детский сад',None)
object2 = ObjDef('котельная Лермонтова, 20','школа',datetime.utcnow())
object3 = ObjDef('котельная Чехова, 30','больница',None)

db.session.add(object1)
db.session.commit()

db.session.add(object2)
db.session.commit()

db.session.add(object3)
db.session.commit()

user1.objects.append(object1)
user1.objects.append(object2)
user1.objects.append(object3)
db.session.commit()

user2.objects.append(object1)
user2.objects.append(object3)
db.session.commit()

for ob in user1.objects:
    print(ob.name)
    
print()    
    
for ob in user2.objects:
    print(ob.name)
    
print()

for us in object1.users:
    print(us.email)
    
print()

for us in object2.users:
    print(us.email)
    
    