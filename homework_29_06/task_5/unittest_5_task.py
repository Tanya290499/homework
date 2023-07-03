import unittest
from course.homework.homework_29_06.task_5.fifth_task import Palindrome

from parameterized import parameterized

class TestDictionary(unittest.TestCase):
    @parameterized.expand([('121', True), ('12123', False)])
    def test_01_merging_dictionaries_first_way(self, string, expected_result):
        my_string = Palindrome()
        result = my_string.polydrome_search_first_way(string)
        self.assertEqual(result, expected_result)

    @parameterized.expand([('121', True), ('12123', False)])
    def test_02_merging_dictionaries_second_way(self, string, expected_result):
        my_string = Palindrome()
        result = my_string.polydrome_search_second_way(string)
        self.assertEqual(result, expected_result)