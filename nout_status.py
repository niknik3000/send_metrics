import time
import logging
import psutil
import common
import platform

logging.basicConfig(level=logging.INFO, format='[%(asctime)s][%(levelname)s] %(message)s', datefmt='%d-%b-%y %H:%M:%S')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
seconds2check = 600

def get_mem(send_data):
    mem = psutil.virtual_memory()
    if int(round(mem.percent)) > 70:
        send_data +=("WARNING, LOW FREE MEMORY")
        send_data += f"Total: {mem.total / 1024 /1024 } Mb\n"
        send_data += f"Free: {mem.free / 1024 /1024 } Mb\n"
        send_data += f"Available: {mem.available  / 1024 /1024} Mb\n"
        send_data += f"Used persentage: {mem.percent}\n"
        send_data += "\n####################\n"
    return send_data


def get_cpu(send_data):
    loadavg_data = tuple()
    loadavg_data = psutil.getloadavg()
    max_value = 3
    for f in loadavg_data:
        if f > float(max_value):
            send_data += f"WARNING, LA > {max_value}\n"
            send_data += f"LA: {loadavg_data}\n"
            send_data += "\n####################\n"
            break
    return send_data


def get_battery(send_data):
    battery = psutil.sensors_battery()
    if battery and not battery.power_plugged and int(round(battery.percent)) <= 20:
        send_data += "WARNING, BATTERY DISCHARGING\n"
        send_data += f"Батарея заряжается: {battery.power_plugged}\nПроцент заряда: {round(battery.percent)}\nЗаряда осталось на {round(battery.secsleft / 60)} минут"
        send_data += "\n####################\n"
    return send_data

def get_partition_usage(send_data, entrypoint):
    home_usage = psutil.disk_usage(entrypoint)
    perc_used = round(100 - home_usage.percent, 2)
    if (perc_used) < float(10):
        send_data += f"WARNING, LOW FREE SPACE in '{entrypoint}'\nОсталось места {perc_used}% ({round(home_usage.free / 1024 / 1042 / 1024, 2)} Гб)"
        send_data += "\n####################\n"
    return send_data

while True:
    _name = f"===> {platform.node()}  <===\n"
    send_data = _name
    send_data = get_partition_usage(send_data, "/")
    send_data = get_partition_usage(send_data, "/home/")
    send_data = get_cpu(send_data)
    send_data = get_mem(send_data)
    send_data = get_battery(send_data)
    if send_data != _name:
        common.send_statistics(send_data)
        logging.info(send_data)
    else:
        logging.info("Нечего отправлять")
    time.sleep(seconds2check)

