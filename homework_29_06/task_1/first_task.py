import math

class Square:
    def __init__(self):
        self.result = []

    def square_first_way(self, side):
        perimeter_square = side * 4
        square_area = side ** 2
        diagonal_square = side ** (1/2)
        self.result = [perimeter_square, square_area, diagonal_square]
        return self.result

    def square_second_way(self, side):
        return [side * 4, pow(side, 2), math.sqrt(side)]






