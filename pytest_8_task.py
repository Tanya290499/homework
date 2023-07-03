import pytest
from course.homework.eighth_task import get_extension

class TestNewList:
    @pytest.mark.parametrize('filename, expected_result', [('something.py', 'py'), ('file', 'the file has no extension')])
    def test_01_extension(self, filename, expected_result):
        result = get_extension(filename)
        assert result == expected_result

