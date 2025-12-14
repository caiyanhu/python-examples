balance_str = "1500"
balance_int = int(balance_str)

print(type(balance_int))
print(balance_int)

balance_str = "1500.4"
balance_float = float(balance_str)
print(type(balance_float))
print(balance_float)

balance_str = "1500.34"
balance_int = int(float(balance_str))
print(type(balance_int))
print(balance_int)
