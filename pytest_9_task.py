import pytest
from course.homework.ninth_task import even_numbers_first_way, even_numbers_second_way

class TestNewList:
    @pytest.mark.parametrize('length, expected_result', [([1, 2, 3, 4, 6, 237, 14], [2, 4, 6]), ([], [])])
    def test_01_even_numbers_first_way(self, length, expected_result):
        result = even_numbers_first_way(length)
        assert result == expected_result

    @pytest.mark.parametrize('length, expected_result', [([12, 12, 5, 237, 1, 2], [12, 12]), ([], [])])
    def test_02_element_search(self, length, expected_result):
        result = even_numbers_second_way(length)
        assert result == expected_result
