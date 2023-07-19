from classes.api.get_api_hh_ru import GetApiHhRu
from classes.api.get_api_super_job import GetApiSuperJob
from classes.work_with_data_in_file.class_for_operation_with_vacancies import WorkingWithDataInJsonFile


# Создание экземпляра класса для работы с API сайтов с вакансиями
HH_api = GetApiHhRu()
Super_job_api = GetApiSuperJob()

# Получение вакансий с разных платформ
hh_vacancies = HH_api
superjob_vacancies = Super_job_api
platforms = {'1': hh_vacancies, '2': superjob_vacancies}


# Функция для взаимодействия с пользователем
def user_interaction():
    """Функция для интерактивного взаимодействия с пользователем"""

    while True:
        platform = input('Выбери платформу, с которой хочешь получить вакансии: 1-HeadHunter, 2-SuperJob. ')
        if platform in ['1', '2']:
            break
        else:
            print('Некорректный ввод')

    while True:
        search_query = input("Введите поисковый запрос в формате 'Ключевое слово для поиска, зарплата': ").split(', ')

        if str.isdigit(search_query[-1]):
            break
        else:
            print('Некорректный ввод')

    print()
    vacancies = platforms[platform].get_data_from_the_api(search_query[0], int(search_query[1]))
    print('Список вакансий по запросу')
    print(vacancies, end='\n\n')

    json_saver = WorkingWithDataInJsonFile(vacancies)
    json_saver.write_data_in_json_file('vacancies.json')

    print('Вакансии, отсортированные по зарплате')
    key = "HHru" if platform == '1' else "SuperJob"
    print(json_saver.sort_vacancies_by_the_minimal_salary(key), end='\n\n')

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    print(json_saver.get_top_N_vacancies(key, top_n), end='\n\n')


if __name__ == "__main__":
    user_interaction()
