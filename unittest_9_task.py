import unittest

from parameterized import parameterized

from course.homework.ninth_task import even_numbers_first_way, even_numbers_second_way


class TestNewList(unittest.TestCase):
    @parameterized.expand([([1, 20, 30, 45, 56, 66, 237, 2], [20, 30, 56, 66]), ([], [])])
    def test_01_even_numbers_first_way(self, length, expected_result):
        result = even_numbers_first_way(length)
        self.assertEqual(result, expected_result)

    @parameterized.expand([([1, 20, 30, 45, 56, 66, 237, 2], [20, 30, 56, 66]), ([], [])])
    def test_02_even_numbers_second_way(self, length, expected_result):
        result = even_numbers_second_way(length)
        self.assertEqual(result, expected_result)