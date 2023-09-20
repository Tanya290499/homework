import random


class Student:
    def __init__(self, age, first_name, last_name):
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def print_student_data(self):
        print(self.age, self.first_name, self.last_name)


ages = [20, 28, 24, 26, 19, 23, 25]
first_names = ['Olya', 'Petya', 'Katya', 'Masha', 'Tanya', 'Sveta', 'Kostya']
last_names = ['Kosparov', 'Grechkin', 'Pechkina', 'Dobrev', 'Motina', 'Demido', 'Godnev']
random_students = []
for i in range(10):
    random_age = random.randrange(len(ages))
    random_first_name = random.randrange(len(first_names))
    random_last_name = random.randrange(len(last_names))
    random_student = Student(ages[random_age], first_names[random_first_name], last_names[random_last_name])
    random_students += [random_student]
    random_student.print_student_data()

