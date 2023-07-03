class Palindrome:
    def __init__(self):
        self.result = None

    def polydrome_search_first_way(self, string):
        return string == string[::-1]

    def polydrome_search_second_way(self, string):
        string = string.casefold()
        rev = reversed(string)
        return list(rev) == list(string)
