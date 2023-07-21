import requests
import json
from classes.api.get_api import GetApi
import os


class GetApiSuperJob(GetApi):
    """Класс для работы с API сайта SuperJob"""

    def get_data_from_the_api(self, text_search, minimal_salary):
        api_key: str = os.getenv('SJ_API_KEY')
        request = requests.get('https://api.superjob.ru/2.0/vacancies/?' + f'keyword={text_search}&payment_from={minimal_salary}',
                               headers={'X-Api-App-Id': api_key},)
        vacancies_data = json.loads(request.text)
        data_result = {'SuperJob': []}

        for object in vacancies_data['objects']:
            data_result['SuperJob'].append({'vacancy_id': object['id'],
                                            'title': object['profession'],
                                            'minimal_salary': 'Зарплата не указана' if object.get('payment_from') is None else object.get('payment_from'),
                                            'vacancy_url': object["link"],
                                            'location': object["address"]})

        return data_result
