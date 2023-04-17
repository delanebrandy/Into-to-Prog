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
def dataTypes():
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
def variables():

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
def operators():
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


##Conditional statements
# if, elif, else


def conditions():
#if statement:
    x = 10
    if x > 5:
        print("x is greater than 5")

    #If-else statement:
    x = 3
    if x > 5:
        print("x is greater than 5")
    else:
        print("x is less than or equal to 5")

    #If-elif-else statement:
    x = 7
    if x < 0:
        print("x is negative")
    elif x == 0:
        print("x is zero")
    else:
        print("x is positive")

    #Nested if statements
    x = 10
    if x > 5:
        if x < 15:
            print("x is between 5 and 15")
            

    #all combined example

    value = int(input("Enter a number: "))
    if value > 0:
        
        print("x is positive")
        
        if value < 50:
            print("x is a small positive number")
            
        elif value < 100:
            print("x is a medium positive number")
            
        else:
            print("x is a large positive number")
            
    elif value == 0:
        print("x is zero")
        
    elif value < 0:
        print("x is negative")
        
    else:
        print("x is not a number")
    
##Loops
def loops():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)

    i = 1
    while i < 6:
        print(i)
        i += 1 # i = i + 1

    adj = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]

    for x in adj:
        for y in fruits:
            print(x, y)

    #break statement
    print("break statement")
    i = 1
    while i < 6:
        print(i)
        if i == 3:
            break
        i += 1
        
    fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

    for fruit in fruits:
        if fruit == "cherry":
            break
        print(fruit)


        
    #continue statement
    print("continue statement")
    i = 0
    while i < 6:
        i += 1
        if i == 3:
            continue
        print(i) 
        
    fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

    for fruit in fruits:
        if fruit == "cherry":
            continue
        print(fruit)


    #range function
    print("range function")
    for x in range(6):
        print(x)

##Functions
def functions():
    def greet(name):
        print("Hello, " + name + "!")

    greet("Alice")

    def square(x):
        return x * x

    print (square(4))


##NOEL EXAMPLE TIME


##Arrays (lists) in python
def arrays():

    fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

    print(fruits[0])  # prints "apple"
    print(fruits[1])  # prints "banana"

    fruits[2] = "pear"  # replace "cherry" with "pear"

    fruits.append("grape")  # add "grape" to the end of the list

    print(fruits)  # prints ["apple", "banana", "pear", "orange", "kiwi", "grape"]


#all the functions
def main():
    dataTypes()
    #variables()
    #operators()
    #conditions()
    #loops()
    #functions()
    #arrays()

if __name__ == "__main__":
    main()