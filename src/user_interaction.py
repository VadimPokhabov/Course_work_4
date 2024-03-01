from src.get_vacancies_api_hh import GetHeadHunter
from src.utils import HHRequestDebug, DebugUserJson
from src.sorted_vacancies import SortedVacancy


class UserInteractionHeadHunter(HHRequestDebug):
    def hh_user_search(self):
        """
        Функция для обращения пользователя к сайту ХХ.ру.
        Записывает результат в JSON файл
        """
        search_query = self.user_input_str()
        top_n = self.user_input_int()
        result_search = GetHeadHunter(search_query, top_n)
        result_search.get_json()


class UserInteractionJson(DebugUserJson):
    def json_user_search(self):
        """
        Функция после проверки на целостность ввода,
        добавляет значения ввода юзера и выдаёт результат
        """
        vacancies_list = []
        json_file = SortedVacancy()
        json_vacancies = json_file.sorted_vacancies_hh
        payment = self.user_input_int()
        city = self.user_input_str()
        for vacancies in json_vacancies:
            if payment > vacancies["payment_from"]:
                continue
            if city == vacancies["city"]:
                vacancies_list.append(vacancies)
            if city == "":
                vacancies_list.append(vacancies)
        for result in vacancies_list:
            print(f"Город: {result['city']}\nДата публикации: {result['date']}\n"
                  f"Должность: {result['name']}\nТребование: {result['requirement']}\n"
                  f"Ответственность: {result['responsibility']}\nЗарплата от {result['payment_from']}\n"
                  f"Ссылка на сайт hh.ru: {result['url']}")
        if len(vacancies_list) == 0:
            print(f'Результатов 0')
