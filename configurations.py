import os
import getpass
from dotenv import dotenv_values

config = dotenv_values(".env")

OS = {
    'win32': 'windows',
    'linux': 'linux',
    'darwin': 'OSX'
}
SENDING_TEXT = {
    'data_time': None,
    'the_сardinals': None,
}
USER_NAME = getpass.getuser()  # Имя хозяина
PICTURE_NAME = 'temp.png'
CMD_LAUNCH_OCULUS = 'oculus.cmd'
CURRENT_DIRECTORY = os.getcwd()  # Директория где лежит програма
DOWNTIME = 30  # Время простоя для задач
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
