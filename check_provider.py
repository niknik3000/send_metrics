import logging
import random
import time

import requests

logging.basicConfig(
    level=logging.WARNING,
    format='[%(asctime)s][%(levelname)s] %(message)45s',
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
        get_data = requests.get(host)
        if get_data.status_code != 200:
            logging.error(
                f"Не достучались до узла {host}, код {get_data.status_code}\nЗаголовки ответа: {get_data.headers}")
    except requests.ReadTimeout:
        logging.warning(f"Превышен таймаут ожидания чтения с {host}")
        pass
    except requests.ConnectTimeout:
        logging.warning(f"Превышен таймаут ожидания подключения к {host}")
        pass
    except requests.ConnectionError as ex:
        logging.error(f"[ConnectionError] Ошибка при попытке доступа к {host}: {ex}")
    except requests.HTTPError as http_err:
        logging.error(f"[HTTPError] Ошибка при попытке доступа к {host}: {http_err}")
    except Exception as e:
        logging.critical(f"Необрабатаное исключение!!! {e}")
    else:
        logging.info(f"{host} -> {get_data.reason}")


if __name__ == "__main__":
    while True:
        check_connect(hosts[random.randrange(0, len(hosts))])
        time.sleep(2)
