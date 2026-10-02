employees = {                                                                                                                                  
        101: {'name': 'Rahul', 'department': 'HR', 'incr_percent': 10, 'salary': 30000},                                                           
        102: {'name': 'Priya', 'department': 'IT', 'incr_percent': 15, 'salary': 75000},                                                           
        103: {'name': 'Amit', 'department': 'Sales', 'incr_percent': 12, 'salary': 45000},                                                         
        104: {'name': 'Neha', 'department': 'Finance', 'incr_percent': 8, 'salary': 60000},                                                        
        105: {'name': 'Vikas', 'department': 'IT', 'incr_percent': 20, 'salary': 90000},                                                           
        106: {'name': 'Ananya', 'department': 'HR', 'incr_percent': 7, 'salary': 35000},                                                           
        107: {'name': 'Rohan', 'department': 'Sales', 'incr_percent': 18, 'salary': 52000},                                                        
        108: {'name': 'Kavya', 'department': 'Finance', 'incr_percent': 14, 'salary': 68000},                                                      
        109: {'name': 'Suresh', 'department': 'IT', 'incr_percent': 12, 'salary': 82000},                                                          
        110: {'name': 'Meera', 'department': 'Sales', 'incr_percent': 10, 'salary': 40000},                                                        
        111: {'name': 'Rajesh', 'department': 'HR', 'incr_percent': 9, 'salary': 38000},                                                           
        112: {'name': 'Pooja', 'department': 'Finance', 'incr_percent': 11, 'salary': 71000},                                                      
        113: {'name': 'Deepak', 'department': 'IT', 'incr_percent': 16, 'salary': 95000},                                                          
        114: {'name': 'Sneha', 'department': 'Sales', 'incr_percent': 15, 'salary': 48000},                                                        
        115: {'name': 'Arjun', 'department': 'HR', 'incr_percent': 8, 'salary': 32000},                                                            
        116: {'name': 'Divya', 'department': 'Finance', 'incr_percent': 13, 'salary': 64000},                                                      
        117: {'name': 'Karan', 'department': 'IT', 'incr_percent': 17, 'salary': 88000},                                                           
        118: {'name': 'Ritu', 'department': 'Sales', 'incr_percent': 11, 'salary': 43000},                                                         
        119: {'name': 'Manoj', 'department': 'Finance', 'incr_percent': 9, 'salary': 58000},                                                       
        120: {'name': 'Shreya', 'department': 'IT', 'incr_percent': 19, 'salary': 102000}                                                          
    }

emp_HR = {}
emp_Sales = {}
emp_IT = {}
emp_Finance = {}



for eid, details in employees.items():
    salary = details["salary"]
    increment = details["incr_percent"]
    department = details["department"]
    if department == "IT":
        new_salary = salary + (salary * (increment/100))
        details["new_salary"] = new_salary
        emp_IT[eid]= details
    elif department == "HR":
        new_salary = salary + salary * (increment/100)

        details["new_salary"] = new_salary
        emp_HR[eid]= details
    elif department == "Sales":
        new_salary = salary + salary * (increment/100)

        details["new_salary"] = new_salary
        emp_Sales[eid] = details
    elif department == "Finance":
        new_salary = salary + salary * (increment/100)

        details["new_salary"] = new_salary
        emp_Finance[eid] = details

emp_IT.pop("incr_percent")
emp_IT.pop("salary")

emp_HR.pop("incr_percent")
emp_HR.pop("salary")

emp_Sales.pop("incr_percent")
emp_Sales.pop("salary")

emp_Finance.pop("incr_percent")
emp_Finance.pop("salary")


print(emp_IT)
# print()
# print(emp_Finance)
# print()
# print(emp_Sales)
# print()
# print(emp_HR)



