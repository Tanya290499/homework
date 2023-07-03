import unittest

from parameterized import parameterized

from course.homework.homework_29_06.task_8.eighth_task import get_extension


class TestNewList(unittest.TestCase):
    @parameterized.expand([('something.py', 'py'), ('file', 'the file has no extension')])
    def test_01_element_search(self, filename, expected_result):
        result = get_extension(filename)
        self.assertEqual(result, expected_result)