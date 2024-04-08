import prime
import fibonacci


while 1 == 1:
    app = input("Please select an app (prime for prime checker, fib for Fibonacci Sequence list, quit to quit): ")
    if app.lower() == "prime":
        prime.prime_checker()
    elif app.lower() == "fib":
        fibonacci.fibonacci_sequence()
    elif app.lower() == "quit":
        break
    else:
        print("Invalid app")
