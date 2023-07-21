from abc import ABC, abstractmethod
import json


class WorkingWithVacancies(ABC):
    """Класс для операций с вакансиями и файлом, в котором они хранятся"""

    @abstractmethod
    def write_data_in_json_file(self, filename):
        pass

    @abstractmethod
    def get_data_from_json_file(self, vacancy_id, field_to_get=None):
        pass

    @abstractmethod
    def append_data_in_json_file(self, appending_data):
        pass

    @abstractmethod
    def delete_data_from_json_file(self, vacancy_id):
        pass


class WorkingWithDataInJsonFile(WorkingWithVacancies):
    def __init__(self, data):
        self.data = data

    def write_data_in_json_file(self, filename):
        with open(filename, "w") as file:
            json.dump(self.data, file)

    def append_data_in_json_file(self, appending_data):
        with open(self.data, "r+") as file:
            file.seek(len(file.read()) - 1)
            print(',' + appending_data, file=file)

    def get_data_from_json_file(self, vacancy_id, field_to_get=None):
        with open(self.data, "r") as file:
            vacancy = json.load(file).get(vacancy_id)
            if field_to_get:
                return vacancy.get(field_to_get, 'Введите существующее поле') if vacancy else 'Введите существующую вакансию'
            else:
                return vacancy

    def delete_data_from_json_file(self, vacancy_id):
        vacancies = self.get_data_from_json_file()
        vacancies.pop(vacancy_id, None)

        with open(self.data, "w") as file:
            file.write(json.dumps(vacancies))

    def sort_vacancies_by_the_minimal_salary(self, dict_key):
        return sorted(self.data[dict_key], key=lambda x: int(x['minimal_salary']) if isinstance(x['minimal_salary'], int) else x is None)

    def get_top_N_vacancies(self, dict_key, number_of_vacancies):
        return sorted(self.data[dict_key], key=lambda x: int(x['minimal_salary']) if isinstance(x['minimal_salary'], int) else x is None)[-number_of_vacancies:]
