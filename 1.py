# Area of Circle


r = float(input("Enter the radius : "))

if (r >= 0.0 and r <= 100.0):
    print(f"Area of circle = {(3.14*r*r):.6f}\n")
else:
    print("Enter a positive value upto 100\n")
