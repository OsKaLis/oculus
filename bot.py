from pyrogram import Client

from configurations import (
    api_id, api_hash, bot_token, kontakt,
)


app = Client(
    "Oculus",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


def bot_lik(parameters: list, filename: str):
    """Отправка на бот сообщение фото."""
    app.start()
    app.send_photo(kontakt, filename)
    for key, value in parameters.items():
        app.send_message(kontakt, value)
    app.stop()
