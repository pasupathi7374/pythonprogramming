#-------------------------------------------------------------------------------
# Name:        sum of natural number
# Purpose:
#
# Author: bb
# Created:     23-02-2018
# Copyright:   (c) Administrator 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
num=input("enter the natural number")
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is"),sum