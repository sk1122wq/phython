# x=5
# y=3
# print(x<<1)
# print(x|y)
# y=3
# x*=3 
# x/=3
# x+=3
# x-=3
# x%=3
# x//=3
#  x**=3
# x&=3
# x|=3
# x^=3
# x>>=3
# x^=3
# x<<=3
# print(x)
# x<<=3
# x=5
# y=3
# print((6+3)-(6+3))
# print(100+5*3) All examples of precedence
# thislist=["apple","banana","cherry"] 
# print(thislist)
# thislist=["apple","banana","cherry","apple","cherry"] 
# # print(thislist)
# thislist=["apple","banana","cherry"]
# print(type(thislist)) # this is example of list
# thislist=["apple","banana","cherry"]
# thislist[1:2]=["blackcurrant","watermelon"]
# print(thislist) This is change the second value by replacing it with t
# wo new values

# thislist=["apple","banana","cherry"]
# thislist[1:3]=["watermelon"]
# print(thislist)
# print(thislist) #This is example of change the second and third value by replacing it with one value
# thislist=["apple","banana","cherry"]
# thislist.insert(2,"watermelon")
# print(thislist) 
# thislist=["apple","banana","cherry"]  
# thislist.append("orange")
# print(thislist)
# thislist=["apple","banana","cherry"] 
# tropical=["mango","pineapple","papaya"]
# thislist.extend(tropical)
# print(thislist)
# thislist=["apple","banana","cherry"]  # This is the example of copy list 
# mylist=thislist.copy()
# print(mylist)
# thislist=["Apple","banana","cherry"] # This is example of list method()
# mylist=list(thislist)
# print(mylist)
# thislist=["apple","banana","cherry"] 
# mylist=list(thislist)
# print(mylist)
# thislist=["apple","banana","cherry"] 
# mylist=thislist[:]
# print(mylist)
# list1=["a","b","c"]
# list2=[1,2,3]
# list3=list1+list2
# print(list3)
# list1=["a","b","c"]
# list2=[1,2,3]
# for x in list2:
#     list1.append(x)
#     print(list1)
# thislist=["apple","banana","cherry"]
# thislist.remove("banana")
# print(thislist)
# thislist=["apple","banana","cherry"]
# thislist.pop(1)
# print(thislist)
# thislist=["apple","banana","cherry"]
# del thislist[0]
# print(thislist)
# thislist=["apple","banana","cherry"]
# thislist.clear()
# print(thislist)
# thislist=["apple","banana","cherry"]
# for x in thislist:
#     print(x)
# thislist=["apple","banana","cherry"]
# for i in range (len(thislist)):
#     print(thislist[i])
# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[]
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
#         print(newlist)
# fruits=["apple","banana","cherry","kiwi","mango"] # list comprehension example 
# newlist=[x for x in fruits if "a" in x]
# print(newlist)
# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[x for x in fruits if x!="apple"]
# print(newlist)
# newlist=[x for x in range (10)]
# print(newlist)
# newlist=[x for x in range (10) if x<5]
# # print(newlist)
# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[x.upper() for x in fruits]
# print(newlist)
# Ala=("apple","banana","cherry") 
# print(Ala)
# thistuple=("apple","banana","cherry","apple","cherry") # allow duplication
# print(thistuple)
# thistuple=("apple",)
# print(thistuple) # create a tuple with one item 
# thistuple=("apple")
# print(type(thistuple))
# tuple1=("apple","banana","cherry")
# tuple2=(1,2,3,4)
# tuple3=(True,False,False)
# print(tuple1)
# print(tuple2)
# print(tuple3)
# tuple1=("abc",34,True,40,"male")

# thistuple=tuple(("apple","banana","cherry")) # The tuple() constructor are used to make a tuple 
# print(thistuple)
# thistuple=("apple","banana","cherry")
# thistuple=list(thistuple)
# y=list(thistuple)
# y.append("orange")
# thistuple=tuple(y)
# print(thistuple)
# thistuple=("apple","banana","cherry") # create a new tuple with the new value orange
# y=("orange",)
# thistuple+=y
# print(thistuple)
# thistuple=("apple","banana","cherry")
# y=list(thistuple)
# y.remove("apple")
# thistuple=tuple(y)
# print(thistuple) 
# thistuple=("apple","banana","cherry")
# del thistuple
# print(thistuple)
# x=5 This is first work
# y=3
# temp=0
# print("value of x:",x,"and y:",y)
# print("let's swap the value of x and y")
# temp=x
# x=y
# y=temp
# print("Value of x:",x,"and y:",y)

