# lab1 --------x------
# print("Rana Mehdi")
# print("Gilgit")

# lab2----------x--------


print("I am Mehdi ")
print("I am learning AI")
# lab3--------------x---------------

# add comments on multiple lines
# print("jamil")
# print("Hussain")
# print("nasar")
# you can select the text and press ctrl + ? from the keyboard\
# # declare variables
# sentence="I am jamil. I am learning and video editing"
# print(sentence)
# print(sentence)
# we declare variables to avoid repition and make our code more reusable, readable and clean
#  my name="Malik"    it give error
#  12name="Naeem"       it give error
#  name_$="zeba"     it give error
#  print="Naeem"      it give error
# name_of_book2="Islamiat"
# print(name_of_book2)
# #variables declared
# name="Malik"
# cgpa=1.0
# # # #call the variables
# print("Name of the user is:",name)
# print("CGPA of the",name,"is:",cgpa)
# id1="Naeem"
# print(id1)
# # not a good approach -> declare variable name according to the data.
# variable update
# Bank="Bank al habib"
# print("before",Bank)
# Bank="ABL"
# print("after",Bank,"Bank al habib")
# data types
# value=78   #integer
# print(type(value))

# new_value=0.123  #float
# print(type(new_value))

# new_value2=-2.786  #float
# print(type(new_value2))
# com=23+78j
# print(type(com))
# print(com.real)
# print(com.imag)





# lab4-------------------x--------------

# string data type
# name="Malik"
# # # print(name)
# print(name, "has the data type", type(name))

# for multiple data
# students="ali", "bano", 'sakina', 23    # automatically create tuple
# marks=23,45,23                           # automatically create tuple
# print(students)
# print(type(students))

# new=[14,"ali"]  # list
# for multiple data we can use:
# list
# tuple
# dict
# set
# boolean data type
# print(type(True))     # => 1
# print(type(False))  # => 0
# int + int
# num1=76
# num2=27
# print(num1+num2)
# # return the sum
# string + int
# num=90
# st="book"
# print(num+st)
# it return error bcz we cannot add int and string
# type casting explicit
# declare variables
# a="12"
# b=34

# # print(a+b)   it return error bcz we cannot add int and string

# # type casting
# new=int(a)

# #  use + operator
# print(type(new))

# print(new+b)
# other method
#  declare variables
# a="62"
# b=84

# print(a+b)   it return error bcz we cannot add int and string

# type casting

# use + operator
# res=int(a)+b
# print(res)
# print(type(res))
# string + string
# first_name="Muhammad"
# last_name="Malik"
# print(first_name+last_name)

# # it has combined the both strings
# string + string
# num1="34"
# num2="0"
# print(num1+num2)

# # it has combined the both strings
# implicit type casting
# com=7+8j
# num=90
# print(com+num)
# print(type(com+num))

# # here python automatically add int, complex and return a complex. You not need to change the data type
# implicit type casting
# integer=90
# fl=8.78
# print(integer+fl)
# print(type(integer+fl))

#  here python automatically add int, float and return a float. You not need to change the data type
#  boolean consist of 2 keywords:
#  True  => 1
#  False  =>0
# res=False
# int_res=int(res)
# print(int_res)
# print(type(int_res))


# int + string
# res="True"
# int_res=int(res)
# print(int_res)
# print(type(int_res))

# It show error bcz we cannot add int and string
# boolean + boolean
# res=(True+False)
# print(res)
# print(type(res))
# print(bool(res))
# print(True + True)
# print(True+10)
# use of id
# name=795857
# print(id(name))
# id() returns the unique identifier of the object (in CPython, it's the memory address)
# convert boolean to string
# res=True
# new=(str(res))
# #  print(type(new))
# print("The result is", new)



# lab 5---------------x------------------

# #input from the user
# age=input("Enter your age: ")
# new=int(age)   #by default input return string so we convert it into integer
# print("You will be", new+1,"in next year")
# take inputs from the user
# num1=int(input("enter a number "))
# num2=int(input("enter a number "))
# #  calculate the sum
# sum=num1+num2
# #  display the result
# print("Sum of",num1, "and", num2, "is", sum)
# #formatted string
# print(f"Sum of {num1} and {num2} is {sum}.")
# Write a Python program that calculates the total cost of a shopping item using formatted strings.
# Prompt the user to enter the name of the item, its price (as a float), and the quantity (as an integer).
# Calculate the total cost by multiplying the price with the quantity.
# Use a formatted string (f-string) to display the following output:


# You bought 4 Notebooks at Rs. 120.5 each.

