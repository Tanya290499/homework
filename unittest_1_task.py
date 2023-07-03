import unittest

from parameterized import parameterized

from course.homework.first_task import Square

class Test_first_task(unittest.TestCase):
    @parameterized.expand([(16, [64, 256, 4]), (0, [0, 0, 0])])
    def test_01_square_first_way(self, side, expected_result):
        square = Square()
        result = square.square_first_way(side)
        self.assertEqual(result, expected_result)

    @parameterized.expand([(16, [64, 256, 4]), (0, [0, 0, 0])])
    def test_02_square_second_way(self, side, expected_result):
        square = Square()
        result = square.square_second_way(side)
        self.assertEqual(result, expected_result)