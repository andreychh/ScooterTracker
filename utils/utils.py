from functools import wraps

from flask import jsonify, Response, request, abort

from database import ChargeData, PositionData, ScooterState


# Error Handling
def get_json_error() -> tuple[Response, int]:
    return jsonify({'error': 'Request must be in JSON format'}), 400


def get_field_error(field_name: str) -> tuple[Response, int]:
    return jsonify({'error': f'Field {field_name} is required'}), 400


# Validation
def validate_limit(limit: int):
    if not (limit is None or (isinstance(limit, int) and limit > 0)):
        abort(400, description='Field limit must be a positive integer')


def validate_charge_data(charge_data: list[ChargeData]):
    if not charge_data:
        abort(404, description='Charge data not found')


def validate_position_data(position_data: list[PositionData]):
    if not position_data:
        abort(404, description='Position data not found')


def validate_state(state):
    if state not in ScooterState:
        abort(400, description='Invalid state. Acceptable values: Active, Inactive')


def validate_model(model):  # TODO: write this
    ...
    # abort(400, description='Invalid model')


# Check
def check_json_fields(*fields: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not request.json:
                get_json_error()

            data = request.get_json()
            for field in fields:
                if field not in data:
                    get_field_error(field)

            return func(*args, **kwargs)

        return wrapper

    return decorator
