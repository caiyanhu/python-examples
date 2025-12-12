my_list = [[1], [2, 3], [4, 5, 6, 7]]

flatten_list = [num for sub_list in my_list for num in sub_list]
print(flatten_list)
