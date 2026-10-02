numbers = [9,8,7,6,5,4,3,2,1,0]
reversed_list=[]
for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])

print(reversed_list)