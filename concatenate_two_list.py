# using + operation
list_1 = [1, "a"]
list_2 = [3, 4, 5]
list_joined = list_1 + list_2
print(list_joined)

# using iterable unpacking operator *
list_1 = [1, "a"]
list_2 = range(2, 4)
list_joined = [*list_1, *list_2]
print(list_joined)

# with unique values
list_1 = [1, "a"]
list_2 = [1, 2, 3]
list_joined = list(set(list_1 + list_2))
print(list_joined)

list_1 = [1, 3, 5]
list_2 = [2, 5, 7]


def merge_sorted_list(lst1, lst2):
    return list(set(list_1 + list_2))


print(merge_sorted_list(list_1, list_2))
