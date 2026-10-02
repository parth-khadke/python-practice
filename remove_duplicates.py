def remove_duplicates(list):
    j=0

    while j < len(list):
        x = list[j]
        i = j+1
        while i < len(list):
            if x == list[i]:
                list.pop(i)
            else:
                i += 1
        j+=1
    return list
        
        

num = [1,1,2,2,3,3,1,4,3,2]

List = remove_duplicates(num)

print(List)

