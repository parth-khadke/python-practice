
    

class Student:

    institute = "The Kiran Academy" # \\\\\\
    course = "Python Full Stack"    # ------ Class level attributes
    Trainer = "Vaibhav Sir"         # //////

    def __init__(self, rl, nm, ag): #constructor for initializing object level attributes. 
        self.rollno = rl
        self.name = nm
        self.age = ag
        self.marks = {}

    def showDetails(self):
        details = f"Roll No: {self.rollno} \nName : {self.name} \nAge : {self.age} \n "
        print(details)

    def Add_marks(self, test, marks):
        self.marks[test] = marks
        print("added")

    def calc_perc(self):
        obt = 0 
        for i in self.marks.values():
            obt += i
        total = len(self.marks) * 100

        percent = obt / total * 100

        return percent
            


s1 = Student(101, "Parth", 21)


s2 = Student(102, "Rahul", 22)
s2.Add_marks("Maths", 80)
s2.Add_marks("English", 94)
s2.Add_marks("Science", 87)

s2.showDetails()
print(s2.calc_perc())



