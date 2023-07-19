from abc import ABC, abstractmethod


class GetApi(ABC):
    """Абстрактный класс для API"""

    def __init__(self):
        pass

    @abstractmethod
    def get_data_from_the_api(self, text_search, minimal_salary):
        pass
