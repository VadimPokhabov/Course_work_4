import json
from datetime import datetime
from config import FILE
from pprint import pprint


class SortedVacancy:
    """
    Класс сортирует вакансии
    """
    def __init__(self):
        self.head_hunter_sorted = []
        self.date_format = None

    @property
    def sorted_vacancies_hh(self):
        """
        Получаем отсортированный список вакансий из json файла
        :return: self.head_hunter_sorted
        """
        with open(FILE, encoding="utf-8") as file:
            content = json.load(file)
        for i in content["items"]:
            if i["salary"]["from"] is None:
                i["salary"]["from"] = 0
            if i["salary"]["to"] is None:
                i["salary"]["to"] = 0
            if i["published_at"]:
                date = datetime.strptime(i["published_at"], "%Y-%m-%dT%H:%M:%S+%f")
                self.date_format = f"{date:%d.%m.%Y}"
            self.head_hunter_sorted.append({
                "name": i["name"],
                "url": i["apply_alternate_url"],
                "city": i["area"]["name"],
                "currency": i["salary"]["currency"],
                "payment_from": i["salary"]["from"],
                "payment_to": i["salary"]["to"],
                "requirement": i["snippet"]["requirement"],
                "responsibility": i["snippet"]["responsibility"],
                "date": self.date_format
            })
        return self.head_hunter_sorted


if __name__ == '__main__':
    r = SortedVacancy()
    pprint(r.sorted_vacancies_hh)
