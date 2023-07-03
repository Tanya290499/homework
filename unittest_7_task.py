import unittest

from parameterized import parameterized

from course.homework.seventh_task import new_list_first_way, new_list_second_way


class TestNewList(unittest.TestCase):
    @parameterized.expand([([1, 20, 30, 45, 56, 66], [1, 66]), ([], [])])
    def test_01_element_search(self, something_list, expected_result):
        result = new_list_first_way(something_list)
        self.assertEqual(result, expected_result)

    @parameterized.expand([([1, 20, 30, 45, 56, 66], [1, 66]), ([1, 4, 7, 3], [1, 3])])
    def test_02_element_search(self, something_list, expected_result):
        result = new_list_second_way(something_list)
        self.assertEqual(result, expected_result)