from utils.utils import (create_database,
                         create_tables,
                         insert_data_to_table)
from src.db_manager import DBManager
import json

db_name = "kp_baranova"
create_database(db_name)
create_tables(db_name)
insert_data_to_table(db_name)

while True:
    print("""
Выбери цифру для отображения данных

1. Показать список всех компаний и кол-во открытых вакансий
2. Показать инфо о вакансиях
3. Показать среднюю ЗП по вакансиям
4. Показать вакансии, у которых ЗП выше средней
5. Ввести ключевое слово для поиска
6. Выход
""")
    user_answer = input('Введи цифру: ')
    db = DBManager(db_name)
    if user_answer in ['1', '2', '3', '4', '5', '6']:
        if user_answer == '1':
            print(json.dumps(db.get_companies_and_vacancies_count(), ensure_ascii=False, indent=4))
        if user_answer == '2':
            print(json.dumps(db.get_all_vacancies(), ensure_ascii=False, indent=4))
        if user_answer == '3':
            print(db.get_avg_salary())
        if user_answer == '4':
            print(db.get_vacancies_with_higher_salary())
        if user_answer == '5':
            user_word = input('Введи слово: ')
            json_list = db.get_vacancies_with_keyword(user_word)
            if len(json_list) == 0:
                print('Таких вакансий нет')
            else:
                print(json.dumps(json_list, ensure_ascii=False, indent=4))
            print('Поиск завершен')
        if user_answer == '6':
            break
    else:
        print("Такой цифры нет, попробуй еще раз")
