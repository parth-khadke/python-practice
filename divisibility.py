print("*** Divisibility By 10 Checker  ***")
number = int(input("Enter an integer: "))
if number % 10 == 0:
    print("{} is divisible by 10.".format(number))
else:
    print("{} is not divisible by 10.".format(number))
    rounding= 10-(number % 10)
    print("You need to add {} to make it divisible by 10.".format(rounding))
