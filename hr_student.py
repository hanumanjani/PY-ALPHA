class Student1:
    """
    this is a student of nitr
    NATIONAL INSTITUTE OF TECHNOLOGY
    """
    batch = 2020
    role = "student"
    target = "scientst/engineer"

    def __init__(self,name,rollno,department):
        self.name =name
        self.rollno = f"420{department}{str(rollno)}"
        self.department = department
    @classmethod
    def batchchange(cls,year):
        batch = year
        return batch
    @staticmethod
    def note_some(wordss):
        print(f"you want to say :{wordss}")
    def print_info(self):
        print(self.name)
        print(self.department)
        print(self.rollno)

class Student2(Student1):
    batch = 2021
    def __init__(self,name,rollno,department):
        self.name =name
        self.rollno = f"421{department}{str(rollno)}"
        self.department = department

rohan = Student2("Rohan",4542,"CY")
rohan.print_info()

# print(rohan.__doc__)             -----------------> NONE


hari = Student1("HARI",5643,"CY")
hari.print_info()
l = hari.__doc__
print(l)
