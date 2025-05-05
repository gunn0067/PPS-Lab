
# python program to print factorial of given number.


n = int(input("Enter a number : "))
if (n >= 0):
    fact = 1
    for i in range(1, n+1, 1):
        fact *= i

    print("Factorial of given number is :", fact)

else:
    print("Enter a positive number")
