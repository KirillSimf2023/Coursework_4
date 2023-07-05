from utils.abstract_clas import AbstractJobPlatform
import requests
import time



"1. Реализовать классы, наследующиеся от абстрактного класса, для работы с "
"конкретными платформами."
"Классы должны уметь подключаться к API и получать вакансии."
"Данный класс для сайта superjob.ru"
class SuperJob(AbstractJobPlatform):

    SuperJob_Key = 'v3.r.137619945.1246a6841bd65492ae94a45fcaa54c7cb82a98ab.49fbd189b98ae7e1c37982251922411dd65dfe83'

    def __init__(self, key_word: str, with_salary=False, min_salary=None):
        self.key_word = key_word
        self.with_salary = with_salary
        self.min_salary = min_salary


    def connect(self, number_of_page):

        url = 'https://api.superjob.ru/2.0/vacancies/'
        headers = {
            "X-Api-App-Id": self.SuperJob_Key,
            'Host': 'api.superjob.ru',
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application/x-www-form-urlencoded'
            }

        params = {"keyword": self.key_word,
                  'town': 0,
                  "count": 100,
                  "page": number_of_page,
                  "archive": False,
                  "no_agreement": self.with_salary,
                  "payment_from": self.min_salary,
                  }

        page_response = requests.get(url, headers=headers, params=params)

        return page_response



    def get_vacancy(self):
        # count = 0

        # максимум мы можем получить 6000 вакансий за 1 сессию, по 100 вакансий на странице, соответственно число страниц 6
        number_of_pages = 6

        list_jobs = []

        # максимум мы можем получить 600 вакансий за 1 сессию, по 100 вакансий на странице, соответственно число страниц 6
        for i in range(number_of_pages):
            # задержка
            time.sleep(0.25)

            page_response = self.connect(i)
            data_super = page_response.json()
            result = data_super.get('objects')
            # print(data_super)
            # print(result)

            for item in result:

                id_vacancy = item['id']
                title = item['profession']
                company_name = item["firm_name"]
                salary_min = item.get('payment_from')
                salary_max = item.get('payment_to')
                description = item['profession']
                link = 'https://superjob.ru' + 'id_vacancy'
                salary_currency = item.get('currency')

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

        return list_jobs


