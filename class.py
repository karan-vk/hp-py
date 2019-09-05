class Employee():
    empCount = 0

    def __init__(self, name, salary, did):
        self.name = name
        self.salary = salary
        self.did = did
        Employee.empCount += 1
     
    def displayEmployee(self):
        print (" Name : ", self.name,  ", Salary: ", self.salary,  ", Des: ", self.did)
    

emp1 = Employee("varma", 50000,"GM")
emp2 = Employee("josh", 25000,"AGM")
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)



