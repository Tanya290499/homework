import unittest

from parameterized import parameterized

from course.homework.sixth_task import sequence_of_list, sequence_of_tuple

class TestDictionary(unittest.TestCase):
    @parameterized.expand([('1, 2, 3, 4, 5', [1, 2, 3, 4, 5])])
    def test_01_sequence_of_list(self, string, expected_result):
        result = sequence_of_list(string)
        self.assertEqual(result, expected_result)

    @parameterized.expand([('1, 2, 3, 4, 6', (1, 2, 3, 4, 6))])
    def test_02_merging_dictionaries_second_way(self, string, expected_result):
        result = sequence_of_tuple(string)
        self.assertEqual(result, expected_result)