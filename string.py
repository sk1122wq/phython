# String is a data type that stroe a sequnece of characters
 # escape sequnece character(next line) 
#str1="This is a string.\nand it a group of characters"
#str2='this is anacollege'
#str3=""" apna college
#print(str1)
#tab sequence"""
#str1="This is a string.\tand it a group of letter"
#print(str1)
# concatenation(to add two string)
#str1="apna"
#len1=len(str1)
#print(len1)
#str2="college"
#print(str1+str2)
# length function(len(str))
'''str1="apna"
str2="college"
final_str=str1+"  "+str2
print(final_str)'''
# slicing(Accessing part of a string)
# str[starting-idx:ending-idx] ending index is not include
#str="ApnaCollege"
#print(str[1:4]) 
# is 'pna' because index start from zero
# str[ :4]is same as str[0:4]
# str[1: ]is same as str[1: len(str)]
# for return every string we write print[str(5:len(str))]
# Nagative index (APPLE -1,-2,-3,-4,-5)
#str="APPLE"
#print(str[-3:-1])
# string function
# str.endswith("er") return true if string ends with substr
str="i am a coder"
#print(str.endswith("er") )
# capitalize() capitalize 1st char
#print(str.capitalize())
# str.replace(old,new) replace all occurrences of old
#print(str.replace("i","we"))
# str.find(word) return 1st index of 1st occurrer
#print(str.find("o"))
# str.count("am") count the occurrence of substr
print(str.count("a"))

