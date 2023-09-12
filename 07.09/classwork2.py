def some_decorator_name(some_function):
    def worker(x, y):
        if y == 0:
            return 'ZeroDivisionError, division by 0 is unacceplable'
        x = abs(x)
        return some_function(x, y)
    return worker


@some_decorator_name #== division = worker
def division(x, y):
    return x/y
print(division(10, 20))