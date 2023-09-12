def count(func):
    numbers_of_calls = 0

    def decorated(*args, **kwargs):
        nonlocal numbers_of_calls
        numbers_of_calls += 1
        return func(*args, **kwargs), numbers_of_calls

    return decorated


@count
def some_function(n):
    return n


print(some_function('Me'))
print(some_function('You'))
print(some_function('He'))
print(some_function('She'))
print(some_function('Together we are a friendly family'))
