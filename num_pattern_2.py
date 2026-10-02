a="5"
b="7"
for i in range(1,7):
    for j in range(1,i):
        if j%2!=0:
            print(f"{a}"*j, end=" ")
        else:
            print(f"{b}"*j, end=" ")
    print("\n")


