
# Python program that functions as a simple phone book manager with a menu-driven interface.

phone_book = {}
while True:
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Display")
    print("4. Quit")
    ch = input("Enter choice (1-4): ")

    if ch == "1":
        name = input("Name: ")
        phone = input("Phone number: ")
        phone_book[name] = phone

    elif ch == "2":
        name = input("Name: ")
        if name in phone_book:
            del phone_book[name]

        else:
            print("Not found")

    elif ch == "3":
        print(phone_book)

    elif ch == "4":
        break

    else:
        print("Invalid")
