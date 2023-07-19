class Vacancy:
    """Класс, представляющий вакансию работы с вакансиями"""

    def __init__(self, __vacancy_id, __vacancy_name, __salary_minimal, __vacancy_url, __location):
        self.__vacancy_id = __vacancy_id
        self.__vacancy_name = __vacancy_name
        self.__salary_minimal = __salary_minimal
        self.__vacancy_url = __vacancy_url
        self.__location = __location

    @property
    def vacancy_id(self):
        return self.__vacancy_id

    @property
    def vacancy_name(self):
        return self.__vacancy_name

    @property
    def salary_minimal(self):
        return self.__salary_minimal

    @property
    def vacancy_url(self):
        return self.__vacancy_url

    @property
    def location(self):
        return self.__location

    def __repr__(self):
        return f'Vacancy({self.vacancy_id}, {self.vacancy_name}, {self.salary_minimal}, {self.vacancy_url}, {self.location})'

    def __str__(self):
        return self.vacancy_name

    def __lt__(self, other):
        return int(self.salary_minimal) < int(other.salary_minimal)

    def __le__(self, other):
        return int(self.salary_minimal) <= int(other.salary_minimal)

    def __gt__(self, other):
        return int(self.salary_minimal) > int(other.salary_minimal)

    def __ge__(self, other):
        return int(self.salary_minimal) >= int(other.salary_minimal)

    def __eq__(self, other):
        return int(self.salary_minimal) == int(other.salary_minimal)
