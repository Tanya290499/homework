import unittest

from course.homework.second_task import List

from parameterized import parameterized

class TestList(unittest.TestCase):
    @parameterized.expand([([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 5, [1, 1, 2, 3]),
                                                        ([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 3, [1, 1, 2])
                                                       ])
    def test_01_second_task_first_way(self, a, b, expected_result):
        my_list = List()
        result = my_list.second_task_first_way(a, b)
        self.assertEqual(result, expected_result)

    @parameterized.expand([([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 5, [1, 1, 2, 3]),
                           ([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 3, [1, 1, 2])
                           ])
    def test_02_second_task_second_way(self, a, b, expected_result):
        my_list = List()
        result = my_list.second_task_second_way(a, b)
        self.assertEqual(result, expected_result)