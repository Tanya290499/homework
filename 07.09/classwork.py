import time


def fn(a):
    print(a, 'fn')
    print(locals())
    def inner():
        nonlocal a
        print(inner.__closure__)
        print(a, 'inner')
        a += 1
        print(locals())
    return inner

fn(5)
print('------------------------------------------')
def fn(a):
    def inner(x, y):
        nonlocal a
        print(inner.__closure__)
        print(a, x, y, 'params')
    return inner

some = fn(5)
print(some('x', 'y'))
some2 = fn([1, 2, 3])
print(some2('x', 'y'))
print(some('arg1', 'arg2'))
print(some2('xxx', 'yyy'))
print('------------------------------------------')


def fn(func):
    def inner(x):
        print(inner.__closure__)
        start = time.time()
        func(x)
        finish = time.time() - start
        print(finish)
    return inner

@fn

def decorated(n):
    time.sleep(n)
    return n

#decorated = fn(decorated)
print(decorated.__name__)
print(decorated(2))