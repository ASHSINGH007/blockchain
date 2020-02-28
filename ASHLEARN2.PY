class Employee:
    def __init__(self,empname,empid):
        print(self)
        self.empname = empname
        self.empid = empid
    
    def get_empname(self):
            print(self.empname)
        
    def get_empid(self):
            print(self.empid)
    
    ashutosh = Employee("anish","1001")
    ashutosh.get_empname()
    ashutosh.get_empid()

