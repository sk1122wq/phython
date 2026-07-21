# class Myclass:
#     x=5
    # print(x)
# print(Myclass)
# class Myclass:
#     x=5
# p1=Myclass()
# print(p1.x) # create an object 
# class Myclass:
#     x=5
# p1=Myclass()
# del p1 # delete the object 
# print(p1.x)
# class Myclass:
#     x=5
# p1=Myclass()
# p1=Myclass()
# p1=Myclass()
# print(p1.x)
# print(p1.x)
# print(p1.x)
# class myclass: # The self parameter 
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def greet(self):
#             print("Hello,my name is"+self.name)
# p1=myclass("Emil",25)
# p1.greet()
# create a class name person with firstname and lastname properties,and a print name method
# class person:
#    def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#    def printname(self):
#             print(self.firstname,self.lastname)
# x=person("Ali","Ahmad")
# x.printname()
# class person:
#    def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#    def printname(self):
#             print(self.firstname,self.lastname)
# class student(person):
#     pass            
# x=student("Ali","Ahmad")
# x.printname()
# import numpy
# speed=[9,8,7]
# x=numpy.mean(speed)
# print(x)
# x="Hello world" # fro string the len() return the number of character
# print(len(x))
# mytuple=("apple","banana","cherry")
# print(len(mytuple)) # for tuple len() return the number of items in the tuple
class person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
p1=person("Ali",25)
print(p1.name)
print(p1.age) # cause an error