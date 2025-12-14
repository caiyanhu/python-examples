def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


print(is_float("s12"))
print(is_float("1.23"))