# Your total bill is: Rs. 482.0
# #declare varaibles and take inputs from the user

# item_name=input("enter the name of the item: ")
# price=float(input("enter the price of the item: "))
# quantity=int(input("enter the quantity of the item: "))

# # #finding cost

# cost=price*quantity

# # print the result
# print(f"You bought {quantity} {item_name} at Rs.{price} each.")
# print(f"Your total bill is Rs.{cost}")

# print with formatted string
#  print(f"You bought {quantity} {item_name} at Rs.{price} each.\nYour total bill is Rs.{cost}")
# arithmetic operators
# arithmetic operators
# a=9
# b=3
# print(a+b)  #addition
# print(a-b)  #subtraction
# print(a*b)  #multiplication
# print(a/b)  #division
# print(a//b)  #floor division
# print(a%b)  #modulus
# print(a**b)  #power

#  +-  operators  a,b operands
# comparison operators
# comparison operators

# print(5==6)       #False (is equal to)
# print(5<6)        #True (less then)
# print(12>90)      #False (greater then)
# print(5<=2)       #False (less then equal to)
# print(78>=109)    #False (greater then equal to)
# print(5!=5)       #False  (not equal to)
# print(1==True)    #True   (is equal to)
# print(1=="a")     #False  bcz int and string are not comparable.
# print("True"==True)#False  bcz boolean and string are not comparable.
# #logical operators
# #logical operators

# print(25<6 and 18<9)         #if all conditions are True then return True
# print(123<89 or 78<10)       #if any one condition is True then return True
# print(not(True))             #not return opposite
# print(not(15<9))             #not return opposite
# num=90
# print(not(num))   #bcz here num has the data, so while applying not it returns False
# a=None
# print(not(a))

# #bcz here a has not any data, so while applying not returns False
# #assignment operators
# #assignment operators

# a=4
# a+=2  #a=a+2   add and assign
# print(a)
# a=4
# a-=1  #a=a-1   subtract and assign
# print(a)

# a=9
# a*=2     #a=a*2     multiply and assign
# print(a)
# a=20
# a**=2     #a=a**2     power and assign
# print(a)
# a=8
# a/=12     #a=a/12     divide and assign
# print(a)
# a=19
# a%=2     #a=a%2     modulus and assign
# print(a)
# a=9
# a//=2     #a=a*2     floor divide and assign
# print(a)
# Question: Movie Night Group Discount at cinema charges Rs. 850 per ticket.

# A group gets a 15% discount if:

# The group has 4 or more people AND The total price is more than 3000

# Write a program that: Takes number of people as input Calculates total cost Applies discount automatically using formulas Displays all details
# declare variables
# num_ppl=int(input("enter the number of people: "))
# charges=850
#  calculate total price
# total=charges*num_ppl
# print(f"Total price is {total}")

#  check whether the user is eligible for discount
# is_dis=num_ppl>=4 and total>3000
#  print(is_dis)  it return True or False
#  Find discount
# dis=total*0.15*is_dis  #is_dis may have the value 1 or 0
# print(f"Discount is {dis}")
# new_price=total-dis
# print(f"Total Price after discount is: {new_price}")



# lab 6---------------------x-----------------------

#  IF-ELSE
# Age=int(input("Write your age:"))

# if Age >= 18  :
#  print("You are eligible to vote ")
# if Age < 0:
#   print("Invalid age")
# else:
#   print("You are not eligible to vote ")


# # even or odd
# num = int(input("Write a number: "))

# if num % 2 == 0:
#   print("Number is even")
# else:
#   print("Number is odd")


# Grading System

# marks=int(input("Enter your Marks: "))

# if marks < 0 or marks > 100:
#   print("Please enter correct number")
# elif marks >= 90 and marks <= 100 :
#   print("Grade A+")
# elif   marks >= 80 and marks < 90:
#   print("Grade A")
# elif marks >= 70 and marks < 80:
#   print("Grade B")
# elif marks >= 60 and marks < 70:
#   print("Grade c")
# elif marks >= 50 and marks < 60:
#   print("Grade D")
# else:
#   print("You're Fail ")


# # largest of three number

# num1=int(input("Enter number 1: "))
# num2=int(input("Enter number 2: "))
# num3=int(input("Enter number 3: "))

# if num1 > num2 and num1 > num3:
#   print("Number 1 is greater")
# elif num2 > num1 and num2 > num3:
#   print("Number 2 is greater")
# else:
#   print("Number 3 is greater")


# sceret Number

# sceret = 1

