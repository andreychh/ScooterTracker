from flask import Blueprint, request, jsonify, Response

from database import db, Scooter, ScooterState
from utils import check_json_fields, validate_state

bp = Blueprint('common', __name__)


@bp.route('/scooters', methods=['POST'])
@check_json_fields('model')
def post_scooter() -> tuple[Response, int]:
    data = request.get_json()
    scooter = Scooter(model=data['model'])

    if 'state' in data:
        state = data['state']
        validate_state(state)
        scooter.state = state.upper()

    db.session.add(scooter)
    db.session.commit()

    return jsonify({'id': scooter.id, 'message': 'Scooter created successfully'}), 201


@bp.route('/scooters/active', methods=['GET'])
def get_active_scooters() -> tuple[Response, int]:
    active_scooters = Scooter.query.filter_by(state=ScooterState.ACTIVE).all()
    return jsonify([scooter.to_dict() for scooter in active_scooters]), 200


@bp.route('/ping', methods=['GET'])
def ping() -> tuple[Response, int]:
    return jsonify({'message': 'pong!'}), 200
