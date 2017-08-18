#################
#### imports ####
#################
 
from flask import render_template, Blueprint,session,abort,jsonify
from flask_login import login_required
from project.models import ObjDef
from .obj_state import ObjState
 
 
################
#### config ####
################
 
object_state_blueprint = Blueprint('object_state', __name__, template_folder='templates')
 
 
################
#### routes ####
################
 
@object_state_blueprint.route('/state/<int:id>')
@login_required
def state(id):
    ob = ObjDef.query.filter_by(id = id).first()
    if ob is None:
        return abort(404)
    user_check = False
    for user in ob.users:
        if session['email']==user.email:
            user_check = True
    if user_check:
        dis = ob.discretes
        ais = ob.analogs
        dt = ob.input_data[0]
        mss = ob.messages
        obs = ObjState(name=ob.name,comment=ob.comment,upd_time=dt.upd_time,id=id)
        for di in dis:
            if di.enable:
                value = dt.data[di.offset]
                obs.add_discr(di.name,di.comment,value)
        for ai in ais:
            if ai.enable:
                value = (dt.data[ai.offset]*256 + dt.data[ai.offset+1])*ai.coeff
                obs.add_analog(ai.name,ai.comment,ai.measure,value)
        for ms in mss:
            if ms.enable:
                value = dt.data[ms.offset]
                if value:
                    obs.add_message(ms.message,ms.alarm_level)
        return render_template('obj_state.html',obj_var = obs)
    return abort(404)

@object_state_blueprint.route('/obj_info/<int:id>')
@login_required
def info(id):
    ob = ObjDef.query.filter_by(id = id).first()
    if ob is None:
        return abort(404)
    user_check = False
    for user in ob.users:
        if session['email']==user.email:
            user_check = True
    if user_check:
        di_values=list()
        ai_values = list()
        alarms = list()
        warnings = list()
        infos = list()
        for di in ob.discretes:
            if di.enable:
                di_values.append(ob.input_data[0].data[di.offset])
        for ai in ob.analogs:
            if ai.enable:
                value = (ob.input_data[0].data[ai.offset]*256 + ob.input_data[0].data[ai.offset+1])
                if ai.sign and value>32767:
                    value=(65536-value)*-1
                value = value * ai.coeff
                ai_values.append(value)
        for ms in ob.messages:
            if ms.enable:
                value = ob.input_data[0].data[ms.offset]
                if value:
                    if ms.alarm_level == 2:
                        alarms.append(ms.message)
                    if ms.alarm_level == 1:
                        warnings.append(ms.message)
                    if ms.alarm_level == 0:
                        infos.append(ms.message)
        time_str = "Нет данных"
        if ob.input_data[0].upd_time is not None:
            time_str = ob.input_data[0].upd_time.strftime("%d-%m-%Y   %H:%M:%S")
        info = {
            "di" : di_values,
            "ai" : ai_values,
            "alarm" : alarms,
            "warning" : warnings,
            "info" : infos,
            "time" : time_str 
        }

        return jsonify(info)
    return abort(404)