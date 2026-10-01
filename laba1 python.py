import platform
import getpass
import os
import socket
import shutil
import json

usage = shutil.disk_usage("/")

data = {
    #ОС
    "os_name": platform.system(),
    "os_release": platform.release(),
    "os_version": platform.version(),
    "os_architecture": platform.machine(),

    #пользователь
    "username": getpass.getuser(),
    "home_dir": os.path.expanduser("~"),
    "current_dir": os.getcwd(),

    #процессор
    "cpu": platform.processor(),
    "cpu_cores": os.cpu_count(),

    #сеть
    "hostname": socket.gethostname(),
    "ip_address": socket.gethostbyname(socket.gethostname()),

    #диск
    "disk_total_gb": round(usage.total / (1024 ** 3), 2),
    "disk_used_gb": round(usage.used / (1024 ** 3), 2),
    "disk_free_gb": round(usage.free / (1024 ** 3), 2),
}
with open("system_info.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

for key, value in data.items():
    print(key, value)
