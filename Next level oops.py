#  del keyword (used to delete object properties or object itself )
# class student:
#     def __init__(self,name):
#         self.name=name
#         s1=student("ali")
#         del s1
#         print(s1)
        #  private (like ) attribtue and method  
        #  conceptual implementation in python attribute and method are meant to be used only within the class and are not accessible from outside the class . 
# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_pass
#         self.acc__pass=acc_pass


#         acc1=Account("12345","abcde")
#         print(acc1.acc_no)
#         print(acc1.acc_pass)
# class person:
#             __name="anonymous" # private like
#             def __hello():
#                     print("hello person!")
#                     p1=person()
#                     print(p1.___hello())
# inheritance when one class (chil/derives )derives the properties and method of another class 
# class car:
#.....#
# class Toyota car (car):
# ....
# class car:
#     @staticmethod
#     def start():
#         print("car started..")
#         @staticmethod
#         def stop():
#             print("car stopped")
# class Toyotacar(car):
# #     def __init__(self,name):
#         self.name= name
#         car1=Toyotacar("fortuner")
#         car2=Toyotacar("prius")
#         print(car1.start()) # output should be fortuner 
        # we divided inheritance into three type (single inheritance, Multi-level inheritance(there are two or more derive class) )
# Multiple ingeritance(one Derive class and multiple base class) 
# class car:
#     @staticmethod
#     def start():
#         print("car started..")
#         @staticmethod
#         def stop():
#             print("car stopped")
# class Toyotacar(car):
#     def __init__(self,brand):
#         self.brand=brand
# class fortuner(Toyotacar):
#     def __init__(self,type):
#         self.type=type 
# Multiple ingeritance(one Derive class and multiple base class) 
# class A:
#     varA="welcome to classA"
# class B:
#         varB="welcome to classB"
# class C(A ,B):
#       varc="welcome to class c"
# c1=C()
# print(c1.varc)
# print(c1.varB)
# print(c1.varA) # output is welcome to class c,B,and A
# super method (is used to access method of the parent class)
# class car:
#      def __init__(self,type):
#          self.type=type
#      @staticmethod
#      def start():
#          print("car started..")
#          @staticmethod
#          def stop():
#              print("car stopped")
# class Toyotacar(car):
#      def __init__(self,brand):
#          self.brand=brand
# class fortuner(Toyotacar):
#      def __init__(self,name,type):
#          self.name= name
#          super(). __init__(type)
#          car1=Toyotacar("prius","electric")
#          print(car1.type)
         # class Method (A class method is bound to the class and receive the class as an implicit first argument) Note -static method can't access or modify class state adn generally for utility 
         # class student:
        #  @classmethod 
        #  def college(cls)
        #      pass
class person:
    name="ahmad"
    # def changename(self,name):
    #     self.__class__.name="ali"
    @classmethod
    def changename(cls,name):
        cls.name=name
        p1=person()
        p1.changename("ali")
        print(p1.name)
        print(person.name) 







