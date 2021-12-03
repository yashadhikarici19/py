def hello(name):
    print("Hello, " + name + "!")
hello('Harshit')

#Hello Jessy!

######################
def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num
print(absolute_value(2))
print(absolute_value(-4))

#2
#4
############################

def my_func():
	x = 20
	print("Value inside function:",x)
x = 40
my_func()
print("Value outside function:",x)

#Value inside function: 20
#Value outside function: 40

############################

def greet(name, msg):
    print("Hello", name + ', ' + msg)
greet("Harshit", "Good Morning")

#Hello Jessy, Good Morning

############################
def factorial(x): #Recursion
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 3
print("The factorial of", num, "is", factorial(num))

#The factorial of 6 is 6

###########################
#The output shows an error because we are trying to access a local variable y in a global scope whereas the local variable only works inside var() or local scope.
def var():
    y = "local"
var()
print(y)

##################################
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()

#inner: nonlocal
#outer: nonlocal
