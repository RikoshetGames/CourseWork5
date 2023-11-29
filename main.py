from src.utils import get_employers, create_db, create_tables, fill_db, update_database_config, user_interface, is_english
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
    print('Введине название создаваемой базы данных, либо введите "стоп", чтобы завершить работу.')

    while True:
        user_input = input().lower()
        if user_input == "стоп" or user_input == "stop":
            break
        elif not is_english(user_input):
            print("Пожалуйста, введите только английские буквы.")
            continue
        else:
            database_name = user_input.lower()
            update_database_config()
            params = config()
            print('Данные успешно обновлены!')

            create_db(database_name, params)
            create_tables(database_name, params)
            fill_db(get_employers(companies), database_name, params)

            print("Данные загружены, база данных создана!\n")
            break

    if user_input == "стоп" or user_input == "stop":
        print("До свидания!")
    else:
        user_interface(database_name, params)





if __name__ == '__main__':
    main()