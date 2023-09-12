def decorated_dev(f):
    def decorator(a, b):
        try:
            return f(a, b)
        except Exception as e:
            print(e)

    return decorator


@decorated_dev
def dev(a, b):
    return a / b


print(dev(-1, 0))
