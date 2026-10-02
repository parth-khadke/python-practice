while True:
    print("*** ASCII Value Finder ***")
    char=input("Enter a character: ")
    ascii_value=ord(char)
    print("The ASCII value of '{}' is: {}".format(char, ascii_value))
    print()
    if char.lower() == 'q':
        break