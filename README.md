Демонстрация работы сайта
---
___
В файле screencast.mkv 
и здесь
https://drive.google.com/file/d/1qX-kYVBhg8H05AQtQ-8rGmkztM4xAxME/view?usp=sharing

Инструкция по использованию
---
___

1)Клонируем репозиторий

    git clone https://github.com/Badsnus/popso_test_task.git

2)Заходим в директорию репозитория

    cd news_site

3).env.example -> .env

    И выставить там настройки
    TELEGRAM_API_HASH и TELEGRAM_API_ID надо брать тут
    https://my.telegram.org/apps

4)Создать виртуальное окружение (ну если хотите)

    python -m venv venv

    Windows: venv\Scripts\activate.bat
    Linux и MacOS: source venv/bin/activate

5)Зависимость скачать

    pip install -r requirements.txt

6)Зайти в папку parser и запустить

    cd parser
    python main.py

7)Зайти в папку сайта и запустить

    cd ../news_site
    python manage.py runserver

Немного моих мыслей
---
___

В телеге у различных фото одного поста - считаются разными сообщениями.
Поэтому там в парсере такая штука, что мы собираем все фото поста, а уже потом пулим пост.
Там конечно можно всю эту штуку так скажем немного сломать (ну мне так кажется, но я не проверял), если сможете
сломать - вы молодец :)

CRUD - не совсем понял, что там надо было сделать. Сделал так, как посчитал, что нужно.

Ну и конечно стоило бы написать тесты, но тут такой функционал, что тесты будут скорее тестировать саму джангу, чем мой
код. Так что тесты не написал(

Ссылка на тестовое
---
___
https://docs.google.com/document/d/1lghiBb1E4kpTaGXMryqItTUDqlsslkKHgZkNLArRSJM/edit?usp=sharing
