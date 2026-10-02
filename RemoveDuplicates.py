'''
My solution

nums = [1,1,1,4,5,6,6,8,3,3,0]
fresh_nums = []
for i in nums:
    if i in fresh_nums:
        continue
    else:
        fresh_nums.append(i)

print(fresh_nums)
'''
## Chatgpt's solution. Uses set for hashing functionality which reduces lookup time for each value. My primary logic was correct.
## Required efficient time complexity practices and some implementation improvements

nums = [1,1,1,4,5,6,6,8,3,3,0]

seen = set()
result = []

for num in nums:
    if num not in seen:
        result.append(num)
        seen.add(num)

print(result)