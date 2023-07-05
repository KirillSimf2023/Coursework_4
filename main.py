from utils.hhru import HhruJob
from utils.superjob import SuperJob
from filemanagers.json_file_manager import JsonFileManager
from filemanagers.csv_file_manager import CSVFileManager
from utils.vacancy import Vacancy



def main():
    # main menu

    input_url = None
    input_key_word = None
    input_city = None
    with_salary = None
    min_salary = None

    print('Приветствую! Я помогу тебе найти работу')
    print('Помогу найти вакансии на HH.ru и SuperJob.ru')


    # выбираем сайт для поиска
    while True:
        input_url = input('Выбери сайт (введи цифру): 1 - HH.ru, 2 - SuperJob.ru, 7 - выход из программы')
        match input_url:
            case '1':
                print("HH.ru")
                select_url = 1
                # second_menu(select_url)
                break
            case '2':
                print("SuperJob.ru")
                select_url = 2
                break
            case '7':
                print("Спасибо что использовал мою программу!!!")
                quit()
            case _:
                print("Не правильно ввел выбор! Попробуй еще раз.")

    # получаем ключевое слово для поиска
    while True:
        input_key_word = input('Укажите ключевое слово поиска или для выхода из программы введите 7:')

        match input_key_word:
            case '7':
                print("Спасибо что использовал мою программу!!!")
                quit()
            case _:
                print("Ключевое слово: ", input_key_word)
                break

    # получаем город для поиска
    while True:
        input_city = input(
            'Укажи город в которм ищещь работу, если город не важен введи 2, если хочешь прекратить поиск и выйти из программы, введи 7')
        match input_city:
            case '2':
                print("Понял, город не важен. Ищем все вакансии")
                input_city = ''
                break
            case '7':
                print("Спасибо что использовал мою программу!!!")
                quit()
            case _:
                print("Город: ", input_city)
                break

    # ищем все вакансии или только с зарплатой
    while True:
        with_salary = input('Ищем все вакансии введи 2, только с зарплатой введите 1, для выхода из программы введи 7')
        match with_salary:
            case '1':
                with_salary=True
                while True:
                    min_salary = input('Укажите минимальную зарплату, если это не важно введите 1, для выхода из программы введи 7')
                    match min_salary:
                        case '1':
                            min_salary = None
                            break
                        case '7':
                            print("Спасибо что использовал мою программу!!!")
                            quit()
                        case _:
                            if min_salary.isdigit() and int(min_salary)>0:
                                break
                            else:
                                print('Ты ввел не число, попробуй еще раз.')
                break
            case '2':
                with_salary = False
                min_salary = None
                break
            case '7':
                print("Спасибо что использовал мою программу!!!")
                quit()
            case _:
                print("Не правильно ввел выбор! Попробуй еще раз.")

    print("Все данные принял, начинаю поиск:")

    if input_url == '1':
        # HH.ru
        my_hhru = HhruJob(input_key_word+' '+input_city, with_salary, min_salary)
        list_jobs = my_hhru.get_vacancy()
    else:
        # SuperJob
        my_superjonb = SuperJob(input_key_word+' '+input_city, with_salary, min_salary)
        list_jobs = my_superjonb.get_vacancy()

    Vacancy.class_vacancy(list_jobs)

    print(f'Найдено {len(Vacancy.all_class_vacancy)} вакансий')

    while True:
        input_User = input('1 - вывести в консоль, 2 - сохранить в JSON файл, 3 - сохранить в CSV файл, 7 - выйти')
        match input_User:
            case '1':
                # 1 - вывести в консоль
                for item in Vacancy.all_class_vacancy:
                    print(item)
            case '2':
                # 2 - сохранить в JSON файл
                json_file = JsonFileManager()
                json_file.save_to_file('my_vacancy')
                print('Вакансии сохранены в папку data, имя файла: my_vacancy.json')
            case '3':
                # 3 - сохранить в CSV
                csv_file = CSVFileManager()
                csv_file.save_to_file('my_vacancy')
                print('Вакансии сохранены в папку data, имя файла: my_vacancy.csv')
            case '7':
                print("Спасибо что использовал мою программу!!!")
                quit()
            case _:
                print('Ты ввел неправильную команду, попробуй еще раз.')



if __name__ == '__main__':
    main()

