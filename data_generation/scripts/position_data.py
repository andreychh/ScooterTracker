import logging
import time

import requests
from requests import ConnectionError, HTTPError

from data_generation.scripts.utils import BASE_URL, get_active_scooters, update_data

latitude_params = {
    'min_value': -90,
    'max_value': 90,
    'min_offset': -0.005,
    'max_offset': 0.005,
}
longitude_params = {
    'min_value': -180,
    'max_value': 180,
    'min_offset': -0.005,
    'max_offset': 0.005,
}


def update_position(scooter):
    updated_data = \
        update_data('latitude', scooter['position_data'], **latitude_params) | \
        update_data('longitude', scooter['position_data'], **longitude_params)

    response = requests.post(
        url=f'{BASE_URL}/scooters/{scooter["id"]}/position',
        headers={'Content-Type': 'application/json'},
        json=updated_data
    )

    response.raise_for_status()


def main():
    try:
        for scooter in get_active_scooters():
            update_position(scooter)

        logging.info(f'Position data updated successfully')
    except HTTPError as e:
        logging.error('HTTPError Error occurred: %s, json=%s', e, e.response.json())
    except ConnectionError as e:
        logging.error('Connection error occurred: %s', e)


def update_position_loop():
    logging.info('Starting update_position loop')
    while True:
        main()
        time.sleep(10)


if __name__ == '__main__':
    main()
