#print command
print ("hello python")

#info about python version
import sys
print (sys.version)

#comments are  done with hash signn(#)


#PYTHON IDENTATION IS MUST
#Identation refers to leave spaces at begining of a code line
#Very Important without it code does not indicate block of code 
#if no idenatiton is there THE Python will show error.
#idenatiton using if condition
if 5>2:
    print("five is greater than two!")#atleast one line space is improtant (default four spaces)
#IMPORTANT - YOU HAVE TO USE SAME NO OF SPACES IN SAME BLOCK OF CODE OTHER WISE ERROR.

#TO DECLARE VARIABLES IN PYTHON
x = 5 #asigns the integer to the variable
y ="nice,command!"
# u can add multiple comments in comment line with using hash

"""

This is the comment 
writen in multline
string
"""
################################PYTHON VARIABLES###########################################
"""
variables are containers for storing data values
"""
print (x)#x and y variables are taken from the above variable decleration section and print command is being used here
print (y)

#Variables dont need to be decalred With any particular type
#they can be even changed after setting the values
a = 4 #an integer assigned for an example
b = "text inserted in string type" #b is now type str
print ("a")# prints a only
print (a) # print the value of a
print ("b")#prints b only
print (b)#prints the value of b
'''CASTING:-TO SPECIFY THE DATA TYPE OF VARIABLE'''
o = str(3) #str data type o will be '3'
p = int(3) #integer data type p will be 3
q = float(3) #float data type q will be 3.0
print (o)
print (p)
print (q)#floating data type called decimal

#GET THE TYPE OF THE FUNCTION BY PRINT COMMAND
#USING type() function
print (type(a))
print (type(p))
print (type(b))
print (type(q))
#this will tell you what is the class(cateorgry) of fucntion.x

#More IN part 2