class Employee:

    def __init__(self, id, name, sal):
        self.emp_id = id
        self.emp_name = name
        self.emp_salary = sal

    def display_emp_details(self):
        print("---- Employee Details ----")
        print("Emp. ID : ", self.emp_id)
        print("Emp. Name : ", self.emp_name)
        print("Salary : ₹", self.emp_salary)

    def calculate_salary(self):
        print("Base Salary : ₹", self.emp_salary)

class Manager(Employee):
    def __init__(self, id, name, sal, bonus):
        super().__init__(id, name, sal)
        self.bonus = bonus

    def calculate_total_salary(self):
        total_salary = self.emp_salary + self.bonus
        print(f"Total Salary : ₹{total_salary} (including Bonus : ₹{self.bonus})")

emp = Manager(101, "Parth", 75000, 5000)
emp.display_emp_details()
emp.calculate_salary()
emp.calculate_total_salary()