#  To map with real world scenarious we started using object in code this is called object oriented programming 
# class is a blueprint(featrue of object) for creating object 
class student: # creating class
     name="ali"
   #creating object (instance)
s1=student()
print(s1.name)
# class car:
#     color="blue"
#     brand="mercedes"

# car1 = car()
# print(car1.color)
# print(car1.brand)
#  Constructor : All class have a function called -int-(),which is always execute when the object is being initiated 
#  # creating class
#    name="ali"
#  class student:  def __init__(self): Default constructor 
#     print("adding a new student in database..")
# # creating object (instance)
# s1=student()
# print(s1)
# #print(s1.name)
# class student:
#      def __init__(self,fullname,marks):# self parameter is a reference to the current  this consttructor is called parametise constructor 
#       self.name=fullname
#       self.marks=marks
#       print("adding a new student in database..")
# s1=student("ali",88)
# print(s1.name,s1.marks)
# s2=student("ahmad",89)
# print(s2.name,s2.marks)
# polymorphism (when the same operator is allowed to have different meaning according to the context)
# oerator and Dunder function 
# operator overloading 
print(1+2) # add
print("apna"+"college") # concatenate 
print([1,2,3]+[5,6,7])# merge
# we use Dunder function 
# class complex:
#      def __init__(self,real,img):
#           self.real=real
#           self.img=img
#           def showNumber(self):
#                print(self.real,"i+",self.img,"j")
#                def __add__(self,num2):
#                     newreal=self.real+num2.real
#                     newimg=self.img+num2.img
#                     return complex(newreal,newimg)
#                num1=complex(1,3)
#                num1.showNumber()
#                num2=complex(4,6)
#                num2.showNumber()
#                num3=num1+num2
#                num3.showNumber()
               # Define a circle class to create a circle with radius r suing the constructor . Define an area() nethod of the class which calculate the area of the circle. Define a perimeter () method of the class which allow you to calculate the perimeter of the circle
# class circle:
#      def __init__(self,radius):
#           self.radius=radius
#           def area (self):
#                return 3.14*self.radius**2
#           def perimeter(self):
#                return 2*3.14*self.radius
#           c1=circle(21)
#           print(c1.area())
#           print(c1.perimeter())
          # Define a Employee class with attribute role department and salary . This class also have a showDetails method . Create an Engineer class that inherit properties from Employee and has additional attribute :name and age
          # class Employee:
          #      def __init__(self,role,dept,salary):
          #           self.role=role
          #           self.dept=dept
          #           self.salary=salary
          #           def showDetails(self):
          #                print("role=",self.role)
          #                print("dept=",self.dept)
          #                print("salary=",self.salary)
          # class Engineer(Employee):
          #      def __init__(self ,name,age):
          #           self.name=name
          #           self.age=age
          #           super().__int__("Engineer","IT","65000")
          #           engg1=Engineer("Elon Musk",40)
          #           engg1.showDetails()
          #  create a class called order which store items and its price use Dunder function ..gt..() to convey that order1>order 2 if price of order1>price of order2
class order:
     def __int__(self,item,price):
          self.item=item
          self.price=price
          def __gt__(self,odr2):
               return self,price>odr2.price
          odr1=order("chip",20)
          odr2=order("tea",15)
          print(odr1>odr2)     


