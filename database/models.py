import datetime
from typing import Type

from flask_sqlalchemy import SQLAlchemy

from .misc import Base, ScooterState, camel_to_snake

db = SQLAlchemy(model_class=Base)


class Scooter(db.Model):
    __tablename__ = 'scooter'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String(64), nullable=False)
    state = db.Column(db.Enum(ScooterState), default=ScooterState.ACTIVE, nullable=False)

    charge_data = db.relationship(
        'ChargeData',
        backref='scooter',
        cascade='all, delete',
        passive_deletes=True,
        order_by=lambda: db.desc(ChargeData.recorded_at)
    )
    position_data = db.relationship(
        'PositionData',
        backref='scooter',
        cascade='all, delete',
        passive_deletes=True,
        order_by=lambda: db.desc(PositionData.recorded_at)
    )

    def to_dict(self) -> dict[str, ...]:
        return {
            'id': self.id,
            'model': self.model,
            'charge_data': self.charge_data[0].to_dict() if self.charge_data else None,
            'position_data': self.position_data[0].to_dict() if self.position_data else None,
        }


class SensorData[T](db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    scooter_id = db.Column(db.Integer, db.ForeignKey('scooter.id', ondelete='CASCADE'), nullable=False)
    recorded_at = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)

    @classmethod
    @db.declared_attr
    def __tablename__(cls) -> str:
        return camel_to_snake(cls.__name__)

    @classmethod
    @db.declared_attr
    def scooter(cls) -> db.RelationshipProperty:
        return db.relationship('Scooter', backref=camel_to_snake(cls.__name__))

    @classmethod
    def get_data(cls: Type[T], scooter_id: int, limit: int | None = None) -> list[T]:
        return cls.query.filter_by(scooter_id=scooter_id).order_by(cls.recorded_at.desc()).limit(limit).all()

    def to_dict(self):
        raise NotImplementedError("Method to_dict() must be implemented in subclasses.")


class ChargeData(SensorData):
    charge = db.Column(db.Float, nullable=False)

    def to_dict(self) -> dict[str, ...]:
        return {
            'recorded_at': self.recorded_at,
            'charge': self.charge,
        }


class PositionData(SensorData):
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def to_dict(self) -> dict[str, ...]:
        return {
            'recorded_at': self.recorded_at,
            'latitude': self.latitude,
            'longitude': self.longitude,
        }
