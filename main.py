from utils.utils import (create_database,
                         create_tables,
                         insert_data_to_table)
from src.db_manager import DBManager
from tabulate import tabulate

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
5. Ввести ключевое слово для поиска и отобразить вакансии
6. Выход
""")
    user_answer = input('Введи цифру: ')
    db = DBManager(db_name)
    if user_answer in ['1', '2', '3', '4', '5', '6']:
        if user_answer == '1':
            print(tabulate(db.get_companies_and_vacancies_count(), headers=['Company_name', 'Count']))
        if user_answer == '2':
            print(tabulate(db.get_all_vacancies(),
                           headers=['Company_name', 'Vacancy_name', 'Url', 'Salary_from', 'Salary_to']))
        if user_answer == '3':
            print(tabulate(db.get_general_avg_salary(), headers=['Avg_min', 'Avg_max']))
        if user_answer == '4':
            print(tabulate(db.get_vacancies_with_higher_salary(), headers=['Vacancy_name', 'Salary']))
        if user_answer == '5':
            user_word = input('Введи слово: ').lower()
            json_list = db.get_vacancies_with_keyword(user_word)
            if len(json_list) == 0:
                print('Таких вакансий нет')
            else:
                print(tabulate(db.get_vacancies_with_keyword(user_word),
                               headers=['Company_name', 'Vacancy_name', 'Url', 'Salary_from', 'Salary_to']))

        print('Поиск завершен')
        if user_answer == '6':
            break
    else:
        print("Такой цифры нет, попробуй еще раз")
