class Employee:
    def __init__(self,name, salary,dept,role):
        self.name=name
        self.salary=salary
        self.dept=dept
        self.role=role
    
    @property
    def setDept(self):
        return self.dept
    
    def setDept(self, newDept, modifiedRole):
        self.dept=newDept
        self.role=modifiedRole
    
    def getInfo(self):
        print(f"The name is {self.name}. The salary is {self.salary} and the dept is {self.dept} and {self.role}")


a=Employee("Subhankar", 114000, "IT","QA")
a.getInfo()
print ("-----------------------------------------")
a.dept="QEA"
a.role="SDET"
a.getInfo()