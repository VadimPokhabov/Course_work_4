from abc import abstractmethod


class UserForm:

    @abstractmethod
    def user_input_int(self) -> int:
        """
        Определение абстракции user_input_int
        """
        pass

    @abstractmethod
    def user_input_str(self) -> str:
        """
        Определение абстракции user_input_str
        """
        pass
