def fibonacci_less_than(n):
    n1, n2 = 0, 1
    fib_sequence = []

    if n <= 0:
        return fib_sequence
    if n1 < n:
        fib_sequence.append(n1)
    if n2 < n:
        fib_sequence.append(n2)

    while True:
        next_term = n1 + n2
        if next_term >= n:
            break
        fib_sequence.append(next_term)
        n1, n2 = n2, next_term

    return fib_sequence


print(fibonacci_less_than(22))
