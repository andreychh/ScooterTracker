import os

import dotenv
from flask import Flask

from .database import db
from .routes import common_bp, scooter_details_bp


def create_app() -> Flask:
    dotenv.load_dotenv()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

    app.register_blueprint(common_bp)
    app.register_blueprint(scooter_details_bp)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
