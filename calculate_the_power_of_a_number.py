import math

base = 3
exponent = 4

result = 1

while exponent != 0:
    result *= base
    exponent -= 1
print("Answer =", result)

exponent = 4
result = 1
for i in range(exponent, 0, -1):
    result *= base
print("Answer =", result)


exponent = 4
result = pow(base, exponent)
print("Answer =", result)
