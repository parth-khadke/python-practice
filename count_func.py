def countEvens(list):
    count=0
    for i in list:
        if i%2==0:
            count+=1
        else:
            continue
    
    return count

list_num = [1,2,3,4,5,6,7,8,10,13]

count=countEvens(list_num)
 
print(count)
