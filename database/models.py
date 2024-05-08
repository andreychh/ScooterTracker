import datetime as dt

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Scooter(db.Model):
    __tablename__ = 'scooter'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String(100), nullable=False)
    # state

    charge_data = db.relationship('ChargeData', back_populates='scooter')
    location_data = db.relationship('LocationData', back_populates='scooter')

    def __repr__(self):
        return '<Scooter %r>' % self.id

    def to_json(self):
        return {
            'model': self.model,
            # TODO: return last charge and locate data
        }


class ChargeData(db.Model):
    __tablename__ = 'charge_data'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datetime = db.Column(db.DateTime, default=dt.datetime.now)
    scooter_id = db.Column(db.Integer, db.ForeignKey('scooter.id'), nullable=False)
    charge = db.Column(db.Float, nullable=False)

    scooter = db.relationship('Scooter', back_populates='charge_data')

    def __repr__(self):
        return '<ChargeData %r>' % self.id

    def to_json(self):
        return {
            'datetime': self.datetime,
            'charge': self.charge,
        }


class LocationData(db.Model):
    __tablename__ = 'location_data'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datetime = db.Column(db.DateTime, default=dt.datetime.now)
    scooter_id = db.Column(db.Integer, db.ForeignKey('scooter.id'), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    scooter = db.relationship('Scooter', back_populates='location_data')

    def __repr__(self):
        return '<LocationData %r>' % self.id

    def to_json(self):
        return {
            'datetime': self.datetime,
            'latitude': self.latitude,
            'longitude': self.longitude,
        }
