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
c = 20.5 # float, decimal point or exponent notation
d = 1j # complex number
e = True # boolean 
e_2 = False # boolean

list = [a, b, c, d, e, e_2] # list

printType(a)
printTypesList(list)


#Variables in python

num1 = 56
num2 = 12

num3 = num1 + num2

string1 = "God i want him so bad"
string2 = "Hi, my name is noel"

string3 = string1 + " " + string2 

float1 = 1.5

mixed = num3 + float1

same = 10
value = 10


#prints

print(num3)
print(string3)
print(mixed)
print(same == value) # True
print(same == 12)
print("\n")

##Operators in python
#Arithmetic: + - * / % ** //

x = 10
y = 3
print(x + y)  # addition operator
print(x - y)  # subtraction operator
print(x * y)  # multiplication operator
print(x / y)  # division operator
print(x % y)  # modulo operator (remainder)
print(x ** y) # exponent operator

#fun one

x = 10.56
y = 2

print(x // y) # floor division operator (rounds down[integer division])

#Comparison  == != > < >= <=

x = 10
y = 5
print(x > y)   # greater than operator
print(x < y)   # less than operator
print(x == y)  # equality operator
print(x != y)  # not equal operator
print(x >= y)  # greater than or equal to operator
print(x <= y)  # less than or equal to operator

#Logical 

x = True
y = False
print(x and y) # logical AND operator
print(x or y)  # logical OR operator
print(not x)   # logical NOT operator

#Assignment 

x = 10
x += 5  # equivalent to x = x + 5
print(x)

y = 3
y *= 2  # equivalent to y = y * 2
print(y)


##if-elif-else statements in python



