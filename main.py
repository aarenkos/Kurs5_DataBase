from utils import get_employers_hh, get_vacancies_hh

if __name__ == '__main__':

    employers_id = [906557, 3536900, 4949, 2324020, 3529, 3776, 41862, 839098, 2000762, 793926]

    employers = get_employers_hh(employers_id)

    # print (employers)

    vacancies = get_vacancies_hh(employers_id)

    # print(vacancies)

