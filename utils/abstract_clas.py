from abc import ABC, abstractmethod

"1. Создать абстрактный класс для работы с API сайтов с вакансиями."


class AbstractJobPlatform(ABC):
    """Абстрактный класс, обязывающий создание методов в классах наследниках"""
    @abstractmethod
    def connect(self, number_of_page):
        pass

    @abstractmethod
    def get_vacancy(self):
        pass



