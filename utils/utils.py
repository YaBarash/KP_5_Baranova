import psycopg2
import dotenv
import os
from src.api import HHApi

dotenv.load_dotenv()


def create_database(db_name) -> None:
    '''
    Функция создает новую  БД с названием db_name, основываясь на подключении к postgres
    :param db_name: название БД
    :return:None
    '''
    conn = psycopg2.connect(dbname='postgres',
                            user=os.getenv("user"),
                            password=os.getenv("password"),
                            host=os.getenv("host"),
                            port=os.getenv("port"))
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
    cur.execute(f"CREATE DATABASE {db_name}")

    cur.close()
    conn.close()


def create_tables(db_name) -> None:
    '''
    Создаем таблицы с вакансиями и работодателями в БД
    :param db_name: Название БД
    :return: None
    '''
    conn = psycopg2.connect(dbname=db_name,
                            user=os.getenv("user"),
                            password=os.getenv("password"),
                            host=os.getenv("host"),
                            port=os.getenv("port"))
    with conn:
        with conn.cursor() as cur:
            cur.execute("""CREATE TABLE employers (
            id INTEGER PRIMARY KEY,
            name VARCHAR(100) UNIQUE NOT NULL
            )
            """)

            cur.execute("""CREATE TABLE vacancies (
                        id INTEGER PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        url VARCHAR(100) NOT NULL,
                        salary_from INTEGER,
                        salary_to INTEGER,
                        area VARCHAR(100) NOT NULL,
                        employer INTEGER REFERENCES employers(id)
                        )
                        """)
    conn.close()


def insert_data_to_table(db_name) -> None:
    '''
    Запись данных в таблицы
    :param db_name: Название БД
    :return: None
    '''
    hh = HHApi()
    employers = hh.get_employers()
    vacancies = hh.get_all_vacancies()
    conn = psycopg2.connect(dbname=db_name,
                            user=os.getenv("user"),
                            password=os.getenv("password"),
                            host=os.getenv("host"),
                            port=os.getenv("port"))
    with conn:
        with conn.cursor() as cur:
            for emp in employers:
                cur.execute("""INSERT INTO employers VALUES (%s, %s)""",
                            (emp["id"], emp["name"]))
            for vac in vacancies:
                cur.execute("""INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                            (vac["id"],
                             vac["name"],
                             vac["url"],
                             vac["salary_from"],
                             vac["salary_to"],
                             vac["area"],
                             vac["employer"]))
    conn.close()
