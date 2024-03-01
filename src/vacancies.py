class Vacancy:
    def __init__(self, name, page):
        """
        Инициализация
        :param name: name
        :param page: page
        """
        self.__name = name
        self.__page = page

    @property
    def name(self):
        """
        Расширение функционала с помощью @property
        """
        return self.__name

    @property
    def page(self):
        """
        Расширение функционала с помощью @property
        """
        return self.__page

    def __str__(self):
        """
        __str__ Vacancy
        :return: self.__name
        """
        return f"{self.__name}"

    def __repr__(self):
        """
        __repr__ Vacancy
        :return: f"{self.__class__.__name__}({self.__name, self.__page})"
        """
        return f"{self.__class__.__name__}({self.__name, self.__page})"
