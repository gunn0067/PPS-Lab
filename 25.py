

# Python program using a class named Complex to perform operations on complex numbers.


def __init__(self):
    self.real = 0
    self.imag = 0


def initComplex(self):
    self.real = int(input("Real Part: "))
    self.imag = int(input("Imaginary Part: "))


def display(self):
    print(f"{self.real}+{self.imag}i")


def sum(self, c1, c2):
    self.real = c1.real+c2.real
    self.imag = c1.imag + c2.imag
