def name():
    return "John", "Armin"


print(name())
name_1, name_2 = name()
print(name_1, name_2)


def another_name():
    n1 = "John"
    n2 = "Armin"
    return {1: n1, 2: n2}


names = another_name()
print(names)
