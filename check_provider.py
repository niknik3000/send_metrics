import logging
import random
import requests
import time

logging.basicConfig(level=logging.INFO, format='[%(asctime)s][%(levelname)s] %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    filename="check_connect.log")
console = logging.StreamHandler()
console.setLevel(logging.INFO)

hub = [
    "https://download.docker.com",
    "https://dl.google.com",
    "https://ya.ru",
    "http://ru.archive.ubuntu.com",
    "https://repo.mongodb.org",
    "https://packages.microsoft.com"
]


def check_connect(host):
    try:
        get_data = requests.get(host, timeout=5)
        if get_data.status_code != 200:
            logging.error(f"Не достучались до узла {host}")
    except Exception as ex:
        logging.critical(f"При попытке достучаться до узла {host} критическая ошибка: {ex}")
    else:
        logging.info(f"Опрос узла {host} завершился со статусом {get_data.status_code}")


if __name__ == "__main__":
    while True:
        check_connect(hub[random.randrange(0, len(hub) - 1)])
        time.sleep(2)
