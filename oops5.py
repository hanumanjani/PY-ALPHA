class Employee:
    na = 8

    def printdetail(self):
        return f"Name is {self.name}"
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    @classmethod
    def change_no(cls,newno):
        cls.na = newno
    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])
    @staticmethod
    def printgood(string):
        print(f"this is good statement {string}")
        return 757
class programmer(Employee):
    def printprog(self):
        return f"name is {self.name} salory is {self.salary} and role is {self.role}"
    def __init__(self,name ,salory,role,weiht):
        self.name = name
        self.role=role
        self.salary =salory
        self.weight = weiht
    __pppp =1
    _hh =87845

emp = programmer("hfdgh",566,"dhfg",757)
# print(emp.programmer__pppp)
print(emp._hh)





karan = Employee.from_str("karan-6457-nonee")
print(karan.name)

