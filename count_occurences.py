number_list = list(map(int, input("Enter a list of integers:").split()))

number = int(input("Enter the number to check occurences : "))

counter=0
for i in number_list:
    if i==number:
        counter += 1
    
print(f"{number} occurs {counter} times in the given list. ")