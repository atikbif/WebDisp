#################
#### imports ####
#################
 
from flask import render_template, Blueprint
 
 
################
#### config ####
################
 
object_state_blueprint = Blueprint('object_state', __name__, template_folder='templates')
 
 
################
#### routes ####
################
 
@object_state_blueprint.route('/state')
def state():
    return render_template('obj_state.html')