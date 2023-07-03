def even_numbers_first_way(length):
    new_length = []
    for i in range(len(length)):
        if length[i] % 2 == 0 and length[i] != 237:
            new_length += [length[i]]
        else:
            if length[i] == 237:
                break
            else: continue
    return new_length

def even_numbers_second_way(length):
    new_length = []
    for i in range(len(length)):
        if length[i] == 237:
            break
        else:
            if length[i] % 2 == 0:
                new_length.append(length[i])

    return new_length

