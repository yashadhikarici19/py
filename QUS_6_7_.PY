""" 
6	Write a Python program to calculate the length of a string
7	Write a Python program to parse a string to Float & Integer
"""
def que_6():
    s = "Hello friends! Chai pi loo."
    print("Length of string '"+s+"' is ",len(s))
#Output: Length of string 'Hello friends! Chai pi loo.' is  27

def que_7():
    a = "65841"
    b = "123.45"
    c = int(a)
    d = float(b)
    print( type(a), type(b), type(c), type(d) )
#Output:  <class 'str'> <class 'str'> <class 'int'> <class 'float'>
