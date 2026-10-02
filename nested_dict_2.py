employees = {                                                                                                                                  
        101: {'name': 'Rahul', 'basic_salary': 30000},                                                                                             
        102: {'name': 'Priya', 'basic_salary': 45000},                                                                                             
        103: {'name': 'Amit', 'basic_salary': 35000},                                                                                              
        104: {'name': 'Neha', 'basic_salary': 50000},                                                                                              
        105: {'name': 'Vikas', 'basic_salary': 28000},                                                                                             
        106: {'name': 'Ananya', 'basic_salary': 42000},                                                                                            
        107: {'name': 'Rohan', 'basic_salary': 38000},                                                                                             
        108: {'name': 'Kavya', 'basic_salary': 60000},                                                                                             
        109: {'name': 'Suresh', 'basic_salary': 32000},                                                                                            
        110: {'name': 'Meera', 'basic_salary': 48000}                                                                                              
    }

HRA_per = 10
DA_per = 8
TAX_per = 5
for eid, details in employees.items():
    base = details["basic_salary"]
    HRA = base* HRA_per/100
    DA = base* DA_per/100
    GS = base + HRA + DA 
    tax = base * TAX_per/100
    net_sal = GS - tax

    details.update({"HRA" : HRA, "DA": DA, "Gross": GS, "tax": tax, "net_sal": net_sal})

    employees[eid]= details 

print(employees)