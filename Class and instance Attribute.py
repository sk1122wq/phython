#  #  class and instance attribute class attribute and object attibute  instance attribute like self.name self.marks etcclass student:
# class student:
#   college_name="ABC college"
#   def __init__(self,fullname,marks): # self parameter is a reference to the current  this consttructor is called parametise constructor 
#        self.name=fullname
#        self.marks=marks

# #def welcome(self):
#    #     print("welcome student")
#   #      s1 =student("ali",88)
#  #       s1.welcome()          
# #        print("adding a new student in database..")
# s1=student("ali",88)
# print(s1.name,s1.marks)
# s2=student("ahmad",89)
# print(s2.name,s2.marks)
# print(student.college_name)
 #method and attribute ( method are used function that belong to object) creating object 
 #class studnet: # def__int__(self, fullname);
# create student class that take name adn marks of 3 subject as argument in constructor then create a method to print the average
# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#         def get_avg(self):
#             sum=0
#             for val in self.marks:
#                 sum+=val
#             print("hi",self.name,"your avg score is:",sum/3)
            
# s1=student("ali",[99,78,88])
# s1.get_avg()
# static Method ( Method that don't use the self param) work at class level 
# class student: # decorator 
#     @staticmethod
#     def college():
#         print("ABC college")
class student:
     def __init__(self,name,marks):# self parameter is a reference to the current  this consttructor is called parametise constructor 
      self.name=name
      self.marks=marks
      @staticmethod
      def hello():
         print("hello")
         def get_avg(self):
            sum=0
            for val in self.marks:
               sum+=val
            print("hello",self.name,"your avg score is :",sum/3)
            s1=student("ali",[99,98,97])
            s1.get_avg()
            s1.hello()
#    Abtraction (hiding the implement details of a class and only showing the essential feature to the user )