# print("Welcome to the game ")
# guess=int(input("Enter a number: "))

# if guess == sceret :
#   print("You guessed right !!")
# else:
#   print("You loss !")



# lab7-----------------x-----------------
 
# #and between integers
# num1=5     # 5-> True
# num2=0     # 0-> False
# print(num1 and num2)  #False -> 0
# num1=9   #True
# num2=3    #True
# print(num1 and num2)  #True
# # because it will return the last true
# num1=9   #True
# num2=3    #True
# num3=89   #True
# print(num1 and num2 and num3)  #True
# # because it will return the last true
# num1=0  #False
# num2=-3  #False
# print(num1 and num2)  #False ->0
# #Or between integers
# num1=9  #True
# num2=0   #False
# print(num1 or num2)  #True
# num1=9  #True
# num2=0   #False
# num3=7   #True
# print(num1 or num2 or True)  #True

# #bcz it will return the first true
# num1=-9  #True
# num2=0   #False
# print(num1 or num2)  #True
# #Nested conditions
# Problem Statement: Online Shopping Discount Checker

# You are writing a Python program for an online shopping app.

# The program should:

# Ask the user for the total amount of their shopping.

# If the amount is greater than or equal to 1000, they qualify for a discount.

# Then ask if they are a first-time customer (yes or no).
# If they are a first-time customer, they get 20% discount.
# If not, they get 10% discount.

# If the amount is less than 1000, print: "No discount. Spend at least 1000 to get a discount.“


# #Take the amount from the user
# amount=int(input("Enter the amount "))
# #check whether is eligible for discount or not
# if amount>=1000:
#   print("You qualified for the discount")
#   customer_type=input("Enter (y/n) if you are a regular customer ")
# # check whether the customer is regular or not
#   if customer_type=='y':
#     print("You will get 20% discount")
# # #Calculating the amount after discount (extra part)
#     discount=amount*0.2
#     new_amount=amount-discount
#     print(f"Your new amount is {new_amount}")
#   else:
#     print("You will get 10% discount")
# else:
#   print("You are not qualified for the discount")
# Write a Python program to simulate an ATM Machine:
# 1. Ask the user for PIN
# 2. If PIN is correct → Show menu (1. Withdraw, 2. Balance Inquiry)
# 3. If Withdraw → Check sufficient balance
# 4. If enough balance → Deduct amount
# 5. If not enough → Show error message
# 6. Else if Balance Inquiry → Show current balance


# # # NESTED IF-ELSE


# print("Welcome to ATM ")

# pin=1234

# balance=5000

# # # # Take the user code as input

# code=int(input("Enter your pin code: "))

# # # check whether the user's  code is equal to pin
# if pin == code:
#   print("Login Successfully")
#   print("1 withdraw ")
#   print("2 Balance Inquiry")

#   choice= int(input("Enter your choice"))


# # # # nested if else

# # # # check for withdraw
#   if choice == 1:
#     amount = int(input("Enter your amount "))
# # # check whether the amount is lesser or equal to balance

#     if amount <= balance :

#       balance = balance - amount
#       print("Transaction done ")
#       print("Remaning Balance ", balance )
# # # # if the amount is greater then balance then we cannot withdraw

#     else:
#       print("Insufficenet Balance")
# # check for the balance
#   elif choice == 2:
#     print("Ypur Balance is: ", balance )
# # check for the wrong input
#   else:
#     print("Please choose from menu ")
# # check for the wrong pin code
# else:
#   print ("Wrong pin code ")




#   lab 8 ---------------x------------------

# # Program looks like without using loop
# print("Hamza")
# print("Hamza")
# print("Hamza")
# print("Hamza")
# #while loop
# Print your name 10 times by using while loop
# i=0
# while i<10:
#   print("Hamza")
#   i+=1
# Print numbers from 1 to 10 by using while loop
# num=1
# while num<=10:
#   print(num)
#   num+=1
# use of formatted string in loop
# num=1
# # while num<=7:
# while num<8:
# #   # printing variables by using formatted string
#   print(f"{num} times Hamza")
#   num+=1
#  use of end=" " in loop
# num=1
# # while num<=7:
# while num<8:
#   # print name 7 times without terminating the line
#   print("Hamza",end=" ")
#   num+=1
# # we have to use end="" bcz it is the by default behaviour of python that on running a loop it print the statement on a new line
# printing the table of a number by using while loop
# number=int(input("enter a number to display the table "))

