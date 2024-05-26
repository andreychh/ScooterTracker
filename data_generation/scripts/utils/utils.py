import random

import requests

BASE_URL = 'http://127.0.0.1:5000'


def get_active_scooters():
    response = requests.get(f'{BASE_URL}/scooters/active')
    response.raise_for_status()
    return response.json()


def update_data(key, data, min_value, max_value, min_offset, max_offset):
    if data is None:
        return {key: random.uniform(min_value, max_value)}

    value = data.get(key)

    if min_value <= value <= max_value:
        value -= random.uniform(min_offset, max_offset)
    else:
        value = random.uniform(min_value, max_value)

    return {key: value}
