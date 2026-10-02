def square(n):
    return n * n

def sum_of_squares(lst):
    sum = 0
    for i in lst:
        sum += square(i)

    return sum

nums = [1,2,3,4]

sum = sum_of_squares(nums)

print(sum)

