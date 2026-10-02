list_1= [1,2,3,4]
list_2= [3,4,5,6]
list_int=[]
for num in list_1:
    if num in list_2:
        list_int.append(num)
    else:
        continue

print(list_int)
