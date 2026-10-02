
size = int(input("Enter size of the chessboard: "))

for k in range (size//2):
    for i in range (size//2):
        print(" \u25A0", end=" ")
        print("\u2610", end=" ")

    print()

    for j in range (size//2):
        print("\u2610", end=" ")
        print(" \u25A0", end=" ")

    print()