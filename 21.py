

# program to print the sum of digits of a number.


num = int(input("num: "))
sum = 0

while (num != 0):
    digit = num % 10
    sum += digit
    num = num//10

print("sum:", sum)
