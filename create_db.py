from project import db
from project.models import User,Role,ObjDef,InpData,DiscrDef,AnalogDef,MessageDef
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

object1 = ObjDef(name='котельная Пушкина, 10',comment='детский сад',discr_count=5,analog_count=5,message_count=5)
object2 = ObjDef(name='котельная Лермонтова, 20',comment='школа',discr_count=5,analog_count=5,message_count=5)
object3 = ObjDef(name='котельная Чехова, 30',comment='больница',discr_count=5,analog_count=5,message_count=5)

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
print()

inp1 = (0x01,0x00,0x00,0x01,0x01,0x01,0x23,0x00,0x45,0x00,0x10,0x01,0x01,0x00,0x23,0x00,0x01,0x01,0x00,0x01)    
data1 = InpData(inp1,datetime.utcnow(),object1)

inp2 = (0x00,0x01,0x00,0x00,0x01,0x00,0x23,0x00,0x05,0x01,0x00,0x00,0x31,0x00,0x03,0x01,0x01,0x00,0x01,0x01)    
data2 = InpData(inp2,datetime.utcnow(),object2)

inp3 = (0x01,0x01,0x01,0x00,0x00,0x00,0x56,0x00,0x85,0x01,0x40,0x60,0x38,0x00,0xA3,0x00,0x00,0x00,0x01,0x00)    
data3 = InpData(inp3,datetime.utcnow(),object3)
    
db.session.add(data1)
db.session.commit()

db.session.add(data2)
db.session.commit()

db.session.add(data3)
db.session.commit()




discr_1_1 = DiscrDef(name='пожар',comment='',offset=0,obj=object1)
db.session.add(discr_1_1)
discr_1_2 = DiscrDef(name='охрана',comment='',offset=1,obj=object1)
db.session.add(discr_1_2)
discr_1_3 = DiscrDef(name='CO',comment='',offset=2,obj=object1)
db.session.add(discr_1_3)
discr_1_4 = DiscrDef(name='CH4',comment='',offset=3,obj=object1)
db.session.add(discr_1_4)
discr_1_5 = DiscrDef(name='газовый клапан',comment='',offset=4,obj=object1)
db.session.add(discr_1_5)

db.session.commit()

for d in object1.discretes:
    print(d.offset)

discr_2_1 = DiscrDef(name='насос 1',comment='',offset=0,obj=object2)
db.session.add(discr_2_1)
discr_2_2 = DiscrDef(name='насос 2',comment='',offset=1,obj=object2)
db.session.add(discr_2_2)
discr_2_3 = DiscrDef(name='клапан 1',comment='',offset=2,obj=object2)
db.session.add(discr_2_3)
discr_2_4 = DiscrDef(name='клапан 2',comment='',offset=3,obj=object2)
db.session.add(discr_2_4)
discr_2_5 = DiscrDef(name='вентиляция 1',comment='',offset=4,obj=object2)
db.session.add(discr_2_5)

db.session.commit()

discr_3_1 = DiscrDef(name='загазованность зона 1',comment='подвал',offset=0,obj=object3)
db.session.add(discr_3_1)
discr_3_2 = DiscrDef(name='загазованность зона 2',comment='гараж',offset=1,obj=object3)
db.session.add(discr_3_2)
discr_3_3 = DiscrDef(name='загазованность зона 3',comment='стоянка',offset=2,obj=object3)
db.session.add(discr_3_3)
discr_3_4 = DiscrDef(name='загазованность зона 4',comment='проходная',offset=3,obj=object3)
db.session.add(discr_3_4)
discr_3_5 = DiscrDef(name='загазованность зона 5',comment='склад',offset=4,obj=object3)
db.session.add(discr_3_5)

db.session.commit()

an_1_1 = AnalogDef(name='T помещения', comment='',measure='град',sign=False,coeff=0.1,offset=5,obj=object1)
db.session.add(an_1_1)
an_1_2 = AnalogDef(name='T нар', comment='',measure='град',sign=True,coeff=0.1,offset=7,obj=object1)
db.session.add(an_1_2)
an_1_3 = AnalogDef(name='T котла 1', comment='',measure='град',sign=False,coeff=0.1,offset=9,obj=object1)
db.session.add(an_1_3)
an_1_4 = AnalogDef(name='T котла 2', comment='',measure='град',sign=False,coeff=0.1,offset=11,obj=object1)
db.session.add(an_1_4)
an_1_5 = AnalogDef(name='T котла 3', comment='',measure='град',sign=False,coeff=0.1,offset=13,obj=object1)
db.session.add(an_1_5)
    
