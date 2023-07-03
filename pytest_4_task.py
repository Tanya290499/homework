import pytest
from course.homework.fourth_task import Dictionary

class TestDictionary:
    @pytest.mark.parametrize('first_dictionary, second_dictionary, expected_result',
                             [({1: "Potatoes", 2: "Pasta", 3: "Rice"}, {4: "Meat", 5: "Chicken", 6: "Fish"},
                               {1: "Potatoes", 2: "Pasta", 3: "Rice", 4: "Meat", 5: "Chicken", 6: "Fish"})])
    def test_01_merging_dictionaries_first_way(self, first_dictionary, second_dictionary, expected_result):
        my_recipe = Dictionary()
        result = my_recipe.merging_dictionaries_first_way(first_dictionary, second_dictionary)
        assert result == expected_result

    @pytest.mark.parametrize('first_dictionary, second_dictionary, expected_result',
                             [({1: "Potatoes", 2: "Pasta", 3: "Rice"}, {4: "Meat", 5: "Chicken", 6: "Fish"},
                               {1: "Potatoes", 2: "Pasta", 3: "Rice", 4: "Meat", 5: "Chicken", 6: "Fish"})])
    def test_02_merging_dictionaries_second_way(self, first_dictionary, second_dictionary, expected_result):
        my_recipe = Dictionary()
        result = my_recipe.merging_dictionaries_second_way(first_dictionary, second_dictionary)
        assert result == expected_result