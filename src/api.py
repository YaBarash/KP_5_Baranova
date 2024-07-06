import requests


class BaseApi():
    def get_request(self):
        pass


class HHApi(BaseApi):
    def get_request(self):
        params = {
            'per_page': 10,
            'sort_by': 'by_vacancies_open'
        }

        response = requests.get('https://api.hh.ru/employers', params=params)

        if response.status_code == 200:
            return response.json()['items']
