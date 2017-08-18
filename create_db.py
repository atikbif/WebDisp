from project import db
from project.models import User,Role,ObjDef,InpData,DiscrDef,AnalogDef,MessageDef
import json

with open('instance/db_conf.json') as data_file: 
    data = json.load(data_file)
    
    db.drop_all()
    db.create_all()
    
    role1 = Role('admin')
    role2 = Role('guest')
    
    db.session.add(role1)
    db.session.add(role2)
    
    db.session.commit()
    
    users = list()
    
    for user in data["users"]:
        us = User(user["email"],user["password"], role1)
        users.append(us)
        db.session.add(us)
        
    db.session.commit()
    
    for ob in data["objects"]:
        obj = ObjDef(name = ob["name"],comment=ob["comment"],discr_count=len(ob["discr"]),analog_count=len(ob["regs"]),message_count=len(ob["messages"]),enable=(ob["enable"]!="0"))
        db.session.add(obj)
        db.session.commit()
        
        for ob_us in ob["users"]:
            for user in users:
                if ob_us==user.email:
                    user.objects.append(obj)
                    db.session.commit()
        inp=[0]*256
        inp_data = InpData(topic=ob["topic"],data=inp,upd_time=None,obj=obj)
        db.session.add(inp_data)
        db.session.commit()
        
        for i in range(obj.discr_count):
            di = DiscrDef(name=ob["discr"][i]["name"],comment=ob["discr"][i]["comment"],offset=i,obj=obj,enable=(ob["discr"][i]["enable"]!="0"))
            db.session.add(di)
            db.session.commit()
            
        for i in range(obj.analog_count):
            ai = AnalogDef(name=ob["regs"][i]["name"],comment=ob["regs"][i]["comment"],measure=ob["regs"][i]["meas"],sign=ob["regs"][i]["sign"],coeff=ob["regs"][i]["coeff"],offset=i*2+obj.discr_count,obj=obj,enable=(ob["regs"][i]["enable"]!="0"))
            db.session.add(ai)
            db.session.commit()
        
        for i in range(obj.message_count):
            ms = MessageDef(message=ob["messages"][i]["name"],alarm_level=int(ob["messages"][i]["alarm"]),obj=obj,offset = obj.discr_count + 2*obj.analog_count+i,enable=(ob["messages"][i]["enable"]!="0"))
            db.session.add(ms)
            db.session.commit()

