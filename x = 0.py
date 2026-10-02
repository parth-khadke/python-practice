n = 4
for i in range(n):
    for space in range(i):
        print(" ", end="")
    for star in range(2*(n - i) - 1):
        print("*", end="")
    print()
