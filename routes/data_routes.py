from flask import Blueprint, request

from database import db, ChargeData, LocationData
from routes.utils import *

bp = Blueprint('data', __name__)


@bp.route('/scooters/<int:scooter_id>/charge', methods=['GET'])
def get_charge_data(scooter_id):
    limit = request.args.get('limit', type=int)  # TODO: try extract method

    if limit is not None and limit <= 0:
        return jsonify({'error': 'Parameter "limit" must be a positive integer'}), 400

    charge_data = ChargeData.query.filter_by(scooter_id=scooter_id).order_by(ChargeData.datetime.desc()) \
        .limit(limit).all()

    if charge_data:
        return jsonify({'charge_data': format_charge_data(charge_data)})
    else:
        return jsonify({'error': 'Charge data not found'}), 404


@bp.route('/scooters/<int:scooter_id>/charge', methods=['POST'])
def post_charge_data(scooter_id):
    if not request.is_json:
        return get_json_error()

    data = request.get_json()

    if 'charge' not in data:
        return get_field_error('charge')

    db.session.add(ChargeData(scooter_id=scooter_id, charge=data['charge']))
    db.session.commit()

    return jsonify({'message': 'Scooters charge data updated successfully'}), 201


@bp.route('/scooters/<int:scooter_id>/location', methods=['GET'])
def get_location_data(scooter_id):
    limit = request.args.get('limit', type=int)  # TODO: try extract method

    if limit is not None and limit <= 0:
        return jsonify({'error': 'Parameter "limit" must be a positive integer'}), 400

    location_data = LocationData.query.filter_by(scooter_id=scooter_id).order_by(LocationData.datetime.desc()) \
        .limit(limit).all()

    if location_data:
        return jsonify({'charge_data': format_location_data(location_data)})
    else:
        return jsonify({'error': 'Charge data not found'}), 404


@bp.route('/scooters/<int:scooter_id>/location', methods=['POST'])
def post_location_data(scooter_id):
    if not request.is_json:
        return get_json_error()

    data = request.get_json()

    if 'latitude' not in data:
        return get_field_error('latitude')

    if 'longitude' not in data:
        return get_field_error('longitude')

    db.session.add(LocationData(scooter_id=scooter_id, latitude=data['latitude'], longitude=data['longitude']))
    db.session.commit()

    return jsonify({'message': 'Scooters location data updated successfully'}), 201
