def search_replace(my_list, search, replace):
    if not my_list:
        return
    new = my_list.copy()
    for item in my_list:
        if my_list[item] == search:
            new[item] = replace
            return new
        else:
            return new
