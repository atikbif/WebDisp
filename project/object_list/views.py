#################
#### imports ####
#################
 
from flask import render_template, Blueprint,session,abort,jsonify
from flask_login import login_required
from project.models import User
 
 
################
#### config ####
################
 
object_list_blueprint = Blueprint('object_list', __name__, template_folder='templates')
 
 
################
#### routes ####
################
 
@object_list_blueprint.route('/list')
@login_required
def obj_list():
    user = User.query.filter_by(email = session['email']).first()
    if user is not None:
        return render_template('obj_list.html',objects = user.objects)
    return render_template('users.logout')

@object_list_blueprint.route('/list_upd')
@login_required
def obj_upd_time():
    user = User.query.filter_by(email = session['email']).first()
    if user is not None:
        objects = user.objects
        times = list()
        for ob in objects:
            times.append(ob.input_data[0].upd_time.strftime("%d %m %Y   %H:%M:%S"))
        info = {
            "upd_time": times
        }
        return jsonify(info)
    return abort(404)