n1 = eval(input("Enter A Number : "))
n2 = eval(input("Enter A Number : "))

try:
    div = n1//n2
except ArithmeticError as e:
    print("cannot divide by zer0")
except TypeError as f:
    print('cannot divide by string')
else:
    print("div", div)
finally:
    print('the end')