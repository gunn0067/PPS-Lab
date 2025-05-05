
# Python program that prints prime numbers less than n which represents the upper limit.


def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, n, 1):
        if (n % i == 0):
            return False
    return True


ul = int(input("Enter upper limit: "))

for n in range(2, ul+1):
    if isPrime(n):
        print(n)
