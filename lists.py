list=[]
list=[1,2,11,12,13,3,4,6,7,8,9,14,]

for item in range(len(list)):
    print(list[item], end = " ")
print("")
print(sum(list))
print(max(list))
print(min(list))
list.sort(reverse=True)
print(list)


    
