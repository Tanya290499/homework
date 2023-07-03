def nomenclature(first_list, second_list):
    result = []

    for i in range(len(first_list)):
        if first_list[i] not in second_list:
            result.append(first_list[i])
    return result

print(nomenclature([1, 2, 4, 'abc', 5], [1, 2, 20, 30]))
