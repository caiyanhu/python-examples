old_nums = [35, 12, 8, 99, 60, 52]

new_nums = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, old_nums)))
print(new_nums)
