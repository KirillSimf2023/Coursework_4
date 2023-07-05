"""
2. Создать класс для работы с вакансиями.
В этом классе самостоятельно определить атрибуты, такие как:
 - название вакансии,
 - ссылка на вакансию,
 - зарплата,
 - краткое описание
 или требования и т. п. (не менее четырех)
Класс должен поддерживать методы сравнения вакансий между собой по зарплате и
валидировать данные, которыми инициализируются его атрибуты.
"""

class Vacancy():
    """Класс создающий экземпляры класса вакансий"""
    all_class_vacancy = []  # список экземпляров класса, изначально пустой

    def __init__(self, in_vacancy: dict):
        self.id = in_vacancy['id']
        self.title = in_vacancy['title']
        self.link = in_vacancy['link']
        # self.salary_min = in_vacancy['salary_min']
        # self.salary_max = in_vacancy['salary_max']
        # self.salary_currency = in_vacancy['salary_currency']
        self.company_name = in_vacancy['company_name']
        self.description = in_vacancy['description']

        if in_vacancy['salary_min'] is None:
            self.salary_min = 0
        else:
            self.salary_min = int(in_vacancy['salary_min'])

        if in_vacancy['salary_max'] is None:
            self.salary_max = 0
            # salary_max = 0
        else:
            # salary_max = item['salary']['to']
            self.salary_max = int(in_vacancy['salary_max'])

        if in_vacancy['salary_currency'] is None:
            self.salary_currency = 'нет'
        else:
            # salary_currency = item['salary']['currency']
            self.salary_currency = in_vacancy['salary_currency']

        Vacancy.all_class_vacancy.append(self)

    def __str__(self):
        return (f'ID: {self.id}, Title: {self.title}, URL: {self.link}, Salary_min: {self.salary_min}, Salary_max: {self.salary_max}, Currency: {self.salary_currency}')

    @classmethod
    def class_vacancy(cls, vacancy: list):
        """Метод для создания экземпляров класса"""
        for in_vacancy in vacancy:
            cls(in_vacancy)

    @property
    def salary_avg(self) -> int:
         """Возвращает среднюю зарплату вакансии
        :return: средняя зарплата
        """
         if (self.salary_min + self.salary_max) == 0:
            return 0
         avg_salary = int((self.salary_min + self.salary_max) / 2)
         return avg_salary


    def __eq__(self, other):
        """Метод сравнивает зарплаты двух вакансий
        :param other: вакансия с которой сравнивают
        :return: результат"""

        if self.salary_avg == other.salary_avg:
            return 'Зарплаты одинаковы'
        else:
            return 'Зарплаты не равны'


    def __lt__(self, other) -> str:
        """Метод проверяет является ли зарплата первой вакансии
        меньше, чем зарплата второй вакансии
        :param other: вакансия с которой сравнивают
        :return: результат"""

        first_salary = int(self.salary_avg)
        second_salary = int(other.salary_avg)

        if first_salary < second_salary:
            difference = second_salary - first_salary
            return f'{other.id} больше на {difference}'
        else:
            difference = first_salary - second_salary
            return f'{self.id} больше на {difference}'


    def __le__(self, other) -> str:
        """ Метод проверяет является ли зарплата первой вакансии
        меньше или равна, чем зарплата второй вакансии
        :param other: вакансия с которой сравнивают
        :return: результат"""

        first_salary = int(self.salary_avg)
        second_salary = int(other.salary_avg)

        if first_salary == second_salary:
           return 'Зарплаты равны'
        else:
           return self.__lt__(other)


    def __gt__(self, other) -> str:
        """Метод проверяет является ли зарплата первой вакансии
        больше, чем зарплата второй вакансии
        :param other: вакансия с которой сравнивают
        :return: результат"""

        first_salary = int(self.salary_avg)
        second_salary = int(other.salary_avg)

        if first_salary > second_salary:
             difference = first_salary - second_salary
             return f'{other.id} больше на {difference}'
        else:
            difference = second_salary - first_salary
            return f'{self.id} больше на {difference}'


    def __ge__(self, other) -> str:
        """Метод проверяет является ли зарплата первой вакансии
        больше или равно, чем зарплата второй вакансии
        :param other: вакансия с которой сравнивают
        :return: результат"""

        first_salary = int(self.salary_avg)
        second_salary = int(other.salary_avg)

        if first_salary == second_salary:
            return 'Зарплаты равны'
        else:
            return self.__gt__(other)


