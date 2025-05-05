

# Python program that takes a sentence as input, removes punctuations from the sentence, and displays the modified sentence.


s = input()
result = ""
for c in s:
    if c.isalnum() or c.isspace():
        result += c


print(result)
