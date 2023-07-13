--delete_database
DROP DATABASE IF EXISTS

--create_database
CREATE DATABASE

--create_tables_employers
CREATE TABLE employers (id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL)

--create_tables_vacancies
CREATE TABLE vacancies (name VARCHAR(255) NOT NULL, employer VARCHAR NOT NULL, salary INT, employer_id SERIAL REFERENCES employers(id), url TEXT)

--session_termination
SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = 'hh' AND pid <> pg_backend_pid()

--get_companies_and_vacancies_count
SELECT employer, COUNT(*) AS vacancies_count FROM vacancies GROUP BY employer

--save_employers_to_db
INSERT INTO employers (id, name) VALUES (%s, %s) ON CONFLICT DO NOTHING

--save_vacancies_to_db
INSERT INTO vacancies (name, employer, salary, employer_id, url) VALUES (%s, %s, %s, %s, %s)

--get_all_vacancies
SELECT * from vacancies

--get_avg_salary
SELECT AVG(salary) AS avg_salary FROM vacancies WHERE salary IS NOT NULL

--get_vacancies_with_higher_salary
SELECT * FROM vacancies WHERE salary > %s

--get_vacancies_with_keyword
SELECT * FROM vacancies WHERE name ILIKE %s












Поиск
SELECT employer, COUNT(*) AS vacancies_count FROM vacancies GROUP BY employer;

--get_companies_and_vacancies_count
SELECT * from vacancies

SELECT * FROM vacancies WHERE salary > %s;

SELECT * FROM vacancies WHERE name ILIKE %s

