from Class_DBManager import DBManager
from utils import get_employers_hh, get_vacancies_hh

if __name__ == '__main__':
    employers_id = [906557, 3536900, 4949, 2324020, 3529, 3776, 41862, 839098, 2000762, 793926]

    db_manager = DBManager(host="localhost", database="postgres", user="postgres", password="841345", port="5432")

    # db_manager.drop_database('hh')

    db_manager.create_database("hh")  # создание БД с названием HH
    db_manager.create_tables()  # создание таблиц

    employers = get_employers_hh(employers_id)

    # print (employers)

    vacancies = get_vacancies_hh(employers_id)
    #
    # print(vacancies)


    db_manager.save_employers_to_db(employers)
    db_manager.save_vacancies_to_db(vacancies)

    db_manager.get_companies_and_vacancies_count()
    avg_salary = db_manager.get_avg_salary()
    print(f"Средняя зарплата: {avg_salary}")
    db_manager.get_all_vacancies()

    db_manager.get_vacancies_with_higher_salary(avg_salary)
    keyword = input('Введите Слово для поиска вакансий')
    db_manager.get_vacancies_with_keyword(keyword)
