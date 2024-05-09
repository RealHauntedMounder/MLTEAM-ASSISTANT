from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_admin import Admin
from flask import Flask
from flask_babel import Babel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
babel = Babel()

def create_app():
    application = Flask(__name__)
  
    application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/project'
    application.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    db.init_app(application)
    bcrypt.init_app(application)
    #login_manager.init_app(application)
    migrate.init_app(application, db)
    babel.init_app(application)

    
    return application
