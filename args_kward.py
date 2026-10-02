def add(*numbers):
    sum = 0 
    for num in numbers:
        sum += num
    return sum

nums = [45, 50]
print(add(*nums))

def percent(**test_marks):
    obt = 0
    for marks in test_marks.values():
        obt += marks

    total = len(test_marks) * 100
    per = obt/total *100
    return per

marks = {"t1" : 70, "t2" : 80, "t3": 90}
print(percent(**marks))

# pass *args and **kwargs together

try:
    pass
except Exception as e:
    raise
else:
    pass
finally:
    pass

