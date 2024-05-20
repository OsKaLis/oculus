<div id="header" align="center">
  <h1>Проект Oculus</h1>
</div>

## Что это за проект, какую задачу он решает, в чём его польза:
> [!NOTE]
> Отправляет владельцу Фото кто зашол в его пк
> запускает это в тихом режиме чтоб было незаметно.

## Как развернуть проект на локальной машине.
> [!IMPORTANT]
> * 1 (Клонируем проект) :git clone git@github.com:OsKaLis/oculus.git
> * 2 (Переходим в директорию проекта) :cd oculus/
> * 3 (Создание файла с настройками ".env"):
>   ```
>   API_ID=[Ид чата для ответа]
>   API_HASH=[]
>   BOT_TOKEN=[Токен бота]
>   KONTAKT=[индификатор клиента]
> * 4 (Устанавливаем виртуальное окружение) :python -m venv venv 
> * 5 (Запускаем виртуальное окружение из папки "oculus") :source venv/Scripts/activate
> * 6 (Установка всех нужных библиотек) :pip install -r requirements.txt
> * 7 (Запускаем) :python oculus.py

## Cтек технологий:
<img src="https://img.shields.io/badge/Python_-3.9.10-Green"> <img src="https://img.shields.io/badge/pyrogram_-2.0.106-blue"> <img src="https://img.shields.io/badge/OpenCV_-4.8.1.78-red">
<img src="https://img.shields.io/badge/python_dotenv_-1.0.1-aqua"> <img src="https://img.shields.io/badge/PySocks_-1.7.1-white">

## Планы по доработке:
* [1] - Добавить кординаты нахождения пк
* [2] - Реализовать такуюже работу в линукс
* [3] - добавить функционал пратять важные папки если зашол не хозяин

## Автор: Юшко Ю.Ю.
