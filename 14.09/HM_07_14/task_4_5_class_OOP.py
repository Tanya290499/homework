# Создать класс, у которого есть 2 статических аттрибута, и 4 динамических аттрибута,
# и реализованы 3 метода для экземпляров класса
class Parent:
    def __init__(self, age, profession, phone_number, salary):
        self._age = age
        self._profession = profession
        self._phone_number = phone_number
        self._salary = salary

    first_name = 'Oleg'
    last_name = 'Smirnov'

    @staticmethod
    def print_first_name():
        print(Parent.first_name)

    @staticmethod
    def print_last_name():
        print(Parent.last_name)

    @property
    def age(self):
        print(self._age)
        return self._age

    @age.setter
    def age(self, count):
        if isinstance(count, int) or isinstance(count, float):
            self._age = count
        else:
            raise TypeError('Result is always number')

    @property
    def profession(self):
        print(self._profession)
        return self._profession

    @profession.setter
    def profession(self, some_profession):
        if isinstance(some_profession, str):
            self._profession = some_profession
        else:
            raise TypeError('Result is always string')

    @property
    def phone_number(self):
        print(self._phone_number)
        return self._phone_number

    @phone_number.setter
    def phone_number(self, number):
        if isinstance(number, int) or isinstance(number, float):
            self._phone_number = number
        else:
            raise TypeError('Result is always number')

    @property
    def salary(self):
        print(self._salary)
        return self._salary

    @salary.setter
    def salary(self, some_salary):
        if isinstance(some_salary, int) or isinstance(some_salary, float):
            self._salary = some_salary
        else:
            raise TypeError('Result is always number')

    def get_full_name(self):
        return f'{Parent.first_name} {Parent.last_name}'

    def go_to_work(self):
        print(self.get_full_name(), ' is going to work today')

    def salary_check(self):
        if self.salary > 10000:
            print(self.get_full_name(), ' is very rich man')
        elif 100 < self.salary < 10000:
            print(self.get_full_name(), ' has an average salary')
        else:
            print(self.get_full_name(), ' has a small salary')


first_parent = Parent(37, 'builder', 375334567835, 100000)
Parent.print_first_name()
first_parent.salary_check()
first_parent.go_to_work()


