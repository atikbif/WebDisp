#################
#### imports ####
#################
 
from flask import render_template, Blueprint
 
 
################
#### config ####
################
 
object_list_blueprint = Blueprint('object_list', __name__, template_folder='templates')
 
 
################
#### routes ####
################
 
@object_list_blueprint.route('/list')
def obj_list():
    return render_template('obj_list.html')