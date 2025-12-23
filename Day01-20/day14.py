# 通过关键字def定义求阶乘的函数
# 自变量（参数）num是一个非负整数
# 因变量（返回值）是num的阶乘
def fac(num):
    result = 1
    for n in range(2, num + 1):
        result *= n
    return result


m = 8
n = 4
# 计算阶乘的时候不需要写重复的代码而是直接调用函数
# 调用函数的语法是在函数名后面跟上圆括号并传入参数
print(fac(m) // fac(n) // fac(m - n))


# def make_judgement(a, b, c):
#     return a + b > c and a + c > b and b + c > a
#
#
# print(make_judgement(1, 2, 3))  # False
# print(make_judgement(4, 5, 6))  # True


# /前面的参数是强制位置参数
# def make_judgement(a, b, c, /):
#     """判断三条边的长度能否构成三角形"""
#     return a + b > c and b + c > a and a + c > b


# 下面的代码会产生TypeError错误，错误信息提示“强制位置参数是不允许给出参数名的”
# TypeError: make_judgement() got some positional-only arguments passed as keyword arguments
# print(make_judgement(b=2, c=3, a=1))


# *后面的参数是命名关键字参数
def make_judgement(*, a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b


# 下面的代码会产生TypeError错误，错误信息提示“函数没有位置参数但却给了3个位置参数”
# TypeError: make_judgement() takes 0 positional arguments but 3 were given
# print(make_judgement(1, 2, 3))


# 默认参数
# def add(a=0, b=0, c=0):
#     """三个数相加求和"""
#     return a + b + c
#


# 用星号表达式来表示args可以接收0个或任意多个参数
# 调用函数时传入的n个参数会组装成一个n元组赋给args
# 如果一个参数都没有传入，那么args会是一个空元组
def add(*args):
    total = 0
    for val in args:
        if type(val) in (int, float):
            total += val
    return total


# 在调用add函数时可以传入0个或任意多个参数
print(add())  # 0
print(add(1))  # 1
print(add(1, 2, 3))  # 6
print(add(1, 2, "hello", 3.45, 6))  # 12.45
