
class List:
    def __init__(self):
        self.result = []
    def second_task_first_way(self, a, b):
        for i in range(len(a)):
            if a[i] < b:
                self.result.append(a[i])
        return self.result

    def second_task_second_way(self, a, b):
        for i in range(len(a)):
            if a[i] < b:
                self.result += [a[i]]
        return self.result




