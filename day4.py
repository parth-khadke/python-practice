# Day 4 - 


""" 
#  WAP - To print the name of students who have passed. marks >= 40.
result = {'Saniya': 89, 'Anushka': 78, 'Rutuja': 34, 'Adarsh': 31, 'Parth': 99}
passed = []
failed = []
for name, marks in result.items(): # .items() accesses both keys and values. if used with 1 loop variable -> return tuples
    if marks>=40:
        passed.append(name)
    else:
        failed.append(name)
    

print(passed)
print(failed)

 """


""" 
# WAP - to calculate the selling price of the products and save them in a new nested dictionary.
products = {                                                                                                                                   
        101: {                                                                                                                                     
            "pname": "4K Ultra HD Smart TV 55-inch",                                                                                               
            "category": "Electronics",                                                                                                             
            "mrp": 48999                                                                                                                           
        },                                                                                                                                         
        102: {                                                                                                                                     
            "pname": "Ergonomic Mesh Executive Chair",                                                                                             
            "category": "Furniture",                                                                                                               
            "mrp": 14500                                                                                                                           
        },                                                                                                                                         
        103: {                                                                                                                                     
            "pname": "Designer Leather Jacket",                                                                                                    
            "category": "Fashion",                                                                                                                 
            "mrp": 12999                                                                                                                           
        },                                                                                                                                         
        104: {                                                                                                                                     
            "pname": "Gaming Laptop (16GB RAM / 1TB SSD)",                                                                                         
            "category": "Electronics",                                                                                                             
            "mrp": 85000                                                                                                                           
        },                                                                                                                                         
        105: {                                                                                                                                     
            "pname": "Solid Teak Wood 6-Seater Dining Table",                                                                                      
            "category": "Furniture",                                                                                                               
            "mrp": 42000                                                                                                                           
        },                                                                                                                                         
        106: {                                                                                                                                     
            "pname": "Luxury Chronograph Wristwatch",                                                                                              
            "category": "Fashion",                                                                                                                 
            "mrp": 25500                                                                                                                           
        },                                                                                                                                         
        107: {                                                                                                                                     
            "pname": "Mirrorless Digital Camera with Kit Lens",                                                                                    
            "category": "Electronics",                                                                                                             
            "mrp": 62990                                                                                                                           
        },                                                                                                                                         
        108: {                                                                                                                                     
            "pname": "3-Seater Fabric Recliner Sofa",                                                                                              
            "category": "Furniture",                                                                                                               
            "mrp": 38999                                                                                                                           
        },                                                                                                                                         
        109: {                                                                                                                                     
            "pname": "Tailored Italian Wool Suit",                                                                                                 
            "category": "Fashion",                                                                                                                 
            "mrp": 18500                                                                                                                           
        },                                                                                                                                         
        110: {                                                                                                                                     
            "pname": "King Size Bed with Hydraulic Storage",                                                                                       
            "category": "Furniture",                                                                                                               
            "mrp": 34990                                                                                                                           
        }                                                                                                                                          
    }

products_sp = {}
for pid, details in products.items():
    mrp = details["mrp"]
    cat = details["category"]

    if cat =="Electronics":
        sp = mrp - mrp * 20/100
        details['disc%'] = 20
    elif cat == "Fashion":
        sp = mrp - mrp * 10/100
        details['disc%'] = 10
    elif cat == "Furniture":
        sp = mrp - mrp * 5/100
        details['disc%'] = 5
    else:
        sp = mrp 

    details['sell_price'] = sp
    details.pop('mrp')
    products_sp[pid] = details

print(products_sp)

 """        

# WAP - 

