#################
#### imports ####
#################
 
from flask import render_template, Blueprint
from flask_login import login_required
 
 
################
#### config ####
################
 
object_state_blueprint = Blueprint('object_state', __name__, template_folder='templates')
 
 
################
#### routes ####
################
 
@object_state_blueprint.route('/state')
@login_required
def state():
    return render_template('obj_state.html')