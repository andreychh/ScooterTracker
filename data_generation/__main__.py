import logging
import threading

from data_generation.scripts import update_charge_loop, update_position_loop


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)-5s - %(message)s',
        datefmt='%d-%m-%Y %H:%M:%S',
    )

    charge_thread = threading.Thread(target=update_charge_loop)
    position_thread = threading.Thread(target=update_position_loop)

    charge_thread.start()
    position_thread.start()


if __name__ == '__main__':
    main()
