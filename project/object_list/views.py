#################
#### imports ####
#################
 
from flask import render_template, Blueprint
from flask_login import login_required
 
 
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
    return render_template('obj_list.html')