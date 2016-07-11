class Employee:
  'common base class for all employees'
  empcount = 0
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.empcount += 1
  def displaycount(self):
    print ("total Employee %d" %E)
  def displayemployee(self):
    print ("name :", self.name, "salary", self.salary)

print ("Employee.__doc__", Employee.__doc__)
print ("Employee.__name__", Employee.__name__)
print ("Employee.__module__", Employee.__module__)
print ("Employee.__dict__", Employee.__dict__)
print ("employee.__base__", Employee.__base__ )   