import logging
import random
import time

import requests

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s][%(levelname)s] %(message)37s',
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        logging.FileHandler("check_connect.log"),
        logging.StreamHandler()
    ]
)

hosts = [
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
        get_data = requests.get(host, timeout=3)
        if get_data.status_code != 200:
            logging.error(
                f"Не достучались до узла {host}, код {get_data.status_code}\nЗаголовки ответа: {get_data.headers}")
    except Exception as ex:
        logging.critical(f"При попытке доступа к {host} критическая ошибка: {ex}")
    else:
        logging.info(f"{host} -> {get_data.reason}")


if __name__ == "__main__":
    while True:
        check_connect(hosts[random.randrange(0, len(hosts))])
        time.sleep(2)
