import requests


class HHApi:
    '''
    Класс для работы с ххру для получения вакансий по работодателю
    '''
    def __get_request(self):
        """
        Получение вакансий с ххру
        Кол-во 10, сортировка по кол-ву открытых вакансий
        :return:Список вакансий
        """
        params = {
            "per_page": 10,
            "sort_by": "by_vacancies_open"
        }

        response = requests.get("https://api.hh.ru/employers", params=params)

        if response.status_code == 200:
            return response.json()["items"]

    def get_employers(self):
        """
        Фильтрация и получение списка работодателей с данными названия и id
        :return:Список
        """
        employers = []
        data = self.__get_request()
        for emp in data:
            employers.append({"id": emp["id"],
                              "name": emp["name"],
                              })
        return employers

    def __get_vacancies_employer(self, id):
        """
        Получение списка вакансиий одной компании по ее id
        :param id: айди компании
        :return:Список
        """
        params = {"employer_id": id}
        response = requests.get("https://api.hh.ru/vacancies", params=params)
        if response.status_code == 200:
            return response.json()["items"]

    def get_all_vacancies(self):
        '''
        Получение списка всех вакансий компании
        :return: Список
        '''
        employers = self.get_employers()
        all_vacancies = []
        for emp in employers:
            vacancies = self.__get_vacancies_employer(emp["id"])
            for vac in vacancies:
                if vac["salary"] is None:
                    salary_from = 0
                    salary_to = 0
                else:
                    salary_from = vac["salary"]["from"] if vac["salary"]["from"] else 0
                    salary_to = vac["salary"]["to"] if vac["salary"]["to"] else 0
                all_vacancies.append({
                    "id": vac["id"],
                    "name": vac["name"],
                    "url": vac["url"],
                    "salary_from": salary_from,
                    "salary_to": salary_to,
                    "employer": emp["id"],
                    "area": vac["area"]["name"]
                })
        return all_vacancies
