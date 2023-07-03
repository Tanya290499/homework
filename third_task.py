class Lists:

    def __init__(self):
        self.result = []

    def third_task_first_way(self, list_one, list_two):
        self.result = list_one + list_two
        return self.result

    def third_task_another_way(self, list_one, list_two):
        for i in list_one:
            for j in list_two:
                if i == j:
                    self.result.append(i)
                    break
        return self.result