# print("Double of the said number is",num+num)
# fruits=['apple','banana','cherry']
# for fruit in fruits:
#     print(fruit)
# amount=1100
# if amount>=1000:
#     print("You qualified for the discount")
#     cutomer_type=input("Enter (Y/N) if you are a regular customer")
#     if cutomer_type=='Y':
#         print("You will be get 20% discound")
#         discount=amount*0.2
#         new_amount=amount-discount
#         print("your new amount is ",new_amount)
#     else :
#         print("you will get 10% discount")
# else:
#          print("you are eligible for discount")
# country=input("Enter your country name:") 
# print("i love",country)
# num=input("Enter a number")
# num=eval(input("Enter a number"))
# print("Double of the said number is",num+num)

# print("Welcome to ATM") 
# pin=1234
# balance=5000
# code=int(input("Enter your code pin"))
# if pin==code:
#     print("Login successfuly")
#     print("1 widtdraw")
#     print("2 Balance inquiry")
#     choice=int(input("Enter your choice"))
#     if choice==1:
#         amount=int(input("Enter amount:"))
#         balance=balance-amount
#         print("Transaction done")
#         print("Remaning balance ",balance)
#     elif choice==2:
#         print("your balance is",balance)
#     else:
#         print("please choose menu")
# else:
#     print("Wrong pin code")
# range(start?,stop,step?)           
# for i in range(2,17,2):
#     print(i, end='   ')
# fruits=["apple","banana","cherry"]
# for fruit in fruits:
#     print(fruit)
# for char in "hello":   #looping over a string 
#     print(char)
# def factorial(n):
#      result=1
#      for i in range(1,n+1):
#           result *=i
#      return result
# num=int(input("Enter the number:"))
# print(f"The factorail of {num} is : {factorial(num)}")
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)

# i=0
# while i<3:
#     print(i)
#     i+=1
# num=int(input("Enter a number(0 to quit):")) # quit mean the loop stop
# while num!=0:
#     print(f"you entered :{num}")
#     num=int(input("Enter a number(0 to quit):"))
  
# i=0
# while i<4:
#     print(i)
#     i+=1
# i=0 #  infinite loop in python  (server listening for client connection for continuosly listen for incoming client connection) using import socket 

# while True:
#     print(i)
#     i+=1
    
# for i in range(1,11):
#     print("7X",i,"=",7*i)
# total=sum(range(1,11))
# # print("sum of the first 10 number:",total)
# for i in range (3):
#     for j in range(2):
#         print(i,j)
# marks=int( input("enter stud3ent marks:"))
# if(marks>=90):
#     grade="A"
# elif(marks>=80 and marks<90):
#     grade="B"
# elif(marks>=70 and marks<80):
#     grade="C"
# else:
#     grade="D"
# print("grade of the student->",grade)
# age=90
# if(age>=18):
#     if(age>=80):
#         print("cannot be derive")
#     else:
#      print("can dreive")
#  Break: used to terminate the loop when encountered 
# i=1
# while i<=5:
#     print(i)
#     if(i==3):
#         break
#     i+=1
#  continue: terminate execution in the current iteration and continue execution of the loop with the next iteration 
# i=0
# while i<=5:
#     if(i==3):
#         i+=1
#         continue 
#     print(i)
    # i+=1
# i=0
# while i<=10:
#      if(i%2==0):
#         i+=1
#         continue
#      print(i)
#      i+=1 
# type conversio n (convert one type of variable to another  and this automatically conversion)
# a=2
# b=4.25
# sum=a+b # 2.0+4.25 ->> 6.25 and float is superior 
# print(sum)
# str="Hi, $ i am the $ symbol $99.99"
# print(str.count("$"))
#  print the number from 1 toP 10 by using for loop  Here to be started 
# for i in range(1,11):
#     print(i)
#  print the multiplication table of a number n
# n=int(input("enter number:"))
# for i in range(1,11):
#     print(n*i)
# wap to input of a square and print its area
# side=float(input("enter square side:,"))
# print("area=",side*side)

# wirte a program to input 2 floating point number and print their averageP
# a=float(input("enter first number:",))

# b=float(input("enter second number:",))
# avg=(a+b)/2
# print("The average of two number is:",avg)
# a=5
# s=a+4
# print(s)
 
# print(1<x<10)
# print(1<x and x<10)
# print(x>3 and x<10)
# print(x>3 or x<10)
# print(not(x<3 or x<10))
# x=[1,2,3]
# y=[1,2,3]
# print(x==y)
# print(x!=y)


# print(x is y)
# x=["apple","banana"]
# print("banana" in x)
# print(x)


# x=5
# y=3
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x%y)
# print(x**y)
# print(x//y)
# sum1=100+50
# sum2=sum1+250
# sum3=sum2+sum2
# print(sum1)
# print(sum2)
# print(sum3)
# def myfunction():
    # return True
