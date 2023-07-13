import requests


def get_employers_hh(employers_id):
    """Функция получает по API с HeadHunter данные о работодателях, список работодателей задается
    аргументом employers_id , получаем список, в котором Наименованией работодателей соответствует id c c HH.ru"""
    employers_data = []
    employers = []

    headers = {"User-Agent": "ParserEmployersVacancyAR (a.a.renkos@gmail.com)"}

    for i in employers_id:
        url = f"https://api.hh.ru/employers/{i}"
        params = {'page': i, 'per_page': 100}
        response = requests.get(url, headers=headers, params=params)
        data_employers = response.json()
        employers_data.append(data_employers)

    for i in employers_data:
        id_employer = i["id"]
        name = i['name']
        employers.append([id_employer, name])
    return employers


def get_vacancies_hh(employers_id):
    """Функция получает по API с HeadHunter данные о вакансиях определенных работодателей, список работодателей задается
    аргументом employers_id , получаем список, в котором : Название вакансии(vacancy_name), Работодатель(employer),
     Зарплата(salary), id работодателя(employer_id), Ссылка на вакансию(vacancy_url)"""
    vacancies_url = f"https://api.hh.ru/vacancies"
    headers = {"User-Agent": "ParserEmployersVacancyAR (a.a.renkos@gmail.com)"}
    vacancies_hh = []
    for employer in employers_id:
        params = {
            "employer_id": employer,
            "page": 0,
            "per_page": 100
        }
        response = requests.get(vacancies_url, headers=headers, params=params)
        vacancies_data = response.json()

        for vacancy in vacancies_data.get('items'):
            vacancy_name = vacancy['name']
            employer = vacancy['employer']['name']
            if vacancy['salary'] is None:
                continue
            else:
                salary = vacancy.get('salary').get('from')
            employer_id = vacancy['employer']['id']
            vacancy_url = vacancy['url']
            vacancies_hh.append([vacancy_name, employer, salary, employer_id, vacancy_url])
    return vacancies_hh


def get_query(query_type):
    """Функция для определения необходимого запроса к БД. Находит необходимый запрос и возвращает его"""
    with open('queries.sql') as f:
        label = False
        for line in f:
            if label:
                query = line
                break
            elif query_type in line:
                label = True
    return query
