class User:
    MIN_AGE = 18
    def __init__(self, username, password, age):
        self.username= username
        self.password = password
        self.age = age

    def say(self, message):
        print(f'{self.username} says: \n-{message}')

    def __str__(self):
        return f"User({self.username}, {self.age})"


user = User('Patrick', 'qwerty', 30)
print(user)
