import pytest

from course.homework.second_task import List

class TestList:
    @pytest.mark.parametrize('a, b, expected_result', [([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 5, [1, 1, 2, 3]),
                                                        ([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 3, [1, 1, 2])
                                                       ])
    def test_01_second_task_first_way(self, a, b, expected_result):
        my_list = List()
        result = my_list.second_task_first_way(a, b)
        assert result == expected_result


    @pytest.mark.parametrize('a, b, expected_result', [([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 5, [1, 1, 2, 3]),
                                                       ([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 3, [1, 1, 2])
                                                       ])
    def test_02_second_task_second_way(self, a, b, expected_result):
        my_list = List()
        result = my_list.second_task_second_way(a, b)
        assert result == expected_result