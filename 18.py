
# Python program to find whether a given string is a palindrome or not.

s = input()
reversed_s = s[::-1]

if (s == reversed_s):
    print("palindrome")
else:
    print("not a palindrome")
