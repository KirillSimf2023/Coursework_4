from utils.abstract_clas import AbstractJobPlatform
import requests
import time
from utils.convecter_currency import ConvecterCurrency
from abc import ABC

"1. Реализовать классы, наследующиеся от абстрактного класса, для работы с "
"конкретными платформами."
"Классы должны уметь подключаться к API и получать вакансии."
"Данный класс для сайта HH.ru"

class HhruJob(AbstractJobPlatform):

    def __init__(self, key_word: str, with_salary=False, min_salary=None):
        self.key_word = key_word
        self.with_salary = with_salary
        self.min_salary = min_salary


    def connect(self, number_of_page):
        url = "https://api.hh.ru/vacancies"
        params = {
            "text": self.key_word,
            "area": 113,  # Россия
            "per_page": 100,  # количество вакансий на страницу
            "page": number_of_page,  # номер страницы
            "only_with_salary": self.with_salary,
            "salary": self.min_salary,
        }
        response = requests.get(url, params=params)
        return response


    def get_vacancy(self):

        #максимум мы можем получить 2000 вакансий за 1 сессию, по 100 вакансий на странице, соответственно число страниц 20
        number_of_pages = 20

        list_jobs = []

        for k in range(number_of_pages):
            
            # задержка
            time.sleep(0.25)
            
            response = self.connect(k)

            # проверяем что получен ответ от сайта
            if response.status_code == 200:
                data = response.json()
                vacancies = data.get("items")

                i = 0
                for item in vacancies:

                    id_vacancy = item['id']
                    title = item['name']
                    link = item['alternate_url']
                    company_name = item["employer"]["name"]
                    description = item['snippet']['requirement']

                    if item['salary'] is not None:
                        salary_min = item.get('salary').get('from')
                        salary_max = item.get('salary').get('to')
                        salary_currency = item.get('salary').get('currency')
                    else:
                        salary_min = 0
                        salary_max = 0
                        salary_currency = 'нет'

                    #  Создание словарей из вакансий
                    job = {
                        'id': id_vacancy,
                        'title': title,
                        'link': link,
                        'salary_min': salary_min,
                        'salary_max': salary_max,
                        'salary_currency': salary_currency,
                        'company_name': company_name,
                        'description': description
                    }

                    list_jobs.append(job)

            else:
                print(f"Request failed with status code: {response.status_code}")

        # response.close()
        return list_jobs




     
