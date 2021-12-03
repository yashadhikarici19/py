
"""
1	Display float number with 2 decimal places using print()
2	Takes two integer numbers and  return their product.
3	Write a Python program to get the volume of a sphere with radius 10.
4	Accept two numbers from the user and multiply them together.
5	Write a Python program that accepts an integer (a) and computes the value of a+aa+aaa.

"""
def que_1():
    x  = 111.3345
    print(round(x,2))
#output: 111.33

def que_2(a , b):
    return a*b
#Output: 10

def que_3(radius):
    volume = 4/3*3.14*radius**3
    print(round(volume,2))
#Output: 4186.67

def que_4():
    a = int( input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    print(a*b)
#Output: Enter 1st number: 5
#        Enter 2nd number: 8
#        40

def que_5():
    a = input("Enter a number: ")
    res = int(a) + int(a+a) + int(a+a+a)
    print(res)
#Output: Enter a number: 4
#        492




que_1()
product = que_2(4,5)
print(product)
que_3(10)
que_4()
que_5()
