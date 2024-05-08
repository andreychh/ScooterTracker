from flask import jsonify


def get_json_error():
    return jsonify({'error': 'Request must be in JSON format'}), 400


def get_field_error(field_name: str):
    return jsonify({'error': f'Field "{field_name}" is required'}), 400
