def new_list_first_way(something_list):
    if len(something_list) > 0:
        first_element = something_list[0]
        last_element = something_list[-1]
        result = [first_element, last_element]
        return result
    else:
        return []

def new_list_second_way(something_list):
    if len(something_list) > 0:
        return [something_list[0], something_list[-1]]
    else:
        return []
