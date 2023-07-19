import requests
import json
from classes.api.get_api import GetApi
from classes.vacancy_class.vacancy_class import Vacancy


class GetApiSuperJob(GetApi):
    """Класс для работы с API сайта SuperJob"""

    def get_data_from_the_api(self, text_search, minimal_salary):
        request = requests.get('https://api.superjob.ru/2.0/vacancies/?' + f'keyword={text_search}&payment_from={minimal_salary}',
                               headers={'X-Api-App-Id': 'v3.r.137673910.3694aa6ead6555a9d5a5884f6d1914c71174863f.302d08dbd335336b5da27589ccb62494c3985942'},)
        vacancies_data = json.loads(request.text)
        data_result = {'SuperJob': []}

        for object in vacancies_data['objects']:
            data_result['SuperJob'].append(Vacancy(object['id'],
                                                   object['profession'],
                                                   'Зарплата не указана' if object.get('payment_from') is None else object.get('payment_from'),
                                                   object["link"],
                                                   object["address"]).__dict__)

        return data_result
