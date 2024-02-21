from abc import abstractmethod


class UserForm:

    @abstractmethod
    def user_input_int(self):
        pass

    @abstractmethod
    def user_input_str(self):
        pass
