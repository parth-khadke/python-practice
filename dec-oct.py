dec_num = int(input("Enter a decimal number: "))
x = dec_num
quo = 1
oct_num=""
while(quo != 0):
    quo = x//8
    remainder=str(x%8)
    x = quo
    oct_num = oct_num + remainder

oct_num = oct_num[::]

print(f"({dec_num})10 is equivalent to ({oct_num})8.")