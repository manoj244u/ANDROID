class Parent:
  parentAttr = 100
  def __init__(self):
    print (" calling parent class constructor")
  def parentmethod(self):
    print ("calling Paren method")
  def setattr(self, attr):
    Parent.parentAttr = attr
  def getatr(self):
    print ("parent attribute :", Parent.parentAttr)
class Child(Parent):
  def __init__(self):
    print ("calling child constructor")
  def childmethod(self):
    print ("calli child method")
  
c = Child()
c.childmethod()
c.parentmethod()
c.setattr(500)
c.getatr()
 