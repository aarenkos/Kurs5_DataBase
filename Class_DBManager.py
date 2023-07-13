import psycopg2

from utils import get_query


class DBManager:

    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port


    def connect_bd(self, name_bd):
        conn = psycopg2.connect(
            host=self.host,
            database=name_bd,
            user=self.user,
            password=self.password,
            port=self.port
        )
        return conn
    def create_database(self, name):
        connect_bd = self.connect_bd("postgres")
        connect_bd.autocommit = True
        curs = connect_bd.cursor()

        query_delete_database = get_query('--delete_database')
        query_create_database = get_query('create_database')
        get_query('--session_termination')
        curs.execute(f"{query_delete_database} {name}")
        curs.execute(f"{query_create_database} {name}")

        connect_bd.commit()

        curs.close()
        connect_bd.close()

    def create_tables(self):

        create_tables_employers = get_query('--create_tables_employers')
        create_tables_vacancies = get_query('--create_tables_vacancies')

        connect_bd = self.connect_bd("hh")
        connect_bd.autocommit = True
        cur = connect_bd.cursor()


        cur.execute(create_tables_employers)
        cur.execute(create_tables_vacancies)
        connect_bd.commit()

        cur.close()
        connect_bd.close()

    def drop_database(self, name):

        connect_bd = self.connect_bd("hh")
        connect_bd.autocommit = True
        cur = connect_bd.cursor()
        session_termination = get_query('--session_termination')
        delete_database = get_query('--delete_database')

        cur.execute(session_termination)
        cur.execute(f"{delete_database} {name} ")

        cur.close()
        connect_bd.close()

    def get_companies_and_vacancies_count(self):

        companies_and_vacancies_count = get_query('--get_companies_and_vacancies_count')

        connect_bd = self.connect_bd("hh")
        connect_bd.autocommit = True
        cur = connect_bd.cursor()

        cur.execute(companies_and_vacancies_count)
        results = cur.fetchall()

        for company, vacancies_count in results:
            print(f"Company: {company}, Vacancies Count: {vacancies_count}")

        connect_bd.commit()
        cur.close()
        connect_bd.close()

    def save_employers_to_db(self, data):

        connect_bd = self.connect_bd("hh")
        connect_bd.autocommit = True
        cur = connect_bd.cursor()

        for employer in data:
            save_employers_to_db = get_query('--save_employers_to_db')
            cur.execute(save_employers_to_db, employer)

        connect_bd.commit()
        cur.close()
        connect_bd.close()

    def save_vacancies_to_db(self, data):

        connect_bd = self.connect_bd("hh")
        connect_bd.autocommit = True
        cur = connect_bd.cursor()
        for vacancy in data:
            save_vacancies = get_query('--save_vacancies_to_db')
            cur.execute(save_vacancies, vacancy)

        connect_bd.commit()
        cur.close()
        connect_bd.close()

    def get_all_vacancies(self):
        get_vacancies = get_query('--get_all_vacancies')
        connect_bd = self.connect_bd("hh")
        connect_bd.autocommit = True
        cur = connect_bd.cursor()
        cur.execute(get_vacancies)
        results = cur.fetchall()
        for name, employer, salary,employer_id, url in results:
            print(f"Company: {employer}, vacancy: {name}, salary: {salary}, link: {url}")

        connect_bd.commit()
        cur.close()
        connect_bd.close()

    def get_avg_salary(self):

        query_avg_salary = get_query('avg_salary')
        connect_bd = self.connect_bd("hh")
        connect_bd.autocommit = True
        cur = connect_bd.cursor()

        cur.execute(query_avg_salary)
        result = cur.fetchone()
        avg_salary = round(result[0])

        connect_bd.commit()
        cur.close()
        connect_bd.close()
        return avg_salary

    def get_vacancies_with_higher_salary(self, avg_salary):

        query_vacancies_with_higher_salary = get_query('--get_vacancies_with_higher_salary')
        connect_bd = self.connect_bd("hh")
        connect_bd.autocommit = True
        cur = connect_bd.cursor()

        cur.execute(query_vacancies_with_higher_salary, (avg_salary,))
        results = cur.fetchall()
        for name, employer, salary, employer_id, url in results:
            print(f"Company: {employer}, vacancy: {name}, salary: {salary}, link: {url}")

        connect_bd.commit()
        cur.close()
        connect_bd.close()

    def get_vacancies_with_keyword(self, keyword: str):
        query_vacancies_with_keyword = get_query('--get_vacancies_with_keyword')

        connect_bd = self.connect_bd("hh")
        connect_bd.autocommit = True
        cur = connect_bd.cursor()

        cur.execute(query_vacancies_with_keyword, ('%' + keyword + '%',))
        results = cur.fetchall()
        for name, employer, salary,employer_id, url in results:
            print(f"Company: {employer}, vacancy: {name}, salary: {salary}, link: {url}")

        connect_bd.commit()
        cur.close()
        connect_bd.close()
