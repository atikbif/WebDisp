#################
#### imports ####
#################
 
from flask import render_template, Blueprint,session,abort
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
        obs = ObjState(name=ob.name,comment=ob.comment,upd_time=dt.upd_time)
        for di in dis:
            value = dt.data[di.offset]
            obs.add_discr(di.name,di.comment,value)
        for ai in ais:
            value = (dt.data[ai.offset]*256 + dt.data[ai.offset+1])*ai.coeff
            obs.add_analog(ai.name,ai.comment,ai.measure,value)
        for ms in mss:
            value = dt.data[ms.offset]
            if value:
                obs.add_message(ms.message,ms.alarm_level)
        return render_template('obj_state.html',obj_var = obs)
    return abort(404)