cost_price=int(input("Enter the cost price: "))
selling_price=int(input("ENter the selling price: "))

if cost_price > selling_price:
    loss= cost_price - selling_price
    print("Loss : ", loss)
elif selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit : ", profit)
elif cost_price == selling_price:
    print("Profit & Loss = 0")
