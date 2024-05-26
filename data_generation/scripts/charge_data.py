import logging
import time

import requests
from requests import ConnectionError, HTTPError

from data_generation.scripts.utils import BASE_URL, get_active_scooters, update_data

charge_params = {
    'min_value': 0.1,
    'max_value': 1.0,
    'min_offset': 0.05,
    'max_offset': 0.1,
}


def update_charge(scooter):
    updated_data = update_data('charge', scooter['charge_data'], **charge_params)

    response = requests.post(
        url=f'{BASE_URL}/scooters/{scooter["id"]}/charge',
        headers={'Content-Type': 'application/json'},
        json=updated_data,
    )

    response.raise_for_status()


def main():
    try:
        for scooter in get_active_scooters():
            update_charge(scooter)

        logging.info(f'Charge data updated successfully')
    except HTTPError as e:
        logging.error('HTTPError Error occurred: %s, json=%s', e, e.response.json())
    except ConnectionError as e:
        logging.error('Connection error occurred: %s', e)


def update_charge_loop():
    logging.info('Starting update_charge loop')
    while True:
        main()
        time.sleep(5)


if __name__ == '__main__':
    main()
