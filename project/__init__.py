from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

####################
#### blueprints ####
####################
 
from project.users.views import users_blueprint
from project.object_list.views import object_list_blueprint
from project.object_state.views import object_state_blueprint
 
# register the blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(object_list_blueprint)
app.register_blueprint(object_state_blueprint)
