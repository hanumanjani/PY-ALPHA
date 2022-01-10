class Employee:
    na = 8
    pass

harry = Employee()
harry.name = "harry"

larry = Employee()
larry.name = "Larry"
print(larry.name, harry.name)
print(harry.na)
harry.na = 5
print(harry.na, larry.na, Employee.na)
print(harry.__dict__)
print(Employee.__dict__)
print(larry.__dict__)