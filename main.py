#code to run examples

def printTypesList(list):
    for i in list:
        out = type(i)
        out = str(out).replace("<class '", "").replace("'>", "")
        print("Type of " + str(i) + " is: " + out)

def printType(inVar):
    print(str(type(inVar)).replace("<class '", "").replace("'>", "")
)


#This is how you comment in python, with a hashtag (#) the computer will ignore this line

#Data types in python 
a = "Hello World" # str
b = 20	# int
c = 20.5 # float
d = 1j # complex number
e = True # boolean 
e_2 = False # boolean

list = [a, b, c, d, e, e_2] # list

#printType(a)
#printTypesList(list)