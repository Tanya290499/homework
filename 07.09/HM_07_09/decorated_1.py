def decorated_data_type(datatype):
    print(datatype)

    def decorator(func):
        def change_type(*args):
            return datatype(func(*args))

        return change_type

    return decorator


@decorated_data_type(datatype=str)
def summ(first_number, second_number):
    result = first_number + second_number
    return result


print(summ(10, 100))
