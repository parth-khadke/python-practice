print("*** SHopping Cart ***")
total=0
while True:
    item=input("Enter item name(enter 'done' to exit): ")
    if item=="done":
        break
    price=int(input("ENter price: "))
    
    if price<0:
        print("Invalid Price")
        continue
    total+=price

print("BILL")
print(f"Shopping cart total: {total}")

if total>100:
    total= total - (total*0.10)

print("Final Total with 10% discount: ", total)