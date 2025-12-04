def sum_of_digits(n):
    sum = 0
    strNum = str(n)
    length = len(strNum)

    for i in range(length):
        sum += int(strNum[i])

    return sum


print("the sum of digits of 12345 is", sum_of_digits(12345))
