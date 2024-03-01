from abc import ABC, abstractmethod


class VacancyAPI(ABC):
    @abstractmethod
    def get_vacancy(self):
        """
        Определение абстракции класса VacancyAPI
        """
        pass
