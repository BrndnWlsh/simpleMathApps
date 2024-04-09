def fibonacci_sequence(num):
    if not num.isdigit():
        return False
    num = int(num)
    if num == 0:
        fib_sequence = []
    elif num == 1:
        fib_sequence = [0]
    else:
        fib_sequence = [0, 1]
        for _ in range(2, num):
            next_term = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_term)

    return f"Fibonacci sequence up to {num} terms: {fib_sequence}"
