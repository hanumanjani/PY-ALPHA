class Employee:
    na = 8

    def printdetail(self):
        return f"Name is {self.name}"
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole


harry = Employee("harry",2536,"teacher")
harry.name = "harry"

larry = Employee("larry",556,"student")
larry.name = "Larry"
print(harry.printdetail())
