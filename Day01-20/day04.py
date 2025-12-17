"""
输入半径计算圆的周长和面积
"""

import math

radius = float(input("输入圆的半径:"))
perimeter = 2 * math.pi * radius
area = math.pi * radius**2

print(f"{perimeter = :.2f}")
print(f"{area = :.2f}")

"""
输入年份，闰年输出True，平年输出False
"""
year = int(input("输入年份:"))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(f"{is_leap = }")
