import pytest
from course.homework.homework_29_06.task_6.sixth_task import sequence_of_list, sequence_of_tuple

class TestDictionary:
    @pytest.mark.parametrize('string, expected_result', [('1, 2, 3, 4, 5', [1, 2, 3, 4, 5])])
    def test_01_sequence_of_list(self, string, expected_result):
        result = sequence_of_list(string)
        assert result == expected_result

    @pytest.mark.parametrize('string, expected_result', [('1, 2, 3, 4, 6', (1, 2, 3, 4, 6))])
    def test_02_merging_dictionaries_second_way(self, string, expected_result):
        result = sequence_of_tuple(string)
        assert result == expected_result