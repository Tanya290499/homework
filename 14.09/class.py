import datetime


class Child:
    COUNTRY = 'Belarus'

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = 0
        self.birthday = datetime.datetime.now()
        print(self.name)

    @classmethod
    def new_born(cls):
        print(cls)
        print('new_born age is 0')

    @staticmethod
    def some_count():
        print('count ship...')

    def cry(self):
        print(f'{self.name} is crying...')


c = Child('Johnny', 'Wick', 'M')


class YoungMan(Child):
    def __init__(self, name, surname, gender, birthday):
        super().__init__(name, surname, gender)
        self.birthday = birthday
        current_year = datetime.date.today().year
        self.age = current_year - self.birthday.year

    def go_to_school(self):
        print(f'{self.name} is going to school')


dob = datetime.date(2000, 7, 25)

y = YoungMan('Mason', 'Merlin', 'M', dob)
class Actors:
    def improvization(self):
        print('do some stuff...')

class Adult(YoungMan, Actors):
    def __init__(self, name, surname, gender, birthday, profession):
        super().__init__(name, surname, gender, birthday)
        self.profession = profession

    def go_to_school(self):
        raise NotImplemented('too old for school =(')


dob1 = datetime.date(1995, 8, 10)
adult = Adult('Emma', 'Stone', 'W', dob1, 'Actress')
print(adult.birthday, adult.age, adult.profession)
adult.improvization()