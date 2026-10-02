""" x=int(input("Enter a number: "))
if x%2== 0:
    print("even number.")
else:
    print("odd number.") """
""" 
num = eval(input("Enter a number"))

if num> 50 :
    print(f"{num} is greater than 50" )
else:
    print(f"{num} is less than 50")

print("Thank you!!!") """


""" 
num = eval(input("Enter a num : "))
if num > 0:
    print(f"{num} is a positive number")
elif num<0:
    print(f"{num} is a negative number")
else:
    print(f"{num} is zero")
     """
""" 
roll = [1,2,3,4]
name = ["ajay", 'rahul', 'pranav']

for rl in roll:
    print(rl)

for name in name:
    print(name)
 """


# WAP to iterate only negative numbers
# nums = [1,-2,-3,4,5,6,-7,8,9,-10]

# for num in nums:
#     if num <0:
#         print(num)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# for i in numbers:
#     if i % 2 != 0:
#         print(i)

# numb = [10,54,60,43,91,11,24,50]

# for num in numb:
#     if num > 50:
#         print(f"{num} is greater than 50")
#     else:
#         print(f"{num} is less than 50")



# students = ["rajesh", "pavan", "rajeev"]

# print(students[1])
# name =students[-1]
# print(name)

# nums = [10,20,30,40,50,60,70,80,90]

# print(nums[0:4])
# print(nums[::-1]) 

courses = ["py", "jv", "web dev", "DS", "DA", "ML"]

print(courses[-2])
print(courses[0:5:2])
print(courses[-1:])