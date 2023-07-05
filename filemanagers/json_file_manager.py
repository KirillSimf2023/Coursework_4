import json
from filemanagers.filemanager_abstract import FileManager
from utils.vacancy import Vacancy


class JsonFileManager(FileManager):
    """Класс для работы с JSON-файлами"""

    def save_to_file(self, filename):
        """    Функция сохраняет созданные вакансии на основе
        класса Vacancy в файл
        :param filename: название файла"""

        with open(f'data/{filename}.json', 'w', encoding='UTF-8') as file:
            json_data = []
            for vacancy in Vacancy.all_class_vacancy:
                data = {'id': vacancy.id, 'title': vacancy.title, 'link': vacancy.link,
                        'company_name': vacancy.company_name, 'description': vacancy.description,
                        'salary_min': vacancy.salary_min, 'salary_max': vacancy.salary_max,
                        'salary_currency': vacancy.salary_currency}
                json_data.append(data)
            file.write(json.dumps(json_data, ensure_ascii=False))


    def load_from_file(self, filename):
        """Функция загружает вакансии из файла, создавая
        объекты на основе класса Vacancy
        :param filename: название файла"""

        Vacancy.all_class_vacancy.clear()

        try:
            with open(f'data/{filename}.json', 'r', encoding='UTF-8') as file:
                data = json.load(file)

                if len(data) > 0:
                    # цикл перебирает данные каждой вакансии
                    for vacancy in data:
                        Vacancy(vacancy)
                else:
                    return 'Файл пуст!'

                return Vacancy.all_class_vacancy
        except FileNotFoundError:
            return 'Такого файла не существует!'


    def delete_vacancy(self, filename: str, value: int):
        """Удаляет вакансию из файла по переданному
        номеру вакансии
        :param value: номер вакансии
        :param filename: название файла"""

        try:
            with open(f'data/{filename}.json', 'r+', encoding='UTF-8') as file:
                try:
                    json_data = json.load(file)

                    del json_data[int(value) - 1]
                    file.seek(0)
                    file.truncate()
                    file.write(json.dumps(json_data, ensure_ascii=False))
                    return 'Вакансия успешно удалена!'
                except IndexError:
                    print('Вакансии с таким номером не существует')
                except ValueError:
                    return 'Ты ввели некорректные данные'
        except FileNotFoundError:
            return 'Такого файла не существует!'

