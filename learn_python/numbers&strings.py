# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 19:49:29 2017
@author: gaiusyao
"""
from math import exp, log, sqrt

print("Hello world")

hello_world = "Hello world"
print(hello_world)
hello_world = "Hello Python world"
print(hello_world)

# int
x = 42
print("Output #1: {0}".format(x))
print("Output #2: {0}".format(3**4))
print("Output #3: {0}".format(int(8.1)/int(2.7)))
      
# float
print("Output #4: {0:.3f}".format(8.1/2.7))
y = 2.5 * 4.8
print("Output #5: {0:.1f}".format(y))
r = 8 / float(3)
print("Output #6: {0:.2f}".format(r))
print("Output #7: {0:.4f}".format(8.0/3))   

# math module
z = 6
print("Output #8: {0:.4f}".format(exp(z)))
print("Output #9: {0:.2f}".format(log(z)))
print("Output #10: {0:.1f}".format(sqrt(z)))    
     
# string eaxmple
print("Output #11: {0:s}".format('I\'m enjoying learning Python.'))
print("Output #12: {0:s}".format("This is a long string. Without the backslash\
it would run off of the page on the right in the text editor and be very\
difficult to read and edit. By using the backslash you can split the long\
string into smaller strings on separate lines so that the whole string is easy\
to view in the text editor."))
print("Output #13: {0:s}".format('''You can use triple single quotes
for multi-line comment strings.'''))
print("Output #14: {0:s}".format("""You can also use triple double quotes
for multi-line comment strings."""))     

# index
gaius_yao = "Product Manager"
gaius_yao[0]    # 'P'，字符串第一个字符
gaius_yao[2]    # 'o'，字符串第二个字符
gaius_yao[-1]   # 'r'，字符串最后一个字符
gaius_yao[:7]   # 'Product'，字符串前七个字符
gaius_yao[-7:]  # 'Manager'，字符串后七个字符

# split()
string1 = "My deliverable is due in May"
string1_list1 = string1.split()
string1_list2 = string1.split(" ",2)
print("Output #15: {0}".format(string1_list1))
print("Output #16: FIRST PIECE:{0}; SECOND PIECE:{1}; THIRD PIECE:{2}"\
.format(string1_list2[0], string1_list2[1], string1_list2[2]))
string2 = "Your,deliverable,is,due,in,June"
string2_list = string2.split(',')
print("Output #17: {0}".format(string2_list))
print("Output #18: {0} {1} {2}".format(string2_list[1], string2_list[5],\
string2_list[-1]))

# join()
print("Output #19: {0}".format(','.join(string2_list)))
     
# strip()
string3 = " Remove unwanted characters from this string.\t\t \n"
print("Output #20: string3: {0:s}".format(string3))
string3_lstrip = string3.lstrip()
print("Output #21: lstrip: {0:s}".format(string3_lstrip))
string3_rstrip = string3.rstrip()
print("Output #22: rstrip: {0:s}".format(string3_rstrip))
string3_strip = string3.strip()
print("Output #23: strip: {0:s}".format(string3_strip))

string4 = "$$Here's another string that has unwanted characters.__---++"
print("Output #24: {0:s}".format(string4))
string4 = "$$The unwanted characters have been removed.__---++"
string4_strip = string4.strip('$_-+')
print("Output #25: {0:s}".format(string4_strip))      

# replace()
string5 = "Let's replace the spaces in this sentence with other characters."
string5_replace = string5.replace(" ", "!@!")
print("Output #26 (with !@!): {0:s}".format(string5_replace))
string5_replace = string5.replace(" ", ",")
print("Output #27 (with commas): {0:s}".format(string5_replace))      

# lower()、upper()和capitalize()
string6 = "Here's WHAT Happens WHEN You Use lower."
print("Output #28: {0:s}".format(string6.lower()))
string7 = "Here's what Happens when You Use UPPER."
print("Output #29: {0:s}".format(string7.upper()))
string5 = "here's WHAT Happens WHEN you use Capitalize."
print("Output #30: {0:s}".format(string5.capitalize()))
string5_list = string5.split()
print("Output #31 (on each word):")
for word in string5_list:
    print("{0:s}".format(word.capitalize()))      
    
# len()
question = "the answer to life universe and everything"
print("The answer is {0}".format(len(question)))    