# Take a list of numbers
my_list = [
    12,
    65,
    54,
    39,
    102,
    339,
    221,
]


def is_divisible_by_five(n):
    if n % 5 == 0:
        return True
    return False


result = list(filter(is_divisible_by_five, my_list))
print("Numbers divisible by 5 are:", result)
