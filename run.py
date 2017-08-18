DEBUG = True
 
from project import app
from project import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_bootstrap import Bootstrap

import project.mqtt

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

bootstrap = Bootstrap(app)
 
if __name__ == "__main__": 
   manager.run()