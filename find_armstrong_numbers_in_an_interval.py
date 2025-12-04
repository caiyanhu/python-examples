def isArmStrongNumber(num):
    sum = 0
    str_num = str(num)
    length = len(str_num)

    for i in range(length):
        current = int(str_num[i]) ** length
        sum += current

    return sum == num


lower = 100
upper = 2000

for num in range(lower, upper + 1):
    if isArmStrongNumber(num):
        print(num)
