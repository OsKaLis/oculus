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

PICTURE_NAME = 'temp.png'


api_id = int(config['API_ID'])
api_hash = config['API_HASH']
bot_token = config['BOT_TOKEN']
kontakt = int(config['KONTAKT'])
