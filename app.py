import os

import dotenv
from flask import Flask

from database import db
from routes import common_bp, scooter_details_bp

dotenv.load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

app.register_blueprint(common_bp)
app.register_blueprint(scooter_details_bp)

db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
