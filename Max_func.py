def findMax(list):
    x=list[0]
    for i in list:
        if i>x:
            x=i
        else:
            continue

    return x

numList= [5,1,8,3,2]

max = findMax(numList)

print(f"Max number in {numList} is {max}")
