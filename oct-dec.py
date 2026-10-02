oct_num = input("Enter a number: ")
oct_reversed = oct_num[::-1]
power = 0
dec_num = 0
for digit in oct_reversed:

    x = int(digit) * (8**power)
    dec_num = dec_num + x
    power += 1

print(f"({oct_num})8 is equivalent to ({dec_num})10")
