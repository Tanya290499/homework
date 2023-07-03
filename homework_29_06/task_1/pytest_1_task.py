import pytest

from course.homework.homework_29_06.task_1.first_task import Square

class TestSquare:
    @pytest.mark.parametrize('side, expected_result', [(16, [64, 256, 4]), (0, [0, 0, 0])])
    def test_01_square_first_way(self, side, expected_result):
        square = Square()
        result = square.square_first_way(side)
        assert result == expected_result

    @pytest.mark.parametrize('side, expected_result', [(16, [64, 256, 4]), (0, [0, 0, 0])])
    def test_02_square_second_way(self, side, expected_result):
        square = Square()
        result = square.square_second_way(side)
        assert result == expected_result
