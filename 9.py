
# Python program to check if a given year is a leap year or not.


year = int(input("Enter a year: "))

if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
