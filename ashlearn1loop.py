class STUDENT:
    def __init__(self,rollno,name):
        print(self)
        self.rollno =rollno
        self.name = name

    def get_rollno(self):
        print(self.rollno)
    def get_name(self):
        print(self.name)

rahul = STUDENT(24,"rahul")
rahul.get_rollno()
rahul.get_name()

class Employee:
    def __init__(ash,empname,empid):
        print(ash)
        ash.empname = empname
        ash.empid = empid
    
    def get_empname(ash):
            print(ash.empname)
        
    def get_empid(ash):
            print(ash.empid)
    
    ashutosh = Employee("anish","1001")
    ashutosh.get_empname()
    ashutosh.get_empid()


