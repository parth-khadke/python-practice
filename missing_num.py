nums = [11,12,13,15,16,18]

temp = nums[0]


print("Missing numbers")

# for i in range(len(nums)):
#     if nums[i] != temp:
#         print("Missing Number : ", temp)
#         temp += 1
#         i += 1
#     else: 
#         temp += 1

i = 0
while i < len(nums):
    if nums[i] != temp:
        print("Missing Number: ", temp)
        temp += 1
    else:
        temp += 1
        i += 1
