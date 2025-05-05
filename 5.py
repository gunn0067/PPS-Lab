# Finding roots of Quadratic Equations


a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

D = b**2 - 4*a*c

if (D == 0):
    r = -b/(2*a)
    print(f"The root is: {r:.2f}")

elif (D > 0):
    r1 = (-b-D**0.5)/(2*a)
    r2 = (-b+D**0.5)/(2*a)
    print(f"The roots are: {r2:.2f} and {r1:.2f}")

else:
    real = -b/(2*a)
    imag = ((-D)**0.5)/(2*a)
    print(f"The roots are: {real:.2f}+{imag:.2f}j and {real:.2f}-{imag:.2f}j")
