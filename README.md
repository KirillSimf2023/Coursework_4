# Курсовая 4. ООП

## Задание
> В этом проекте вам предстоит написать парсер для сайтов.

Напишите программу, которая будет получать информацию о вакансиях с разных платформ в России, сохранять ее в файл и позволять удобно работать с ней (добавлять, фильтровать, удалять).

## Требования к реализации

1. Создать абстрактный класс для работы с API сайтов с вакансиями. Реализовать классы, наследующиеся от абстрактного класса, для работы с конкретными платформами. Классы должны уметь подключаться к API и получать вакансии.
2. Создать класс для работы с вакансиями. В этом классе самостоятельно определить атрибуты, такие как название вакансии, ссылка на вакансию, зарплата, краткое описание или требования и т. п. (не менее четырех) Класс должен поддерживать методы сравнения вакансий между собой по зарплате и валидировать данные, которыми инициализируются его атрибуты.
3. Определить абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления информации о вакансиях. Создать класс для сохранения информации о вакансиях в JSON-файл. Дополнительно, по желанию, можно реализовать классы для работы с другими форматами, например с CSV- или Excel-файлом, с TXT-файлом.
4. Создать функцию для взаимодействия с пользователем. Функция должна взаимодействовать с пользователем через консоль. Самостоятельно придумать сценарии и возможности взаимодействия с пользователем. Например, позволять пользователю указать, с каких платформ он хочет получить вакансии, ввести поисковый запрос, получить топ N вакансий по зарплате, получить вакансии в отсортированном виде, получить вакансии, в описании которых есть определенные ключевые слова, например "postgres" и т. п.
5. Объединить все классы и функции в единую программу.


## Требования к реализации в парадигме ООП

1. Абстрактный класс и классы для работы с API сайтов с вакансиями должны быть реализованы в соответствии с принципом наследования.
2. Класс для работы с вакансиями должен быть реализован в соответствии с принципом инкапсуляции и поддерживать методы сравнения вакансий между собой по зарплате.
3. Классы и другие сущности в проекте должны удовлетворять минимум первым двум требованиям принципов SOLID.


## Платформы для сбора вакансий

1. **hh.ru** ([ссылка на API](https://github.com/hhru/api/blob/master/docs/general.md))
2. **superjob.ru** ([ссылка на API](https://api.superjob.ru/))
    - Прежде чем начать использовать API от SuperJob, необходимо [зарегистрироваться](https://www.superjob.ru/auth/login/?returnUrl=https://api.superjob.ru/register/) и получить токен для работы. Подробная инструкция дается по ссылке описания документации в разделе [Getting started](https://api.superjob.ru/#gettin). При регистрации приложения можно указать произвольные данные.

## Выходные данные

- Информация о вакансиях, полученная с разных платформ, сохраненная в JSON-файл.
- Отфильтрованные и отсортированные вакансии, выводимые пользователю через консоль.


## Критерии оценивания работы:
- Проект выложили на GitHub.
- Из файла README понятно, о чём проект и как его использовать.
- В Git есть точечные коммиты.
- Код программы грамотно разбит на функции/классы/модули/пакеты.
- Код читабельный (хороший нейминг, есть docstring, используется typing).
- В работе используются абстрактные классы (минимум один).
- В работе есть переопределение магических методов.
- Для работы с API используется библиотека requests.
- В ходе работы программы создается файл со списком вакансий.
- Пользователь может вывести из файла набор вакансий по определенным критериям.