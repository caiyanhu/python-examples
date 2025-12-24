import random
import string

ALL_CHARS = string.digits + string.ascii_letters


def generate_code(*, code_len=10):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码字符串
    """
    return "".join(random.choices(ALL_CHARS, k=code_len))


for _ in range(5):
    print(generate_code(code_len=8))


def is_prime(n: int) -> bool:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(x: int, y: int) -> int:
    while y % x != 0:
        x, y = y % x, x
    return x


def lcm(x: int, y: int) -> int:
    return x * y // gcd(x, y)


def describe(data):
    """输出描述性统计信息"""
    print(f"均值: {mean(data)}")
    print(f"中位数: {median(data)}")
    print(f"极差: {ptp(data)}")
    print(f"方差: {var(data)}")
    print(f"标准差: {std(data)}")
    print(f"变异系数: {cv(data)}")


def mean(data):
    return sum(data) / len(data)


def median(data):
    temp, size = sorted(data), len(data)
    if size % 2 != 0:
        return temp[size // 2]
    else:
        return mean(temp[size // 2 - 1 : size // 2 + 1])


def ptp(data):
    return max(data) - min(data)


def var(data, ddof=1):
    x_bar = mean(data)
    temp = [(num - x_bar) ** 0.5 for num in data]
    return sum(temp) / (len(temp) - ddof)


def std(data, ddof=1):
    return var(data, ddof) ** 0.5


def cv(data, ddof=1):
    return std(data, ddof) / mean(data)
