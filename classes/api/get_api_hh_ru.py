import requests
import json
from classes.api.get_api import GetApi
from classes.vacancy_class.vacancy_class import Vacancy


class GetApiHhRu(GetApi):
    """Класс для работы с API сайта HeadHunter"""

    def get_data_from_the_api(self, text_search, minimal_salary):
        request = requests.get('https://api.hh.ru/vacancies?' + f"text={text_search}&salary={minimal_salary}")
        vacancies_data = json.loads(request.text)
        data_result = {'HHru': []}

        for item in vacancies_data['items']:
            data_result['HHru'].append({'vacancy_id': item['id'],
                                       'title': item['name'],
                                       'minimal_salary': 'Зарплата не указана' if item.get('salary') is None else item['salary']['from'],
                                       'vacancy_url': item["apply_alternate_url"],
                                       'loication': item["area"]["name"]})

        return data_result
