from src.debug_user_json import DebugUserJson
from src.get_vacancies_api_hh import GetHeadHunter
from src.debug_hh_requests import HHRequestDebug
from src.sorted_vacancies import SortedVacancy


class UserInteractionHeadHunter(HHRequestDebug):
    def hh_user_search(self):
        search_query = self.user_input_str()
        top_n = self.user_input_int()
        result_search = GetHeadHunter(search_query, top_n)
        result_search.get_json()


class UserInteractionJson(DebugUserJson):
    def json_user_search(self):
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
                  f"Ответственность: {result['responsibility']}\nЗарплата от {result['payment_from']}\n")
        if len(vacancies_list) == 0:
            print(f'Результатов 0')


if __name__ == '__main__':
    # r = UserInteractionJson()
    # r.json_user_search()
    r = UserInteractionHeadHunter()
    r.hh_user_search()
