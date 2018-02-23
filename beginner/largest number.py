#-------------------------------------------------------------------------------
# Name:        largest number
# Purpose:
#
# Author: bb
# Created:     23-02-2018
# Copyright:   (c) Administrator 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

num1=input("enter the value 1 : ")
num2=input("enter the value 2 : ")
num3=input("enter the value 3 :")

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print('The largest number is'),largest