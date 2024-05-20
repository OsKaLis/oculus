import os
from time import sleep

from utils import (
    defining_operating_system, when_send_time, current_cwordints,
    create_file, recording_auto_upload_windows, recording_auto_upload_linux,
    checking_the_internet,
)
from working_with_face import WorkFace
from bot import bot_lik
from configurations import (
     PICTURE_NAME, SENDING_TEXT, CMD_LAUNCH_OCULUS, CURRENT_DIRECTORY,
     DOWNTIME, ANIME_FECE, HOST_MODEL,
)


def main() -> None:
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
    # Заполняем время включения
    SENDING_TEXT['data_time'] = when_send_time()
    # Получаем кординаты пк
    SENDING_TEXT['the_сardinals'] = current_cwordints()
    wf = WorkFace()
    # Проверка на наличие модели
    if not os.path.exists(HOST_MODEL):
        wf.creating_face_host()
        wf.creating_host_model()
    host_recognized, probability_host = wf.definitions_host()
    if host_recognized:
        # Хозяин
        SENDING_TEXT['host'] = 'Добро пожаловать хозяин!!!'
        picture = ANIME_FECE['smile']
    else:
        # Правонарушитель
        SENDING_TEXT['host'] = 'Постороний позле Ноутбука ???'
        picture = PICTURE_NAME
    bot_lik(SENDING_TEXT, picture)


if __name__ == '__main__':
    main()
