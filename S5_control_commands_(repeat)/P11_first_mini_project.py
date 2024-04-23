while True:
    print("Choose your option: \n\t1)Encrypt\n\t2)Decrypt\n\t3)Exit")
    choice = input("Your choice : ")
    if choice == "1":
        plain_text = input("text : ")
        encrypted_text = ""

        for ch in plain_text:
            x = ord(ch) * 2 + 5
            encrypted_text += chr(x)

        print("Encrypted Text : ", encrypted_text)
        print("_" * 40 + "\n")

    elif choice == "2":
        encrypted_text = input("Encrypted Text : ")
        plain_text = ""

        for ch in encrypted_text:
            x = (ord(ch) - 5) // 2
            plain_text += chr(x)

        print("Plain Text: ", plain_text)
        print("_" * 40 + "\n")

    elif choice == "3":

        print("Good Bye!")
        print("_" * 40 + "\n")
        break

    else:

        print("Your choice is wrong!")
        print("_" * 40 + "\n")