# if myfunction():
#         print("yes!")
# else:
#         print("No!")
# def myfunction():
#     return True
# print(myfunction())
# a=200
# b=33
# if b>a:
#     print("b is greater than a")
# else:
#     print("b is not greater than a")
# print(10>9)
# txt="we are the so-called \"Ali\" from the north"
# txt='it\'s alright'
# txt="This will insert one \\(backslash)"
# print(txt)
# age = 36
# price=59
# txt=f"the price is{price} dollars"
# txt=f"the price is{price : .2f}dollars"
# txt=f"the price is{20*59} dollars"
# print(txt)
# txt=f"my name is John,i am {36}"
# print(txt)
# b="Hello,world"
# print(b.split(","))
# # print(b[:5])
# print(b[2:])
# print(b.upper())
# print(b.lower())
# print(b.replace("H","J"))
# b="Hello,world"
# print(b[2:5])
# x="python"
# y="is"
# z="awesome"
# print(x,y,z)
# print(x+y+z)
# a="Hello,world"
# print(len(a))
# for x in"banana":
#     print(x)
# a="Hello,world"
# print(a[1])
# print("He is called 'hohnny'")
# x,y,z="orange","Banana","apple"
# print(x)
# print(y)
# print(z)
# x=y=z="organge"
# print(x)
# print(y)
# print(z)
# my var="iftikhar"
# print(my var)
# x='john'
# print(x)
# print("I am",35,"year old")
# x=3+5j
# y=5j
# z=-5j
# print(type(x))
# print(type(y))
# print(type(z))
# x=2.8
# a=int(x)
# print(a)
# print(type(a))
# print("Hello,"  "world",sep='')
# print("Hello"+"  "+"world")
# print("This is coding")
# print(3+3)
# x=5
# y="hohn"
# print(type(x))
# print(type(y))
# x=str(3)
# y=int(3)
# z=float(3)
# print(x)
# print(y)
# print(z)
# print("Hello world!",end="")
# print("I will print on the same line.")
# print(3+3)
# print(2*5)
# print("i am ",35,"year old.")
# x=1
# a=float(x)
# print(a)
# a="Hello","world"
# print(a[1])
# x="awesome" local variable and global variable 
# def myfunc():
#     global x
#     x="fantastic"
#     print("python is"+x)
# myfunc()
# print("pyton is"+x)
# def line():
#     print("_"*10)
# line()
# line()
# def hline():
#     print("_"*20)
# hline()
# print(3**2-8%4+10/5*3)
# lets we train linear regression model according to our depandent and indepandent variables
# import numpy as np # we import numpy libary as np because we need array
# import matplotlib.pyplot as plt  #import libaryfor plot as plt
# from sklearn.linear_model import LinearRegression # linear regression model alredy buit in sklearn libary linear regression is a model that take two veiable dependent and indepandent and work on it
# x=np.array([[1],[2],[3],[4],[5]])   # indepandent variable (study hors)
# y=np.array([10,20,30,40,50])      # depandent variable (Marks) we consider the values according to we train our model now linear regression find the relation between these two variable
# model=LinearRegression() # we create model and now we train the model in next step
# model.fit(x,y) # in this step we tell the model this x is our indepandent variable and y is depandent variable and find the relation between two variable
# x_pred=np.array ([[2],[5],[6],[8],[9]]) # for predict we give indepandent varaible values 
# y_pred=model.predict(x_pred) # for predict we give indepandent varaible values 
# plt.scatter(x,y,color='red') # show scatter of x and y relationship 
# plt.scatter(x_pred,y_pred,color='blue') # show scatter of x_pred and y_pred relationship 
# plt.title('study Hours vs Marks')
# plt.xlabel('study Hors')
# plt.ylabel('marks')
# plt.show()



# student_grades=[85,92,78,95,82]
# student_grades.insert(2,90)
# print("Grades after adding a new grade:",student_grades)
# student_grades.append(100)
# print("Grades after adding another new grade:",student_grades)
# student_grades.remove(78)
# print("Grades after removing a new grade:",student_grades)
# lowest_grades=student_grades.pop(2)
# print("Grades after removing the grades on index 2:",student_grades)
# if 88 in student_grades:
#     student_grades.remove(88)
# else:
#        print("Grades 88 not found in the list")
#        average_grade=sum(student_grades)/len(student_grades)
#        print("Average grade:",{average_grade})
# import math
# from turtle import *
# def hearta(k):
#     return 15*math.sin(k)**3
# def heartb(k):
#     return 12*math.cos(k)-5*math.cos(2*k)-2*math.cos(3*k)-math.cos(4*k)
# speed(1000)
# bgcolor("black")
# for i in range(6000):
#     goto(hearta(i)*20,heartb(i)*20)
#     for j in range(5):
#         color("#f73487")
#         goto(0,0)
#     done()

