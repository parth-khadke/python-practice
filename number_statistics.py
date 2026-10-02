def stats(numList):
    min_value = min(numList)
    max_value = max(numList)
    mean = sum(numList) / len(numList)

    sorted_list = sorted(numList)

    if len(sorted_list)%2 == 0:
        median = (sorted_list[(len(sorted_list)// 2) - 1] + sorted_list[(len(sorted_list)//2)]) / 2
    else:
        median = sorted_list[len(sorted_list)//2]

    largest = numList[0] 
    second_largest = numList[0]

    for i in numList:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest :
            second_largest = i

    frequency = {}

    for i in numList:

        if i in frequency:
            frequency[i] +=1
        else:
            frequency[i] = 1

    evenCount = 0 
    oddCount = 0

    for num in numList:
        if num % 2 == 0:
            evenCount +=1
        else:
            oddCount += 1 

    return min_value, max_value, mean, median, second_largest, frequency, evenCount, oddCount

num_list = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
sorted_list = sorted(num_list)
min_value, max_value, mean, median, second_largest, frequency, evenCount, oddCount = stats(num_list)

print("Minimum value: ", min_value)
print("Maximum value: ", max_value)
print("Mean: ", mean)
print("Median: ", median)
print("Second Largest Value: ", second_largest)
print("Frequency: ", frequency)
print("Even Number count: ", evenCount)
print("Odd Number count: ", oddCount)




        

    