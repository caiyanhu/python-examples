num = int(input("Enter a number: "))

sum = 0
str_num = str(num)
len = len(str_num)

for i in range(len):
    current = int(str_num[i]) ** len
    sum += current

if sum == num:
    print(num, "is an armstrong number")
else:
    print(num, "is not an armstrong number")
