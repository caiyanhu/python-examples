from enum import Enum


class Day(Enum):
    MONDAY = 1
    TUSDAY = 2
    WENDESDAY = 3


print(Day.MONDAY)

print(Day.MONDAY.name)

print(Day.MONDAY.value)