# def factorial(n):
#      result=1
#      for i in range(1,n+1):
#           result *=i
#      return result
# num=int(input("Enter the number:"))
# print(f"The factorail of {num} is : {factorial(num)}")



# import dash
# from dash import dcc,html
# import plotly.express as px
# import pandas as pd
# data=pd.DataFrame({
#     "month":["jan","feb","mar","apr","may"],
#     "sales":[150,200,150,300,250]
    

# })
# fig=px.line(data,x="month",y="sales")
# app=dash.Dash()
# app.layout=html.Div(children=[html.H1("sales vs Month DashBoard"),
#                               dcc.Graph(id="sales",figure=fig)
#                               ])
# if __name__=="__main__":
#         app.run(debug=True)
# import turtle
# turtle.speed(3)
# turtle.bgcolor('black')
# turtle.pensize(3)
# def draw_shape():
#     for i in range(200):
#         turtle.right(1)
#         turtle.forward(1)
#         turtle.color('red')
#         turtle.fillcolor('pink')
#         turtle.begin_fill()
#         turtle.left(140)
#         turtle.forward(111.65)
#         turtle.left(120)
#         turtle.forward(111.65)
#         turtle.end_fill()
#         draw_shape()
#         turtle.hideturtle()
#         turtle.done()
# grades=(85,92,78,92,85,95)
# print(grades)
# print("first grade:",grades[0])
# print("second grade:",grades[1])
# print("Third grade:",grades[2])
# if 92 in grades:
#     print("Student got 92")
#     print(grades.count(92))
#     new_grades=grades+(88,90)
#     print(new_grades)
# student_grades={
#   'Amir':90,'Bilal':85,'Dilawar':92  
# }
# for student,grade in student_grades.copy().items():
#     print(f"{student}:{grade}")
#     student_grades['zaid']=88
#     student_grades['Bilal']=87
#     # del student_grades['Dilawar']
#     if 'Dilawar'in student_grades:
#         print(f"\n Dilawar's grade:",student_grades['Dilawar'],"\n")
# else:
#     print("student Dilawar not found \n")
#     for student,grade in student_grades.items():
#         print(f"{student}:{grade}")
# student_test_number={}
# while True:
#     name=input("Enter student name(or'q' to quit):")
#     if name.lower()=='q':
#         break
#     grade=float(input("Enter Test_Number for {}:".format(name)))
#     student_test_number[name]=grade
#     name=input("Enter student name to view test_number:")
#     if name in student_test_number:
#         print(f"{name}'s test_number:{student_test_number[name]}")
#     else:
#         print(f"student'{name}' not found.")
# matrix=[
#         [1,2,3],
#         [4,5,6],
#         [7,8,9]
#   ]
# print(matrix)
# for i in matrix:
#     print(i)
#     for row in range(len(matrix)):
#         for col in range(len(matrix)):
#             print(matrix[row][col], end=' ,')
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print('Matrix is:',matrix)
# for i in matrix:
#     print(i)
#     trans=[
#         [0,0,0],
#         [0,0,0],
#         [0,0,0]
#     ]
#     for row in range(len(matrix)):
#         for col in range(len(matrix)):
#             trans[col][row]=matrix[row][col]
#             print('Transpose of the matrix is:',trans)
#             for j in trans:
#                 print(j)
# students={
#     "sara":["345",85,90,78],
#     "jamal":["678",80,88,92],
#     "zaid":["912",80,79,95]
# }
# sara_reg_num=students["sara"][0]
# print("sara's Reg.No:",sara_reg_num)
# jamal_marks=students["jamal"][1]
# print("jamal marks for first subject are:",jamal_marks)
# students["Azra"]=["234",78,85,90]
# print(students,"\n")
# student_name="Azra"
# subject_index=2
# new_mark=100
# if student_name in students:
#     students[student_name][subject_index]=new_mark
#     print(f"*** Marks updated for {student_name} at index {subject_index}\n")
# else:
#     print("student not found \n")
#     for name,details in students.items():
#         print(f"Registraction Number:",{details[0]})
#         print(f"Marks:[",end='')
#         print(details[1],',',details[2],',',details[3],"]\n")
# with open("abc.txt","w") as file:
#  file.write("The quick brown fox jumps over the lazy dog!!!")
# print("file created and written to successfully!")

# with open("abc.txt","r") as file:
#     for char in file.read():
#         print(char,end="")
#         print("\nfile read character by charcter successfully!")
with open("abc.txt","r") as file:
    for char in file.read():
        print(char,end="")
        print("\nfile read successfuly")
        

      







