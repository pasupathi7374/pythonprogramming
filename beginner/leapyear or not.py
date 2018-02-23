#-------------------------------------------------------------------------------
# Name:        leap year or not
# Purpose:
#
# Author: bb
# Created:     23-02-2018
# Copyright:   (c) Administrator 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
year=input("enter the year")
if (year % 4) == 0 or (year % 100) == 0 or (year % 400) == 0:
           print("it is a leap year".format(year))
else:
           print("it is not a leap year")