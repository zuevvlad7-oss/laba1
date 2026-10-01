import platform
import os
import getpass
def os_name():
    system=platform.system()
    if system=="Windows":
        return "Windows"
    elif system =="Linux":
        return "Linux"
    elif system =="Darwin":
        return "macOS"
    else:
        return "Неизвестная ОС"
print(os_name())

    import platform
import getpass
import os
import socket
import shutil
import json
import datetime

# создаём пустой словарь
data = {}

# --- ОС ---
data["os_name"] = platform.system()
data["os_release"] = platform.release()
data["os_version"] = platform.version()
data["os_architecture"] = platform.machine()

# --- пользователь ---
data["username"] = getpass.getuser()
data["home_dir"] = os.path.expanduser("~")
data["current_dir"] = os.getcwd()

# --- процессор ---
data["cpu"] = platform.processor()
data["cpu_cores"] = os.cpu_count()

# --- сеть ---
data["hostname"] = socket.gethostname()
data["ip_address"] = socket.gethostbyname(socket.gethostname())

# --- диск ---
usage = shutil.disk_usage("/")
data["disk_total_gb"] = round(usage.total / (1024 ** 3), 2)
data["disk_used_gb"] = round(usage.used / (1024 ** 3), 2)
data["disk_free_gb"] = round(usage.free / (1024 ** 3), 2)

# --- когда собрали ---
data["collected_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# --- сохраняем в файл ---
with open("system_info.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Готово! Данные сохранены в system_info.json")
print(data)
