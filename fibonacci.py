def fibonacci_sequence():
    num = 'i'
    while not num.isdigit():
        num = input("How many terms of the Fibonacci sequence would you like to list? ")
        if num.isdigit():
            num = int(num)
            break
        else:
            print("Please provide a positive integer")

    if num == 0:
        fib_sequence = []
    elif num == 1:
        fib_sequence = [0]
    else:
        fib_sequence = [0, 1]
        for _ in range(2, num):
            next_term = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_term)

    print("Fibonacci sequence up to", num, "terms:")
    print(fib_sequence)


if __name__ == '__main__':
    fibonacci_sequence()
