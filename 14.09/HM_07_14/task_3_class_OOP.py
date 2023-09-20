class People:
    def __init__(self, age, first_name, last_name, eye_color, hair_color):
        self._age = age
        self._first_name = first_name
        self._last_name = last_name
        self._eye_color = eye_color
        self._hair_color = hair_color

    def print_people_information(self):
        print('Возраст:', self._age, '\n', 'Имя:', self._first_name, '\n', 'Фамилия:', self._last_name, '\n',
              'Цвет глаз:', self._eye_color, '\n', 'Цвет волос:', self._hair_color)


ages = 20
first_names = 'Katya'
last_names = 'Pygovka'
eye_colors = 'blue'
hair_colors = 'black'
for i in range(1):
    first_people = People(ages, first_names, last_names, eye_colors, hair_colors)
    first_people.print_people_information()
