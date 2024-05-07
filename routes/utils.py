from flask import jsonify


def get_json_error():
    return jsonify({'error': 'Request must be in JSON format'}), 400


def get_field_error(field_name: str):
    return jsonify({'error': f'Field "{field_name}" is required'}), 400


def format_charge_data(charge_data):
    return [{'datetime': data.datetime, 'charge': data.charge} for data in charge_data]


def format_location_data(charge_data):
    return [{'datetime': data.datetime, 'latitude': data.latitude, 'longitude': data.longitude} for data in charge_data]
