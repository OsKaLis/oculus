import os
from time import sleep

from utils import (
    defining_operating_system, take_picture_from_camera,
    when_send_time, current_cwordints, create_file,
    recording_auto_upload_windows, recording_auto_upload_linux,
    checking_the_internet,
)
from bot import bot_lik
from configurations import (
     PICTURE_NAME, SENDING_TEXT, CMD_LAUNCH_OCULUS, CURRENT_DIRECTORY,
     DOWNTIME,
)

# Стоит добавить логи ?


def main():
    """Основа програмы."""
    if defining_operating_system() == 'windows':
        # Проверка записи в реестре
        if not os.path.exists(CURRENT_DIRECTORY + '\\' + CMD_LAUNCH_OCULUS):
            create_file()
        recording_auto_upload_windows()
    else:
        recording_auto_upload_linux()
    # Проверка на доступ в интернет
    while True:
        if checking_the_internet():
            break
        else:
            sleep(DOWNTIME)
    # Проверка есть в кадре не хозяин отправляем правонарушителя
    # Если это первый запуск тогда нужно сделать снимок хозяина
    # Заполняем время включения
    SENDING_TEXT['data_time'] = when_send_time()
    # Получаем кординаты пк
    SENDING_TEXT['the_сardinals'] = current_cwordints()
    # Делаем снимок предпологаемого правонарушителя
    take_picture_from_camera()
    # Отправляем параметры хозяину
    bot_lik(SENDING_TEXT, PICTURE_NAME)


if __name__ == '__main__':
    main()
