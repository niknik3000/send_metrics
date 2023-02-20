import logging
import random
import requests
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s][%(levelname)s] %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
            logging.FileHandler("check_connect.log"),
            logging.StreamHandler()
        ]
)

hub = [
    "https://download.docker.com",
    "https://dl.google.com",
    "http://ru.archive.ubuntu.com",
    "https://repo.mongodb.org",
    "https://packages.microsoft.com",
    "https://losst.pro",
    "https://www.youtube.com",
    "https://ubuntu.com"
]


def check_connect(host):
    try:
        get_data = requests.get(host, timeout=5)
        if get_data.status_code != 200:
            logging.error(f"Не достучались до узла {host}, код {get_data.status_code}")
    except Exception as ex:
        logging.critical(f"При попытке доступа к {host} критическая ошибка: {ex}")


if __name__ == "__main__":
    while True:
        check_connect(hub[random.randrange(0, len(hub))])
        time.sleep(2)
