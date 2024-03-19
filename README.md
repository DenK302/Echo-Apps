Для репозитория:
1. Установка

   Для установки проекта нужно распаковать архив с репозиторием, после чего установить зависимости из requirements.txt
   Сделать это можно выполнив команду pip install -r requirements.txt в терминале из каталога, куда был распакован проект

2. Запуск

   Для запуска проекта нужно выполнить команду uvicorn main:app. Проект по-умолчанию запускается на 8000 порту.

Для Docker контейнера (находится в Releases):

1. Установка

   Необходимо скачать в любое удобное место .tar архив, после чего в терминале перейти в каталог, содержащий скачанный архив.
   Затем нужно выполнить команду docker load -i *.tar, где * - название загруженного архива. Это восстановит Docker образ из файла.

2. Запуск

   Нужно выполнить команду docker run -p port:80 appname, где appname - это имя Docker образа, восстановленного из файла, port - номер порта, который будет использован для Docker образа.

   
Использование:
   Открыв в браузере ссылку http://127.0.0.1:8000 (или выбранный вами порт) можно будет загрузить файл. 
   После отправки файла будет получен ответ в виде URL-ссылки на AMAZON S3.
   Так же доступна отладка в Swagger UI, по адресу http://127.0.0.1:docs/