# i=1
# while i<=10:
#   print(f"{number} x {i} = {number*i}")
#   i+=1
# # Print odd numbers in reverse from 100 to 1 by using while loop
# num=100
# num=num-1
# # # we have to update the variable with 99 bcz our series will start from 99
# while num>=1:
#   print(num, end=", ")
#   num-=2
# #for loop
# start=8
# stop=20
# jump=1
# for value in range(start,stop,jump):
#   print(value)
# for i in range(9,2):
#   print(i)

# # it will not return any output bcz starting point should always be greater then ending point.
# for i in range(4):
#   print(i)

# # start=0
# # stop= 4
# # jump=1

#   # here by default starting point is 0 and it apply the increment of 1
# Print Even Numbers from 2 to 10 use for loop


# for i in range(2,11,2):
#   print(i)
# Calculate the sum of numbers from 1 to n by using for loop

# n=int(input("Enter a number "))
# sum=0
# for i in range(1,n+1):
#   # update the variable sum in loop
#   sum+=i
# print(f"sum of numbers from 1 to {n} is: {sum}")



# lab 9---------------x-------------


# print("Welcome to the world of Python programming!\n")

# # Take input name and marks from the user
# student_name = input("Enter your name: ")
# math = int(input("Enter your math marks: "))
# computer = int(input("Enter your computer marks: "))
# physics = int(input("Enter your physics marks: "))

# # display
# print("Student is : ", student_name)
# print("Math marks are: ", math)
# print("Physics marks are: ", physics)
# print("Cimputer marks are: ", computer)

# # find obtained and average marks
# obtained_marks = math + physics + computer
# average_marks = (math + physics + computer) // 3 #float division

# print(f"Average marks are: {average_marks}")

# # assign grades according to average
# if (average_marks >= 80):
#   grade = "A"

# elif (average_marks >= 60 and average_marks < 80):
#   grade = "B"

# elif (average_marks >= 40 and average_marks < 60):
#   grade = "C"

# else:
#   grade="F"

# #print grade
# print(f"Grade is : {grade}")
# lab 10
# #break
# # break in while loop
# i=1
# while i<=10:  #while i<5:
#   if i==5:
#     break
#   print(i)
#   i+=1
# # on reaching to the break, loop will terminate


# lab 10----------------x----------------

# # break in for loop

# for i in range(1,6):
#   if i==3:
#     break
#   print(i)
#   i+=1


# #continue
# # continue in while loop
# i=1
# while i<=10:
#   i+=1
#   if i==5:
#     continue
#   print(i)

#   # continue will skip the condition

#   # on reaching to the continue, program will automatically move to the while keyword and donot run the program written
#   # below the continue so that the program will run to the infinity

#   # To handle this situation we have to update the variable before the continue.
# for i in range(1,11):
#   if i==5:
#     continue
#   print(i)
# #pass
# var=5
# stop=10
# while var<=stop:
#   if var==7:
#     pass
#   # when executed perform null operation
#   print(var)
#   var+=1
# name="Hamz"

# if name=="Hamza":
#   pass
# else:
#   print("what is your name")
# Ask the user for a number.

# Print its multiplication table but skip the 5th multiple.

# num=int(input("Enter a number "))
# start=0
# end=9
# while start<=end:
#   start+=1
#   if start==5:
#     continue
#   # it will skip the 5th multiple
#   print(f"{num} x {start} = {num*start}")


# Take a number from the user.

# check whether the number is Prime or composite.
# number=int(input('Enter a number '))
# if number<=0: #check for 0 and negative integers
#   print("The number is neither composite nor prime. Enter a value greater then 0")
# elif number==1: #separately check for 1
#   print("The number is composite")
# else:  # check from 1 to number-1
#   for i in range(2,number):
#     if number%i==0:
#       print("the number is composite")
#       break
#     # if loop donot reach the break and print nothing, then print:
#   else:
#     print("the number is prime")
# Take two numbers from the user start and stop.

# print the series start to stop

# while True:

#   # start>=stop then repeat the same process!
#   start=int(input("enter a number to start the series "))
#   stop=int(input("enter a number to stop the series "))

#   # stop the loop when:
#   if start<stop:
#     break

# # print the series
# while start<=stop:
#   print(start)
#   start+=1


# lab 11-----------------x--------------------

# Take a string from the user. check if the string is empty or not
# # st=input("enter")
# # if st=="":
# #   print("empty")
# # else:
# #   print("not empty")


# #take input from the user
# st=input("enter a string ")

# # check if the user entered something or not
# if st:
#   print("You entered",st)
# else:
#   print("You entered nothing")
# Problem 5: Take a number from the user as input and check whether the number is positive, negative, or zero.

