import pytest
from course.homework.homework_29_06.task_7.seventh_task import new_list_first_way, new_list_second_way

class TestNewList:
    @pytest.mark.parametrize('something_list, expected_result', [([1, 20, 30, 45, 56, 66], [1, 66]), ([], [])])
    def test_01_element_search(self, something_list, expected_result):
        result = new_list_first_way(something_list)
        assert result == expected_result

    @pytest.mark.parametrize('something_list, expected_result', [([1, 20, 30, 45, 56, 66], [1, 66]), ([1, 4, 7, 3], [1, 3])])
    def test_02_element_search(self, something_list, expected_result):
        result = new_list_second_way(something_list)
        assert result == expected_result