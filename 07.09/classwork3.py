import sys
sys.setrecursionlimit(999999999)
def fn(x):
    if x == 1:
        return 1
    return x * fn(x - 1)
res = fn(5)
print(res)
