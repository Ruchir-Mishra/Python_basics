
"""Global Variables"""
#Variables created outside the function are called global variables

x = "Mosambi ka"#This is the global variable
 
def function1():
   print ("Juice pila do "+ x)    #juice pila do mosambi ka

function1()    

"""If you create any variable with same name inside the function,this vairable will be local
and can be only used inside the function."""
"""Global variable with the same name will remain as it was,global and with the orginal value"""

x = "best"

def function2():
   x = "game"
   print ("pacman is "+x)#Pacamn is best

   function2()

print ("Pacman is "+x)#Pacman is game

"""The global keyword"""   
"""Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

Example"""
def myfunc():
   global x 
   x = "fanta"

myfunc()

print(x+" is cold drink ") #now you can use global anywhere everyhwere

"""You can use global keyword to change the value of same variable1 inside a function"""
x = "outer value"

def newfunc():
   global x 
   x = "inner variable" #will give output this only if i put newfunc() again

print (x)#This will print outer value

newfunc()

print ("This is "+x)   #Output will be This is inner variable
   
"""Variables can store diffrenet data type """   