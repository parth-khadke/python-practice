for i in range(0,5):
    print("*", end="  ")

print("")
for k in range(0,3):
    for j in range(0,5):
        if j==0 or j==4:
            print("* ", end=" ")
        else:
            print("   ", end = "")
    print("")


for i in range(0,5):
    print("*", end="  ")