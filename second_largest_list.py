num_list= [12,54,33,5,8,37,55,23,46,27,98,36,50,101]

num=num_list[0]
largest = num
second_largest = num

for num in num_list:
    if num > largest:
        second_largest=largest
        largest=num
    elif num> second_largest and num!= largest:
        second_largest = num

print(num_list)
print(second_largest)
