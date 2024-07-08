# KP_5_Baranova

## Программа реализует задачу по получению информации о работодателях и вакансиях с платформы hh.ru в России и проектированию таблиц в БД PosgreSQL

___
Чтобы начать работу, нужно:
- Создать файл .env с указанием инфо для подключения к вашей локальной БД (**dbname, password, host, port**).
- Установить библиотеки, pip install :
- [x] psycopg2
- [x] requests
- [x] python-dotenv


- Запустить интерактивное меню для работы с пользователем, где нужно выбрать цифру:
1. Показать список всех компаний и кол-во открытых вакансий
2. Показать инфо о вакансиях
3. Показать среднюю ЗП по вакансиям
4. Показать вакансии, у которых ЗП выше средней
5. Ввести ключевое слово для поиска
6. Выход

___
Для работы с данным проектом *необходимо наличие*:

+ Python==3.12 и выше

А также *дополнительная установка*:

+ certifi==2024.7.4
  + charset-normalizer==3.3.2
+ idna==3.7
+ psycopg2==2.9.9
+ pydotenv==0.0.7
+ python-dotenv==1.0.1
+ requests==2.32.3
+ urllib3==2.2.2

___
Программа содержит в себе 3 пакета - src, utils с модулями api.py, main.py, db_manager.py, utils.py

Файл db_manager.py содержит в себе класс для поключения к БД и формированию, получению запросов
данных.\
Файл api.py содержит в себе класс, который подключается к API и получает инфо о работодателях и вакансиях.\
Файл utils.py содержит в себе класс по созданию новой БД с помощью подключения к существующей БД postgres. Дополнительно нужно создать файл с указанием инфо для подключения к вашей локальной БД (**dbname, password, host, port**).\
Файл main.py вызывает написанные функции для формирования БД, таблиц и их заполнения, а также функционал для работы с user'ом.

___
Проект имеет удаленный репозиторий с описанием коммитов, 2 ветки - develop and main.\
Разрабокта ведется в ветке develop и сливается с веткой main.