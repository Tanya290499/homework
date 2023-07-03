import pytest
from course.homework.homework_29_06.task_10.tenth_task import nomenclature


class TestLists:
    @pytest.mark.parametrize('first_list, second_list, expected_result', [
        ([1, 2, 4, 'abc', 5], [1, 2, 20, 30], [4, 'abc', 5]),
        ([1, 2, 3], [], [1, 2, 3])
    ])
    def test_01_nomenclature(self, first_list, second_list, expected_result):
        result = nomenclature(first_list, second_list)
        assert result == expected_result
