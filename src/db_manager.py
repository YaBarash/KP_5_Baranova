import psycopg2
import os


class DBManager:
    '''
    Класс для подключения к БД
    '''

    def __init__(self, name):
        self.__name = name

    def __execute_query(self, query):
        '''приватный метод для подключения к БД и формирования запросов'''
        conn = psycopg2.connect(dbname=self.__name,
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

    def get_companies_and_vacancies_count(self):
        '''получает список всех компаний и количество вакансий у каждой компании'''
        return self.__execute_query("""
        SELECT employers.name, COUNT(*) AS count_vacancies
        FROM employers
        LEFT JOIN vacancies ON vacancies.employer=employers.id
        GROUP BY employers.name
        """)

    def get_all_vacancies(self):
        '''получает список всех вакансий с указанием названия компании, названия вакансии,зп и ссылки на вакансию'''
        return self.__execute_query("""
        SELECT employers.name AS company_name, vacancies.name AS vac_name,
        vacancies.url, vacancies.salary_from, vacancies.salary_to
        FROM employers
        LEFT JOIN vacancies ON vacancies.employer=employers.id
        """)

    def get_avg_salary(self):
        '''получает среднюю зарплату по вакансии'''
        return self.__execute_query("""
        SELECT employer, name, round(avg(salary_from),2) AS salary_avg
        FROM vacancies
        GROUP BY name, employer
        ORDER BY round(avg(salary_from),2) DESC, name
        """)

    def get_vacancies_with_higher_salary(self):
        '''получает список всех вакансий, у которых зарплата выше средней по всем вакансиям'''
        return self.__execute_query("""
        SELECT name, round(salary_from,2) AS salary_round
        FROM vacancies
        WHERE  salary_from >= (select round(avg(salary_from),2) AS salary_from from vacancies)
        ORDER BY round(salary_from,2) DESC
        """)

    def get_vacancies_with_keyword(self, keyword):
        '''получает список всех вакансий, в названии которых содержатся переданные в метод слова'''
        new_list_vacancies = []
        vacancies = self.__execute_query("""
        SELECT employers.name AS company_name, vacancies.name AS vac_name,
        vacancies.url, vacancies.salary_from, vacancies.salary_to
        FROM employers
        LEFT JOIN vacancies ON vacancies.employer=employers.id
        """)
        for vac in vacancies:
            if keyword.lower() in vac[1].lower():
                new_list_vacancies.append(vac)
        return new_list_vacancies
