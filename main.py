from Class_DBManager import DBManager
from utils import get_employers_hh, get_vacancies_hh

if __name__ == '__main__':
    employers_id = [906557, 3536900, 4949, 2324020, 3529, 3776, 41862, 839098, 2000762, 793926]

    db_manager = DBManager(host="localhost", database="postgres",
                           user="postgres", password="841345", port="5432")

    db_manager.create_database("hh")  # создание Базы данных с названием 'hh'
    db_manager.create_tables()  # создание  в базе данных таблиц vacancies и employers

    employers = get_employers_hh(employers_id)  # получает данные о работодателях и записываем в переменную
    vacancies = get_vacancies_hh(employers_id)  # получает список вакансий и записываем в переменную

    db_manager.save_employers_to_db(employers)  # сохраняет данные о работодателях в таблицу
    db_manager.save_vacancies_to_db(vacancies)  # сохраняет данные о вакансиях в таблицу

    db_manager.get_companies_and_vacancies_count()  # получает список компаний и количество вакансий у каждой компании
    avg_salary = db_manager.get_avg_salary()  # получает среднюю зарплату
    print(f"Средняя зарплата: {avg_salary}")
    db_manager.get_all_vacancies()  # получает список всех вакансий

    db_manager.get_vacancies_with_higher_salary(avg_salary)  # получает список вакансий с зп больше средней
    keyword = input('Введите Слово для поиска вакансий')
    db_manager.get_vacancies_with_keyword(keyword)  # получает список вакансий по ключевомму слову
