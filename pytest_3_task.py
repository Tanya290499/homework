import pytest
from course.homework.third_task import Lists

class TestLists:
    @pytest.mark.parametrize('list_one, list_two, expected_result',
                             [([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                            [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
                                 ([0, 1, 2], [3, 4], [0, 1, 2, 3, 4])])
    def test_01_third_task_first_way(self, list_one, list_two, expected_result):
        something_list = Lists()
        result = something_list.third_task_first_way(list_one, list_two)
        assert result == expected_result

    @pytest.mark.parametrize('list_one, list_two, expected_result',
                             [([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
                               [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                               [1, 1, 2, 3, 5, 8, 13])
                              ])
    def test_02_third_task_another_way(self, list_one, list_two, expected_result):
        something_list = Lists()
        list_one = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        list_two = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        expected_result = [1, 1, 2, 3, 5, 8, 13]
        result = something_list.third_task_another_way(list_one, list_two)
        assert result == expected_result