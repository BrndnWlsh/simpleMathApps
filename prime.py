def prime_checker():
    loop = 1
    while loop == loop:
        num = input("provide a number: ")

        if not num.isdigit():
            print("Please provide a valid positive integer.")
        else:
            break
    num = int(num)
    if num <= 1:
        prime = False
    else:
        prime = True
        for n in range(2, int(num)):
            prime = int(num) % n != 0
            if not prime:
                break

    if prime:
        print("your number is prime")
    else:
        print("your number is not prime")


if __name__ == '__main__':
    prime_checker()
