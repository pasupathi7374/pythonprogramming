#-------------------------------------------------------------------------------
# Name:        vowel
# Purpose:
#
# Author: bb
# Created:     23-02-2018
# Copyright:   (c) Administrator 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

alphabet= raw_input("Input a letter of the alphabet: ")

if alphabet in ('a','A', 'e','E', 'i','I', 'o','O', 'u',' U'):
	print("it is a vowel")

else:
	print("it is not a vowel")