db.session.commit()

an_2_1 = AnalogDef(name='P1', comment='давление после насоса 1',measure='бар',sign=False,coeff=0.01,offset=5,obj=object2)
db.session.add(an_2_1)
an_2_2 = AnalogDef(name='P2', comment='давление после насоса 2',measure='бар',sign=False,coeff=0.01,offset=7,obj=object2)
db.session.add(an_2_2)
an_2_3 = AnalogDef(name='P3', comment='давление после насоса 3',measure='бар',sign=False,coeff=0.01,offset=9,obj=object2)
db.session.add(an_2_3)
an_2_4 = AnalogDef(name='P4', comment='давление после насоса 4',measure='бар',sign=False,coeff=0.01,offset=11,obj=object2)
db.session.add(an_2_4)
an_2_5 = AnalogDef(name='P5', comment='давление после насоса 5',measure='бар',sign=False,coeff=0.01,offset=13,obj=object2)
db.session.add(an_2_5)
    
db.session.commit()

an_3_1 = AnalogDef(name='T1', comment='температура зона 1',measure='подвал',sign=True,coeff=0.1,offset=5,obj=object3)
db.session.add(an_3_1)
an_3_2 = AnalogDef(name='T2', comment='температура зона 2',measure='гараж',sign=True,coeff=0.1,offset=7,obj=object3)
db.session.add(an_3_2)
an_3_3 = AnalogDef(name='T3', comment='температура зона 3',measure='стоянка',sign=True,coeff=0.1,offset=9,obj=object3)
db.session.add(an_3_3)
an_3_4 = AnalogDef(name='T4', comment='температура зона 4',measure='проходная',sign=True,coeff=0.1,offset=11,obj=object3)
db.session.add(an_3_4)
an_3_5 = AnalogDef(name='T5', comment='температура зона 5',measure='склад',sign=True,coeff=0.1,offset=13,obj=object3)
db.session.add(an_3_5)
    
db.session.commit()

ms_1_1 = MessageDef(message = 'запуск системы',offset = 15,alarm_level=0,obj=object1)
db.session.add(ms_1_1)
ms_1_2 = MessageDef(message = 'Низкое давление теплосети',offset = 16,alarm_level=1,obj=object1)
db.session.add(ms_1_2)
ms_1_3 = MessageDef(message = 'Отключение питания',offset = 17,alarm_level=2,obj=object1)
db.session.add(ms_1_3)
ms_1_4 = MessageDef(message = 'Низкая температура помещения',offset = 18,alarm_level=1,obj=object1)
db.session.add(ms_1_4)
ms_1_5 = MessageDef(message = 'ручной режим',offset = 19,alarm_level=0,obj=object1)
db.session.add(ms_1_5)

db.session.commit()

ms_2_1 = MessageDef(message = 'Высокая температура котла 1',offset = 15,alarm_level=2,obj=object2)
db.session.add(ms_2_1)
ms_2_2 = MessageDef(message = 'Высокая температура котла 2',offset = 16,alarm_level=2,obj=object2)
db.session.add(ms_2_2)
ms_2_3 = MessageDef(message = 'Высокая температура котла 3',offset = 17,alarm_level=2,obj=object2)
db.session.add(ms_2_3)
ms_2_4 = MessageDef(message = 'Розжиг горелки 1',offset = 18,alarm_level=0,obj=object2)
db.session.add(ms_2_4)
ms_2_5 = MessageDef(message = 'Розжиг горелки 2',offset = 19,alarm_level=0,obj=object2)
db.session.add(ms_2_5)

db.session.commit()

ms_3_1 = MessageDef(message = 'Проникновение в зону 1',offset = 15,alarm_level=2,obj=object3)
db.session.add(ms_3_1)
ms_3_2 = MessageDef(message = 'Проникновение в зону 2',offset = 16,alarm_level=2,obj=object3)
db.session.add(ms_3_2)
ms_3_3 = MessageDef(message = 'Проникновение в зону 3',offset = 17,alarm_level=2,obj=object3)
db.session.add(ms_3_3)
ms_3_4 = MessageDef(message = 'Проникновение в зону 4',offset = 18,alarm_level=1,obj=object3)
db.session.add(ms_3_4)
ms_3_5 = MessageDef(message = 'Проникновение в зону 5',offset = 19,alarm_level=1,obj=object3)
db.session.add(ms_3_5)

db.session.commit()