from src.utils import get_employers, create_db, create_tables, fill_db, update_database_config, user_interface
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

    user_interface(database_name, params)





if __name__ == '__main__':
    main()