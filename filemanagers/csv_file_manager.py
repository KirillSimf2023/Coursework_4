import csv

from filemanagers.filemanager_abstract import FileManager
from utils.vacancy import Vacancy


class CSVFileManager(FileManager):
    """Класс для работы с CSV-файлами"""

    def save_to_file(self, filename):
        """Функция сохраняет созданные вакансии на основе
        класса Vacancy в файл
        :param filename: название файла"""

        with open(f'data/{filename}.csv', 'w', encoding='UTF-8') as file:
            writer = csv.writer(file, lineterminator="\r")
            writer.writerow([
                '№ваканчии',
                'описание',
                'URL',
                'мин.зарплата',
                'макс.зарплата',
                'валюта',
                'работодатель',
                'описание'
            ])

            for vacancy in Vacancy.all_class_vacancy:
                writer.writerow([
                    vacancy.id,
                    vacancy.title,
                    vacancy.link,
                    vacancy.salary_min,
                    vacancy.salary_max,
                    vacancy.salary_currency,
                    vacancy.company_name,
                    vacancy.description
                ])

    def load_from_file(self, filename):
        """Функция загружает вакансии из файла, создавая
        объекты на основе класса Vacancy
        :param filename: название файла"""

        Vacancy.all_class_vacancy.clear()
        try:
            with open(f'data/{filename}.csv', 'r', encoding='UTF-8') as file:
                reader = csv.reader(file)
                for row in reader:

                    # проверяет является ли ряд названием колонок
                    if row[0] == '№ваканчии':
                        continue

                    Vacancy( {'id': row[0],
                              'title': row[1],
                              'link': row[2],
                              'salary_min': row[3],
                              'salary_max': row[4],
                              'salary_currency': row[5],
                              'company_name': row[6],
                              'description': row[7]})

                return Vacancy.all_class_vacancy
        except FileNotFoundError:
            return 'Такого файла не существует!'


    def delete_vacancy(self, filename, value):
        '''
        Удаляет вакансию из файла по переданому
        номеру вакансии
        :param value: номер вакансии
        :param filename: название файла
        '''
        try:
            with open(f'data/{filename}.csv', 'r+', encoding='UTF-8') as file:
                reader = csv.reader(file)
                writer = csv.writer(file, lineterminator="\r")
                rows = []
                for row in reader:
                    rows.append(row)
                if int(value) > 0 and int(value) <= len(rows):
                    del rows[int(value)]
                    file.seek(0)
                    file.truncate()
                    for row in rows:
                        writer.writerow(row)
                    return 'Вакансия успешно удалена!'
                else:
                    return 'Вакансии с таким номером не существует'
        except FileNotFoundError:
            return 'Такого файла не существует!'
        except ValueError:
            return 'Вы ввели некоректные данные'


