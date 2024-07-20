import pytest
from src.db_manager import DBManager
from utils.utils import create_database, create_tables
import os
import psycopg2

test_db = 'test_bd'
create_database(test_db)
create_tables(test_db)


def insert_tables(name_db):
    conn = psycopg2.connect(dbname=test_db,
                            user=os.getenv("user"),
                            password=os.getenv("password"),
                            host=os.getenv("host"),
                            port=os.getenv("port"))
    with conn:
        with conn.cursor() as cur:
            cur.execute("""INSERT INTO employers VALUES 
                            (123, 'Магнит'), (234, 'Пятерочка'), (345, 'Перекресток')
                            """
                        )
            cur.execute("""INSERT INTO vacancies VALUES 
                            (1, 'Кассир', 'http://1', 10_000, 20_000, 'Москва', 123),
                            (2, 'Мясник', 'http://2', 10_500, 20_500, 'Москва', 123),
                            (3, 'Охранник', 'http://3', 5_000, 7_000, 'Торжок', 123),
                            (11, 'Кассир', 'http://12', 20_000, 30_000, 'Тверь', 234),
                            (22, 'Консультант', 'http://13', 0, 30_000, 'Москва', 234),
                            (33, 'Кладовщик', 'http://14', 0, 8_000, 'Москва', 234),
                            (111, 'Консультант', 'http://112', 0, 30_000, 'Казань', 345),
                            (222, 'Кладовщик', 'http://113', 0, 0, 'Москва', 345),
                            (333, 'Кассир', 'http://114', 1_000, 50_000, 'Тверь', 345)
                            """
                        )

    conn.close()


insert_tables(test_db)

db = DBManager(test_db)


def query(query):
    conn = psycopg2.connect(dbname=test_db,
                            user=os.getenv("user"),
                            password=os.getenv("password"),
                            host=os.getenv("host"),
                            port=os.getenv("port"))
    with conn:
        with conn.cursor() as cur:
            cur.execute(query)
            result = cur.fetchall()
    conn.close()
    return result


def test_get_companies_and_vacancies_count():
    assert db.get_companies_and_vacancies_count() == [('Магнит', 3), ('Перекресток', 3), ('Пятерочка', 3)]
