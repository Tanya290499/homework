import unittest
from course.homework.fourth_task import Dictionary
from parameterized import parameterized

class TestDictionary(unittest.TestCase):
    @parameterized.expand([({1: "Potatoes", 2: "Pasta", 3: "Rice"}, {4: "Meat", 5: "Chicken", 6: "Fish"},
                               {1: "Potatoes", 2: "Pasta", 3: "Rice", 4: "Meat", 5: "Chicken", 6: "Fish"})])
    def test_01_merging_dictionaries_first_way(self, first_dictionary, second_dictionary, expected_result):
        my_recipe = Dictionary()
        first_dictionary = {1: "Potatoes", 2: "Pasta", 3: "Rice"}
        second_dictionary = {4: "Meat", 5: "Chicken", 6: "Fish"}
        expected_result = {1: "Potatoes", 2: "Pasta", 3: "Rice", 4: "Meat", 5: "Chicken", 6: "Fish"}
        result = my_recipe.merging_dictionaries_first_way(first_dictionary, second_dictionary)
        self.assertEqual(result, expected_result)

    @parameterized.expand([({1: "Potatoes", 2: "Pasta", 3: "Rice"}, {4: "Meat", 5: "Chicken", 6: "Fish"},
                               {1: "Potatoes", 2: "Pasta", 3: "Rice", 4: "Meat", 5: "Chicken", 6: "Fish"})])
    def test_02_merging_dictionaries_second_way(self, first_dictionary, second_dictionary, expected_result):
        my_recipe = Dictionary()
        result = my_recipe.merging_dictionaries_second_way(first_dictionary, second_dictionary)
        self.assertEqual(result, expected_result)