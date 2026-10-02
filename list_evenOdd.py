num_list= [12,54,33,5,65,8,37,55,23,46,27,98,36,50]

even_list=[]
odd_list=[]

for num in num_list:
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Original List : ", num_list)
print("Even list: ", even_list)
print("Odd list: ", odd_list)