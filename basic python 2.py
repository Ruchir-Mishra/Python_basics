
"""Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords."""

#These Variable neames are legal
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Assign Multiple Values in variable
x, y, z = "value of x","value of y","value of z"
print (x) # will print value of x (whatever is wrtitten in "") and so on.
print (y)
print (z)

#one value to multiple variables
a = b = c = "equal sign is important"
print (a)#all 3 will print same values
print (b)
print (c)
########################### UNPACK A COLLECTION ########################
"""if you have collection of values in a list or tuple etc. python allows 
you to extract a variable. This is called unpacking. """
cartypes = ["sedan","suv","hatchback"]
e, f, g = cartypes
print (e) #will extract data and print  values
print (f)
print (g)

"""Very Important - 
if you put any thing in quotes and then type print command exact same value will be printed
see example"""
k = 5+2
print (k)#output will be 7 ie (sum of 5+2)

"""and now if i put the same mathematical operator in quotes ("")"""
m = "5+2"
print (m) #output will be 5+2 only.
#thats the importance of the quotes

#Print function for multiple variables
#seprated by commas
#for example 
a = "this"
b = "is complete"
c = "sentence"
print (a,b,c)# output will be this is complete sentence.
#seprated by + 
e = "this is "
f = "same " #you need to insert qoutes after space other wise words come closer (no_space)
g = "sentence"
print (e+f+g)#output will be this is same sentence.
"""for numbers the + operator will act as mathematics addition operator"""
p = 9
q = 3
r = 6
print (p+q+r)#the output will be 18.
#####IMPORTANT
"""In the print() function, when you try to combine a string and a number with the + operator
Python will give you an error:"""
x = 5
y = "string text"
#print (x+y)error!!!!!!!
#This willl give you the error try it.
#its better to seprate two diffrent type of variables using commas(,)
x = 5
y = "string text"
print (x,y)# right method to print x and y.
#more stuff in part 3.

