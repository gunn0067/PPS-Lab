# python program to define a module to find Fibonacci Numbers and import the module to another program.
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a+b

    return sequence


n = int(input("Enter the max value: "))

if n > 0:
    result = fibonacci(n)
    print(f"Fibonacci series upto {n} :")
    for i in result:
        print(i, end=" ")
    print()

else:
    print("Please enter a positive integer")
