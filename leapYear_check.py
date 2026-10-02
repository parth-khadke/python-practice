year = int(input("ENter year"))

if (year%4==0) & year%100!=0 & year%400 ==0:
    print("Year is leap")
else:
    print("Year is not leap")
    