# If the number is positive:

# Determine whether it is even or odd.

# If even:

# Check whether it is divisible by 4 and divisible by 12.

# If yes, add 10 to the number and print the updated value.

# If odd:

# Multiply the number by 3 and print the updated value.

# Then check whether the new value is greater than 30 and print the result.

# If the number is negative:

# Determine whether it is even or odd.

# If even:

# Check whether it is less than -10 or greater than or equal to -10 and print the result.

# If odd:

# Multiply the number by 2 and print the updated value.

# If the number is zero, simply print: "The number is zero".

# Note: Print the number’s value and all intermediate results at each step.
# # take input from the user
# num=int(input("enter a number"))
# # check if the number is positive
# if num>0:
#   print("positive")
# #check if the number is even
#   if num%2==0:
#     print("even")
# #check if the number is divisible by 4 and 12
#     if num%4==0 and num%12==0:
#       num+=10
#       print("updated value is",num)
# # check if the number is odd
#   else:
#     print("odd")
#     print(num*3)
# # check if the number is negative
# elif num<0:
# # check if the number is even
#   if num%2==0:
#     print("even")
# # check if the number is less then -10
#     if num<-10:
#       print("less then -10")
# # check if the number is greater then -10
#     elif num>-10:
#       print("greater then -10")
# # check if the number is equal to -10
#     else:
#       print("equal to -10")
# # check if the number is odd
#   else:
#     print("odd")
#     print(num*2)
# # check if the number is equal to zero
# else:
#   print("the number is equal to 0")
# #built in functions of int
# print(bin(3))
# print(bin(567))
# a=79
# bin_a=bin(a)

# print(type(bin_a))

# b=oct(a)
# print(b)
# print(type(b))
# a=7899
# print(hex(a))
# print(abs(-9))
# print(abs(9))
# print(divmod(45,4))
# value=90.667
# print(round(value,0))
# print(round(value,-1))
# print(round(value,2))
# print(round(value,3))
# print(pow(4.90,3))
# # built in functions of float
# print(abs(-90.67))
# print(divmod(24.8989,6))
# #built in functions of complex
# a=8j
# print(a.real)
# print(a.imag)
# a=90+8j
# print(a.conjugate())

# b=-18j
# print(b.conjugate())
# # Since we didn’t specify a real part in the variable b.
# # so, Python shows it as -0 but in Python 0 and -0 are the same, so don’t worry about it
# a=4+8j
# print(abs(a))

# #it will return the magnitude of a

# lab 12
# String
# length of string / number of characters
# name="Hamza"
# # # name='Ali'

# print(len(name))  # built in function to check the length of the string
# # # concatenation
# first="Muhammad"
# last="Ali"
# print(first+" "+last)  # use + for concatenation
# # Membership operator in string
# print("a" in "Hamza") # use in to check the membership
# print("k" not in "Hamza")
# print("am" in "Hamza")
# print("A" in "Hamza") # it return False bcz python is case sensitive language.
# # Repetition
# a="Hamza"
# b=a*5
# print(a)
# print(b)
# # indexing in the string
# country="Pakistan"

# print(country[0])
# print(country[1])

# print(country[-1]) # return the last character
# # Take name from the user as input and return the first and last character of the name
# name=input("Enter your name ")
# print(name[0])
# print(name[-1])
# # iteration by using while loop
# name="Ahmad"
# start=0      # start from the 0 index
# while start<=len(name)-1:
#   print(name[start])
#   start+=1

# # use of end=""
# name="Ahmad"
# start=0

# while start<=len(name)-1:   # using the <= operator
#   print(name[start],end="")
#   start+=1
# name="Pakistan"
# start=0
# while start<len(name):    # use of < operator
#   print(name[start],end="")
#   start+=1
# name="Muhammad"
# start=0
# # while start<=len(name)-1:
# while start<len(name):
#   print(name[start],end="")
#   start+=1
# print(len(" $TD8"))  # each value is consider as character in string
# # iteration by using for loop
# name="Zohaib"
# for i in range(len(name)):
#   print(name[i])
# # iteration by using while loop


# name=input("enter ")
# start=len(name)*-1        #start from the first character but use its negative index like -3 in "Ali"

# while start <=-1:
#   print(name[start])
#   start+=1
# # iteration by using for loop without range function
# country="Pakistan"

# for i in country:
#   print(i)
# enumerate
# country="Pakistan"

# for index,value in enumerate(country):
#   print(f"on index {index} the character is {value}")
# #Take name from the user as input and display the characters from start to mid like Mah in Maham
# name=input("enter ")
# start=0
# end=len(name)-1

