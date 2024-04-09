def prime_checker(num):

    if not num.isdigit():
        return False
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
        return "your number is prime"
    else:
        return "your number is not prime"
