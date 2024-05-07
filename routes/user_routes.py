from flask import Blueprint, request, jsonify

from database import db, Scooter
from routes.utils import get_json_error, get_field_error

bp = Blueprint('user', __name__)


@bp.route('/scooters', methods=['POST'])
def create_scooter():
    if not request.is_json:
        return get_json_error()

    data = request.get_json()

    if 'model' not in data:
        return get_field_error('model')

    db.session.add(Scooter(model=data['model']))
    db.session.commit()

    return jsonify({'message': 'Scooter created successfully'}), 201


@bp.route('/scooters/<int:scooter_id>', methods=['GET'])
def get_scooter(scooter_id):
    scooter = Scooter.query.get_or_404(scooter_id)
    return jsonify({'id': scooter.id, 'model': scooter.model})  # TODO: return last charge and locate data


@bp.route('/scooters/<int:scooter_id>', methods=['DELETE'])
def delete_scooter(scooter_id):
    db.session.delete(Scooter.query.get_or_404(scooter_id))
    db.session.commit()
    return jsonify({'message': 'Scooter deleted successfully'}), 200