# mid=(start+end)//2   #find mid

# for i in range(len(name)):
#   if name[i]==name[mid]:    # if loop reach the mid character then stop the loop
#     print(name[i])
#     break
#   print(name[i],end="")

# lab 13-------------------x----------------------

# #String built-in functions
# Case conversion Methods
# a="pyTHon pRograMiNg"

# print(a.upper())                  # convert all the char in upper case
# print(a.lower())                  # convert all the char in lower case
# print(a.capitalize())             # convert first char in upper and remaining in lower case
# print(a.title())                  # convert first char of each word in upper and remaining all in lower case
# print(a.swapcase())               # swap the cases of all characters
# Search and find methods
# new="python programing"
# print(new.find("p"))                     # find the index of character 'p'
# print(new.find("P"))                     # return -1 bcz 'P' not found
# print(new.find("k"))                     # return -1 bcz 'k' not found
# print(new.find("o",3,15))                # find 'o' from index 3 to 14
# print(new.rfind("p"))                    # find 'p' from right side
# print(new.rfind("n",1,7))                # find 'n' from index 1 to 6 from right side
# print(new.rfind("n",8,10))               # return -1 bcz 'n' is not found on index 8 to 9
# print(new.find("g",11,16))               # return -1 bcz 'g' is not found on index 8 to 9
# print(new.index("n"))                    # return index on 'n'
# # # print(new.index("n",10,14))            # return error bcz 'n' is not found on index 10 to 13
# print(new.rindex("o",1,6))               # search 'o' from right side on index 1 to 5
# new="python programing"
# print(new.startswith("p"))                 # check whether the string starts with "p" or not
# print(new.startswith("pyt"))               # check whether the string starts with "pyt" or not
# print(new.startswith("ptn"))               # check whether the string starts with "ptn" or not
# print(new.startswith("p",3,10))            # check from index 3 to 9 whether the string starts with "p" or not
# print(new.endswith("ing"))                 # check whether the string ends with "ing" or not
# print(new.endswith("ning"))                # check whether the string ends with "ning" or not
# print(new.endswith("ing",2,6))             # check from index 2 to 5 whether the string ends with "ing" or not

# new="python programing"
# print(new.count("p"))                  # count 'p' in the string
# print(new.count("p",1,16))             # count from index 1 to 15 "p" in the string
# check methods (these methods return boolean (True/False))
# print("7878".isnumeric())              # if string contain all the characters from 0-9 then true
# print("78b8".isnumeric())              # if string contain all the characters from 0-9 then true
# print("787sds8".isnumeric())           # if string contain all the characters from 0-9 then true
# print("fhdhfd33".isalpha())            # if string contain all the characters (alphabetic) then true
# print("fhhjADA".isalpha())             # if string contain all the characters (alphabetic) then true
# print("78hjhASA".isalnum())            # if string contain all the characters (alphabetic) or 0-9 then true
# print("78hjh###".isalnum())            # if string contain all the characters (alphabetic) or 0-9 then true
# print("78".isalnum())                  # if string contain all the characters from 0-9 then true
# print("343".isdigit())                 # if string contain all the characters from 0-9 then true
# print("343".isdecimal())               # if string contain all the characters from 0-9 then true
# print("Python Is Very Easy".istitle()) # if first char of each word in string is upper all the remaining are lower then return True othewise False
# Modification methods
# print("  Hamza  ".strip())             # remove the space from start and stop

# name="  #  #Hamza##"
# print(name.strip("#"))                 # remove '#' from both sides

# name="    Hamza   "
# print(name.lstrip())                   # remove space from left side
# print(name.rstrip())                   # remove space from right side

# name="  #  #Hamza##"
# print(name.rstrip('#'))                # remove '#' from right side
# new="python programingooo"
# print(new.replace("o","P"))                # replace 'o' with 'p'
# print(new.replace("o","J",3))              # replace first 3 'o' with 'J'
# Split methods
# sen="I am learning Python"
# print(sen.split())                                                              # convert all the words in element of list
# print(type(sen.split()))                                                        # data type of this output is list
# print(sen.split("a"))                                                           # split on each 'a'
# print(sen.split("a",1))                                                         # split on first 'a'
# print(sen.rsplit("a",1))                                                        # split on first 'a' from right side
# sent="I am learning Python\nPython is very easy\nIt is used in AI"
# print(sent.split('\n'))                                                         # split on each '\n'
# print(sent.splitlines())                                                        # split on each '\n' or line
# print(sent.splitlines(True))                                                    # also write '\n'

