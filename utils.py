from datetime import datetime as dt
from sys import platform

import cv2

from configurations import (
    OS,
    PICTURE_NAME,
)


def defining_operating_system():
    """Определяе операционую систему."""
    if platform in OS:
        return OS[platform]
    return '<??? OS ???>'


def when_send_time():
    """Когда отправил картинку."""
    return f'Время отправки: {dt.now().strftime("%Y-%m-%d-%H.%M")}'


def current_cwordints():
    """Узнать текущии кординаты."""
    return 'Ш: 40, Д: 40'


def take_picture_from_camera():
    """Делает снимок с камеры ноутбука."""
    camera = cv2.VideoCapture(0)
    for i in range(30):
        camera.read()
    ret, frame = camera.read()
    camera.release()
    cv2.imwrite(PICTURE_NAME, frame)


def recording_auto_upload_windows():
    """."""
    pass


def recording_auto_upload_linux():
    """."""
    pass
