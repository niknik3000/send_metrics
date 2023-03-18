import logging
import random
import time

import requests

def set_logging():
    """Задаем логгирование"""
    logger_main = logging.getLogger()
    logger_main.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
    # В файл пишем только ошибки
    file_handler = logging.FileHandler(filename='check_connect.log',
                                       mode='w',
                                       encoding='utf-8')
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(formatter)
    # В консоль пишем DEBUG
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger_main.addHandler(console_handler)
    logger_main.addHandler(file_handler)


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
        logging.info(f"[{get_data.reason}] -> {host}")


if __name__ == "__main__":
    set_logging()
    while True:
        check_connect(hosts[random.randrange(0, len(hosts))])
        time.sleep(2)