# name="Hamza"
# print(name.partition("m"))                                  # split in 3 elements
# print(type(name.partition("m")))                            # return the output in tuple
# print(name.partition("a"))                                  # split on first 'a'
# print(name.partition("H"))                                  # split the targeted char in middle
# print(name.rpartition("a"))                                 # split on first 'a' from right side
# a="90"
# print(a.zfill(3))           # Make the length of string 3 so, it will add one zero in start

# lab 14--------------------x------------

# Take a number n from the user as input and print the Fibonacci series up to n


# num=int(input("enter a number "))
# i=0

# first=0
# second=1

# if num<0:        # check for negative input
#   print("enter a valid number")

# elif num==0:     # check for zero
#   print(first)

# elif num==1:     # check for 1
#   print(first)
#   print(second)

# else:            # check for other numbers
#   print(first)
#   print(second)
#   while i<num-2:
#     total=first+second
#     print(total)
#     first=second     # update the first varibkle
#     second=total     # update the second variable
#     i+=1
# name="Hamza"
# print(name[0])
# name[0]="C"
# print(name)

# # it will return error bcz string is unmutable (unchangable) data type


# isspace
# print(" ".isspace())
# print(" b ".isspace())
# print("\n".isspace())
# print("\t".isspace())
# is operator
# a="Hamza"
# print(id(a))          # return the memory address
# b="Hamza"
# c="Ahmad"
# print(id(b))           # return the memory address
# print(a is b)          # return True bcz the data is same and both varibles point to the same object in memory.
# print(a is c)      # return False bcz the data is different and both varibles point to the different objects in memory.
# a=5
# b=5
# c=6
# print(a is b)    # return True bcz the data is same and both varibles point to the same object in memory.
# print(a is c)


# l1=[1,2,3]
# l2=[1,2,3]
# print(l1 is l2)    # return False bcz both varibles point to the different objects in memory as list is unmutable.


# a=23
# b=90
# c=90
# print(a is not b)
# print(b is not c)

# a=-6
# b=-6
# print(a is b)    # return False bcz is is out of the range (-6<=n<=256)

# a=278
# b=278
# print(a is b)   # return False bcz is is out of the range (-6<=n<=256)

# Slice in String
# text="PythonPrograming"
# # print(text[start:end:jump])   #syntax of slice

# print(text[0:5:1])               # Slices the string from index 0 to 4 (5 is excluded) with a step of 1
# print(text[0:5:2])               # step of 2
# print(text[0:5])                 # by default step=1, we can skip it
# print(text[:5:])                 # if we donot enter the start argument it will slice from 0
# a=text[0:15:4]
# print(a)                         # You can store the sliced sub string in a variable
# print(text[3::])                 # It will print characters from index 3 to last
# print(text[::-1])                # It will print all the characters in reverse order  (sort the string)
# print(text[::-2])                # It will print the characters in reverse order (sort the string) but with the jump of 2
# print(text[-10:-3:])             # it will print the characters from index -10 to -4
# Write a Python program to check the strength of a password based on multiple conditions.

# The program should:

# Take a given string as the password.

# Verify the following rules one by one:

# Length Check: Password must be at least 8 characters long.

# Uppercase Check: Password must contain at least one uppercase letter.

# Lowercase Check: Password must contain at least one lowercase letter.

# Digit Check: Password must contain at least one digit.

# Special Character Check: Password must contain at least one character from the set !@#$%^&*()_+-=[]{};:'",.<>?/|

# # take input from the user
# pas=input("enter a password ")
# res=True

# # check length of the password
# if len(pas)>=8:
#   res*=True    # res=res*True   (update the result)
# else:
#   res*=False   # res=res*False   (update the result)

# # check whether the password has atleast one upper case character

# for i in pas:
#   if i.isupper():
#     res*=True    # (update the result)
#     break
# else:
#   res*=False     # (update the result)


# # check whether the password has atleast one lower case character

# for i in pas:
#   if i.islower():
#     res*=True  #  (update the result)
#     break
# else:
#   res*=False   #  (update the result)

# # check whether the password has atleast one numeric character

# for i in pas:
#   if i.isnumeric():
#     res*=True    #  (update the result)
#     break
# else:
#   res*=False    #  (update the result)

# # check whether the password has atleast one special character

# special="""!@#$%^&*()_+-=[]{};:'",.<>?/|"""
# for i in pas:
#   if i in special:
#     res*=True    #  (update the result)
#     break
# else:
#   res*=False    #  (update the result)

