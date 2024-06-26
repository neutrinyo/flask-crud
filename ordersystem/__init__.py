from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .config import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_mode: str):
    app = Flask(__name__)
    print(f'>{config_mode}<')

    app.config.from_object(config[config_mode])

    db.init_app(app)
    migrate.init_app(app, db)

    if config_mode == "testing":
        with app.app_context():
            from flask_migrate import upgrade  
            upgrade()

    return app