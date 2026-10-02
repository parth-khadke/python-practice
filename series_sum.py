n = int(input("Enter a number for the end of the series: "))
sum=0
other_sum=0
for i in range(1,n+1):
    sum += (i*i) // i

print("Sum of the series is ", sum)

