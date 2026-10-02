product_mrp = [10000,20000, 30000, 5000, 6000, 14000, 8000 ]
sell_price = []
disc = 0
for i in product_mrp:
    if i >= 15000:
        disc = 15
        sp = i - (i * (disc/100))
        sell_price.append(sp)
    elif i >= 10000:
        disc = 10
        sp = i - (i * (disc/100))
        sell_price.append(sp)
    elif i >= 5000:
        disc = 5
        sp = i - (i * (disc/100))
        sell_price.append(sp) 
    else:
        disc = 0 
        sp = i
        sell_price.append(i)

print(sell_price)  
     
