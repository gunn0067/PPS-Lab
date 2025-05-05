
# largest of three numbers.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

if (a > b and a > c):
    L = a
elif (b > c):
    L = b
else:
    L = c

print(f"Largest number: {L}")
