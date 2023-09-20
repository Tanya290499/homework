from functools import reduce


def fn_reduce(a, b):
    return a * b


class Calculator:
    MODEL = 'CITIZEN'        #Статический атрибут


    def __init__(self, seria):
        self._seria = seria           #атрибут экземпляра класса
        self._result = None
        self.mem = None

    def memory(self):                      #функция которая определяется в области видимости класса
        self.mem = self._result

    def get_memory(self):
        return self.mem

    def clear_mem(self):
        self.mem = None

    def clear(self):
        self._result = None

    @property                              #
    def result(self):
        print(self._result)
        return self._result
    @result.setter
    def result(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self._result = value
        else:
            raise TypeError('Result is always number')

    def sum(self, *args):
        try:
            self.result = sum(args)
            self.result
        except TypeError as exc:
            print('***Only numbers allowed*** \n', exc)
        return self
    def multiply(self, *args):
        try:
            res = reduce(lambda x, y: x * y, args)
            self.result = res
        except TypeError:
            self.clear()
            print('Only Numbers for multiply')
        self.result
        return self

c = Calculator(seria='38638266')

c.sum(1, 2, 3).memory()
print(c.mem, 'mem')
c.multiply(2, 2, 3).sum(c.get_memory(), c.result)
