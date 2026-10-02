list = list(map(int, input("Enter a number: ").split()))
x= list[0]
print("Entered List : ", list)

for i in list:
    if i > x:
        x = i
    
print(x)

