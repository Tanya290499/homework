class Dictionary:
    def __init__(self):
        self.result = {}

    def merging_dictionaries_first_way(self, first_dictionary, second_dictionary):
        self.result = {**first_dictionary, **second_dictionary}
        return self.result

    def merging_dictionaries_second_way(self, first_dictionary, second_dictionary):
        self.result = first_dictionary | second_dictionary
        return self.result



