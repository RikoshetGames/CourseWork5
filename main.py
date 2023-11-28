from src.utils import get_employers, create_db, create_tables, fill_db, update_database_config
from config import config
from src.DBManager import DBManager

def main():
    companies = [1740,  # "Яндекс"
                 4181,  # "Банк ВТБ"
                 78638,  # "Тинькофф"
                 67611,  # "Тензор"
                 80,  # "Альфа-Банк"
                 9352463,  # "X5 Tech"
                 3529,  # "СБЕР"
                 2748,  # "Ростелеком"
                 733,  # "ЛАНИТ"
                 6093775  # "Aston"
                 ]

    print("Привет! Я бот, который будет находить вакансии по компаниям и их зарплатам.")
    print("Как вы хотите назвать свою базу данных?")
    user_input = input()
    database_name = user_input.lower()
    update_database_config()
    params = config()
    print('Данные успешно обновлены!')
    print(f"Создаю базу данных {database_name}, пожалуйста подождите...")

    create_db(database_name, params)
    create_tables(database_name, params)
    fill_db(get_employers(companies), database_name, params)

    print("Данные загружены, база данных создана!\n")
    dbmanager = DBManager(database_name, params)

    while True:
        print("Введите 1, чтобы получить список всех компаний и количество вакансий у каждой компании")
        print("Введите 2, чтобы получить список всех вакансий с указанием названия компании")
        print("Введите 3, чтобы Получить среднюю зарплату по вакансиям")
        print("Введите 4, чтобы Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям")
        print("Введите 5, чтобы Получить список всех вакансий, в названии которых содержатся переданные в метод слова")
        print("Введите Стоп, чтобы завершить работу")
        task = input("Ваш выбор: ")


        if task == "Стоп":
            break
        elif task == '1':
            print()
            print(dbmanager.get_companies_and_vacancies_count())
            print()
        elif task == '2':
            print()
            print(dbmanager.get_all_vacancies())
            print()
        elif task == '3':
            print()
            print(dbmanager.get_avg_salary())
            print()
        elif task == '4':
            print()
            print(dbmanager.get_vacancies_wth_highest_salary())
            print()
        elif task == '5':
            print()
            keyword = input('Введите ключевое слово: ')
            print(dbmanager.get_vacancies_with_keyword(keyword))
            print()
        else:
            print('Неправильный запрос')





if __name__ == '__main__':
    main()