import re

my_string = " Python "
print(my_string.strip())

my_string = " \nPython "
print(my_string.strip(" "))

my_string = " Hello Python "
output = re.sub(r"^\s+|\s+$", "", my_string)
print(output)
