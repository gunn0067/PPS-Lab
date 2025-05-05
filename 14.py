
# Python program that prompts the user to input three digits (0-9) and checks if the entered digits are valid.

d1 = int(input("digit1 (0-9): "))
d2 = int(input("digit2 (0-9): "))
d3 = int(input("digit3 (0-9): "))
a = [d1, d2, d3]


if (d1 > 9 or d2 > 9 or d3 > 9):
    print("Invalid")
else:
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                if (i != j and j != k and k != i):
                    print(f"{a[i]}{a[j]}{a[k]}")
