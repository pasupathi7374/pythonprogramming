#-------------------------------------------------------------------------------
# Name:        even or odd
# Purpose:
#
# Author:      bb
#
# Created:     23-02-2018
# Copyright:   (c) Administrator 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


num =int(input("Enter a number: "))

if 1<=num<=100000 and (num % 2) == 0:
   print("it is Even")
elif 1<=num<=100000:
   print("it is Odd")
else:
    print("limit exceeded")
