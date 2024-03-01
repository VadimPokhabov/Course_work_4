from config import FILE
from src.api_connect import VacancyAPI
from src.vacancies import Vacancy
import json
import requests


class GetHeadHunter(Vacancy, VacancyAPI):
    def __init__(self, name, top_n):
        """
        Класс получает вакансии с hh.ru
        """
        super().__init__(name, top_n)
        self.top_n = top_n
        self.url = "https://api.hh.ru"

    def __str__(self):
        """
        Удобочитаемое строковое представление объекта
        :return: self.name
        """
        return self.name

    def __repr__(self):
        """
        Информативное строковое представление объекта
        :return: self.__class__.__name__ (self.name, self.top_n)
        """
        return f"{self.__class__.__name__}({self.name}, {self.top_n})"

    @property
    def get_vacancy(self):
        """
        Получение вакансий,
            -только в России,
            -только enable_snippets,
            -только с указанием зарплаты
        :return: date
        """
        date = requests.get(f"{self.url}/vacancies",
                            params={'text': self.name,
                                    'area': 113,
                                    'enable_snippets': "true",
                                    'only_with_salary': "true",
                                    'per_page': self.top_n}).json()
        return date

    def get_json(self):
        """
        Открывает файл
        Только для записи. Создаст новый файл,
        если не найдет с указанным именем.
        Кодировка = utf-8
        """
        with open(FILE, "w", encoding="utf-8") as file:
            file.write(json.dumps(self.get_vacancy, indent=4, ensure_ascii=False))