# if res:   # if res==True
#   print("Strong password")
# else:   # res==False
#   print("weak password")



#   lab 15--------------------------x----------------
# #List
# elements of list
# new=[34,"Hamza",89.90,78+8j,[89,89],True,None]
# first=(new[1])
# print(type(first))      # Prints the data type
# print(first[1])         # Prints the character on the index 1
# print(new[1][2])        # Prints the third character of the string at index 1 of the list ('Hamza' → 'm')
# print(type(new[3]))     # Prints the data type of the element at index 3
# print(type(new))        # Prints the data type of the entire variable 'new' (which is a list)
# empty list
# a=[]               # declare an empty list
# print(a)
# b=list()           # declare an empty list
# print(b)
# list is mutable (changable)
# names=["Ali","Ahmad","Zain"]
# names[1]="Bilal"                 # change the element of list on index 1
# print(names)
# # names=["Ali","Ahmad","Zain"]
# # print(names[4])


# # it will return error 'list index out of range'
# # as we are calling the element out of range of list
# concatenation
# l1=[23,343,343,23,"Ali"]
# l2=[78,78,"Ahmad"]
# print(l1+l2)                 # Concatenates l1 and l2, returning a new combined list
# Repetition
# l2=[78,78,"Ahmad"]
# l2=l2*3                  # Repeats the list 3 times and assigns it back to l2
# print(l2)
# Membership operator
# print(343 in l1)
# print(560 not in l1)
# Slice operator
# l1=[23,343,343,23,"Ali"]
# new=(l1[2:5:2])                    # print the elements from index 2 to 4 with jump of 2
# print(new)


# print(l1[::-1])                   # Print all the elements in reverse order
# print(l1[-4:-2])                  # print the elements from index -4 to -3
# print(l1[-2:-5:-1])               # print the elements from index -2 to -4 in reverse order
# change multiple elements of list
# l1=[23,343,343,23,"Ali"]
# l1[-2:-5:-1]=["a","b","c"]

# # Replace elements from index -2 to -4 (reverse slice) with ["a","b","c"]
# #   -2 → "Ali"  → replaced with "a"
# #   -3 → 23     → replaced with "b"
# #   -4 → 343    → replaced with "c"

# print(l1)

# iteration on list
# by using for loop with range
# l1=[23,343,343,23,"Ali"]

# for i in range(len(l1)):
#   print(l1[i])

# by using while loop



# l1=[23,343,343,23,"Ali"]

# start=0
# end=len(l1)-1

# while start<=end:
#   print(l1[start])
#   start+=1
# by using for loop

# l1=[23,343,343,23,"Ali"]
# for i in l1:
#   print(i)


# enumerate
# l1=[23,343,343,23,"Ali"]
# # for index, value in enumerate(l1):      # first variable -> index and second variable -> element of the list
# #   print(index, value)
# # built _in functions
# l1=[23,34,323,34]
# l2=[23,243,23,"Ahmad"]
# l3=["Mango","pineapples","apple","banana","grapes","Orange","mango"]

# # max
# print(max(l1))                  # Returns the maximum numeric value from l1 → 323
# print(max(l2))                  # error: Python cannot compare numbers with strings
# print(max(l3))                  # Returns the maximum string (lexicographically, based on ASCII/Unicode)

# # min
# print(min(l3))                  # Returns the minimum string (lexicographically)

# # sum

# print(sum(l1))                  # Returns the sum of all numeric elements in l1 → 414
# print(sum(l2))                  # error: l2 has both numbers and a string, so sum() will not work


# # sorted
# b=(sorted(l1))
# print(b)                          # sort elements in ascending order


# b=(sorted(l1,reverse=True))
# print(b)                          # sort elements in descending order

# b=sorted(l3)                      # Sorts alphabetically (capital letters come before lowercase due to ASCII)

# print(b)

# b=sorted(l3,key=str.lower)        # Sorts alphabetically, ignoring case
# print(b)


# c=sorted(l3,reverse=True,key=str.lower)   # Sorts alphabetically in reverse order, ignoring case
# print(c)
# # any
# print(any([True,False,1]))           # Print True if atleast one element will be True
# print(any([]))                       # bcz empty list -> False

# # all
# print(all([" ",1]))                  # print True if all the elements will be True
# print(all(["",9,"kl"]))
# print(all(["-",-9,"kl"]))
# sort()
# 15=["ilyas","musa","Rahman","naqi","Aisar","Naveed","sabir"]
# print(15)
# 15.sort(reverse=True)         # after sorting update l3
# print(15)

















