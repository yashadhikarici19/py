#2	Write a program to demonstrate Tuple in Python

# Creating tuple
T = ('Acro', 'Polis')
print (T)
"""OUTPUT:-
('Acro', 'polis')
"""
 
# Tuple summation
tup = (7, 8, 9, 1, 10, 7) 
sum1 = sum(list(tup))
print(" summ " + str(sum1)) 
 """OUTPUT:-
sum : 42 """
  
 
# printing the length of a tuple
print("\nLength of tuple is ",len(tup))
"""OUTPUT:-
Length of tuple is 6
"""

# creating nested tuples
tup3 = (tupl, T)
print("\nNested tuple:- ",tupl3)
"""OUTPUT:-
Nested tuple:-  (('Acro', 'polis'), (7, 8, 9, 1, 10, 7))
"""
