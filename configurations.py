import os
import getpass
from dotenv import dotenv_values

config = dotenv_values(".env")

OS = {
    'win32': 'windows',
    'linux': 'linux',
    'darwin': 'OSX'
}
# Дополнительные данные которые отправляются боту
SENDING_TEXT = {
    'data_time': None,
    'the_сardinals': None,
    'host': None,
}
USER_NAME = getpass.getuser()  # Имя хозяина
PICTURE_NAME = 'temp.png'  # Профиль человека который включает пк
CMD_LAUNCH_OCULUS = 'oculus.cmd'
CURRENT_DIRECTORY = os.getcwd()  # Директория где лежит програма
FACE_USER = CURRENT_DIRECTORY + '\\face_user\\'  # Куда сохраняю картинки юзера
HOST_MODEL = f'{USER_NAME}.yml'  # Модель хозяина
DOWNTIME = 30  # Время простоя для задач
VIEWING_TIME = 60  # Время для определения кто квлючил пк
NUMBER_FACE_IMAGES = 50  # Количество картинок для создание модли нейронки
PERCENTAGE_TRUST = 50  # Процент доверия когда больше тогда доверияет
# Параметры для отправки сообщения для БОТА
api_id = int(config['API_ID'])
api_hash = config['API_HASH']
bot_token = config['BOT_TOKEN']
kontakt = int(config['KONTAKT'])

AUTO_LAUNCH_FILE = ("@echo off \n"
                    f"cd /d {CURRENT_DIRECTORY}\\venv\\Scripts \n"
                    "call activate \n"
                    f"cd /d {CURRENT_DIRECTORY} \n"
                    "start /min pyw oculus.py"
                    )
# картинки имоции бота
ANIME_FECE = {
    'smile': 'face_anime\\smile.png',
}
