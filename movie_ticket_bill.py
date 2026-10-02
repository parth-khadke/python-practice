Customer_Name = input("Enter your name: ")
NumOf_Tickets = int(input("Required tickets: "))

Cost_per_ticket = 250

total_cost = NumOf_Tickets * Cost_per_ticket


GST = total_cost*0.18

payable_amt = total_cost+GST


print(f'''
************Movie Ticket Bill**************\n
Customer Name : \t {Customer_Name}\n
Number of Tickets : \t {NumOf_Tickets}\n
Cost :  {total_cost}\n
Payable amount with GST : {payable_amt}
''')