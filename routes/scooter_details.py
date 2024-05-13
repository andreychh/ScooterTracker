from flask import Blueprint, request, jsonify, Response

from database import db, ChargeData, PositionData, Scooter, ScooterState
from utils import validate_limit, validate_charge_data, validate_position_data, validate_state, validate_model, \
    check_json_fields

bp = Blueprint('scooter_details', __name__)


@bp.before_request
def check_id():
    scooter_id = int(request.view_args['scooter_id'])
    Scooter.query.get_or_404(scooter_id, description='Scooter not found')


# charge
@bp.route('/scooters/<int:scooter_id>/charge', methods=['GET'])
def get_charge_data(scooter_id: int) -> tuple[Response, int]:
    limit = request.args.get('limit', type=int)
    validate_limit(limit)

    charge_data = ChargeData.get_data(scooter_id, limit)
    validate_charge_data(charge_data)

    return jsonify({'charge_data': [data.to_dict() for data in charge_data]}), 200


@bp.route('/scooters/<int:scooter_id>/charge', methods=['POST'])
@check_json_fields('charge')
def add_charge_data(scooter_id: int) -> tuple[Response, int]:
    data = request.get_json()
    db.session.add(ChargeData(scooter_id=scooter_id, charge=data['charge']))
    db.session.commit()

    return jsonify({'message': 'Scooters charge data updated successfully'}), 201


# position
@bp.route('/scooters/<int:scooter_id>/position', methods=['GET'])
def get_position_data(scooter_id: int) -> tuple[Response, int]:
    limit = request.args.get('limit', type=int)
    validate_limit(limit)

    position_data = PositionData.get_data(scooter_id, limit)
    validate_position_data(position_data)

    return jsonify({'position_data': [data.to_dict() for data in position_data]}), 200


@bp.route('/scooters/<int:scooter_id>/position', methods=['POST'])
@check_json_fields('latitude', 'longitude')
def add_position_data(scooter_id: int) -> tuple[Response, int]:
    data = request.get_json()
    db.session.add(PositionData(scooter_id=scooter_id, latitude=data['latitude'], longitude=data['longitude']))
    db.session.commit()

    return jsonify({'message': 'Scooters position data updated successfully'}), 201


# state
@bp.route('/scooters/<int:scooter_id>/state', methods=['GET'])
def get_state(scooter_id: int) -> tuple[Response, int]:
    scooter = Scooter.query.get(scooter_id)
    return jsonify({'state': scooter.state}), 200


@bp.route('/scooters/<int:scooter_id>/state', methods=['PUT'])
@check_json_fields('state')
def update_state(scooter_id: int) -> tuple[Response, int]:
    data = request.get_json()
    state = data['state']
    validate_state(state)

    scooter = Scooter.query.get(scooter_id)
    scooter.state = ScooterState(state)
    db.session.commit()

    return jsonify({'message': 'Scooters state updated successfully'}), 200


# model
@bp.route('/scooters/<int:scooter_id>/model', methods=['GET'])
def get_model(scooter_id: int) -> tuple[Response, int]:
    scooter = Scooter.query.get(scooter_id)
    return jsonify({'model': scooter.model}), 200


@bp.route('/scooters/<int:scooter_id>/model', methods=['PUT'])
@check_json_fields('model')
def update_model(scooter_id: int) -> tuple[Response, int]:
    data = request.get_json()
    model = data['model']
    validate_model(model)

    scooter = Scooter.query.get(scooter_id)
    scooter.model = model
    db.session.commit()

    return jsonify({'message': 'Scooters model updated successfully'}), 200


# other
@bp.route('/scooters/<int:scooter_id>', methods=['DELETE'])
def delete_scooter(scooter_id) -> tuple[Response, int]:
    db.session.delete(Scooter.query.get(scooter_id))
    db.session.commit()
    return jsonify({'message': 'Scooter deleted successfully'}), 200


@bp.route('/scooters/<int:scooter_id>', methods=['GET'])
def get_scooter(scooter_id) -> tuple[Response, int]:
    return jsonify(Scooter.query.get(scooter_id).to_dict()), 200
