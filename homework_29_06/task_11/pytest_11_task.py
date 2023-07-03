import pytest
from course.homework.homework_29_06.task_11.eleventh_task import directory


class TestLists:
    @pytest.mark.parametrize('dirname, expected_result', [
        ('/Users/tanya/Desktop/python/1/course', ['classwork 27.04.23.py', '.DS_Store', 'classwork.py', 'another_circle.py', '.pytest_cache', 'new and init.py', 'methods.py', 'circle.py', 'newcalkengine.py', 'unuttest10806.py', 'testCalcEngine.py', 'recipeтренировочное.py', 'database.py', '01.06 classwork.py', '__pycache__', 'container.py', 'point.py', 'classmetods.py', 'homework', 'CalcEngine.py', 'example-class.py', '25.05 задача.py', 'homeworkclasses.py', 'Accointing08_06.py', 'AccountingEngine.py', 'newversion222.py']),
    ])
    def test_01_directory(self, dirname, expected_result):
        result = directory(dirname)
        assert result == expected_result
