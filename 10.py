
# Python program to calculate the average marks for 5 subjects.


s1 = float(input("subject 1: "))
s2 = float(input("subject 2: "))
s3 = float(input("subject 3: "))
s4 = float(input("subject 4: "))
s5 = float(input("subject 5: "))

avg = (s1+s2+s3+s4+s5)/5.0
print(f"Average Marks: {avg:.2f}")

if avg >= 90:
    print("Grade: A")
elif avg >= 80 and avg <= 89:
    print("Grade: B")
elif avg >= 70 and avg <= 79:
    print("Grade: C")
elif avg >= 60 and avg <= 69:
    print("Grade: D")
else:
    print("Grade: F")
