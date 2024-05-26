from functools import wraps

from flask import jsonify, Response, request, abort

from app.database import ChargeData, PositionData, ScooterState


# Error Handling
def json_error() -> tuple[Response, int]:
    return jsonify({'error': 'Request must be in JSON format.'}), 400


def field_error(field_name: str) -> tuple[Response, int]:
    return jsonify({'error': f'Field {field_name} is required.'}), 400


# Validation
def validate_limit(limit: int):
    if not (limit is None or (isinstance(limit, int) and limit > 0)):
        abort(400, description='Invalid limit. The limit parameter must be a positive integer.')


def validate_state(state):
    if state not in ScooterState:
        abort(400, description='Invalid state. The state parameter must be either "Active" or "Inactive".')


def validate_model(model):
    if not model or not isinstance(model, str):
        abort(400, description='Invalid model. The model parameter must be a non-empty string.')


def validate_charge(charge):
    if not isinstance(charge, (int, float)) or charge < 0 or charge > 1:
        abort(400, description='Invalid charge. The charge parameter must be a float in range [0.0, 1.0].')


def validate_latitude(latitude):
    if not isinstance(latitude, (int, float)) or latitude < -90 or latitude > 90:
        abort(400, description='Invalid latitude. The latitude parameter must be a float in range [-90.0, 90.0].')


def validate_longitude(longitude):
    if not isinstance(longitude, (int, float)) or longitude < -180 or longitude > 180:
        abort(400, description='Invalid longitude. The longitude parameter must be a float in range [-180.0, 180.0].')


def validate_charge_data(charge_data: list[ChargeData]):
    if not charge_data:
        abort(404, description='Charge data not found.')


def validate_position_data(position_data: list[PositionData]):
    if not position_data:
        abort(404, description='Position data not found.')


# Check
def check_json_fields(*fields: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not request.is_json:
                return json_error()

            data = request.get_json()

            for field in fields:
                if field not in data:
                    return field_error(field)

            return func(*args, **kwargs)

        return wrapper

    return decorator
