m = int(input("Enter a positive number: "))
n = int(input("Enter a positive number: "))

if m<=n:
    for i in range(1,n):
        if i%m==0:
            print(i)
            i+=1
else:
    print("Try again.")