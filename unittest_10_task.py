import unittest

from parameterized import parameterized

from course.homework.tenth_task import nomenclature


class TestNewList(unittest.TestCase):
    @parameterized.expand([
        ([1, 2, 4, 'abc', 5], [1, 2, 20, 30], [4, 'abc', 5]),
        ([1, 2, 4, 'abc', 5], [], [1, 2, 4, 'abc', 5]),
    ])
    def test_01_nomenclature(self, first_list, second_list, expected_result):
        result = nomenclature(first_list, second_list)
        self.assertEqual(result, expected_result)
