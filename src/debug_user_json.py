from src.user_forms import UserForm


class DebugUserJson(UserForm):
    payment_from = None
    city = None

    def user_input_int(self):
        self.payment_from = input("Введите минимальную зарплату: ")
        if self.payment_from.isalpha():
            raise ValueError("Количество не может быть строкой")
        if self.payment_from == "":
            self.payment_from = 0
        return int(self.payment_from)

    def user_input_str(self):
        self.city = input("Введите город: ").title()
        if self.city.isdigit():
            raise TypeError("Запрос не может быть числом")
        return self.city


if __name__ == '__main__':
    r = DebugUserJson()
    print(r.user_input_str())