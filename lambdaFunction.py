#4	Write  problem codes to demonstrate usage of Lambda functions
# Python

#Programe to find smallest number
Min = lambda a,b: y if (a > b) else a
print("Minimum number is :- ",Min(345,456))
#OUTPUT:-
Minimum number is :- 345


# Program to find even number using  filter() with lambda()
List = [9, 11, 13, 12, 34, 33, 88, 11, 56, 77]
Filter1 = list(filter(lambda x: (x % 2 == 0), List))
print("List of even number :- ",Filter1)
"""OUTPUT:-
List of even number :-  [12, 34, 88, 56]
"""

# Program to get double of a Number using map() with lambda() .
l = [5, 7, 22, 24, 54, 62, 87, 24, 13, 31]
doublel = list(map(lambda x: x * 2, l))
print("List of double of a Number",doublel)
"""OUTPUT:-
List of double of a Number [10, 14, 44, 48, 108, 124, 174, 48, 26, 62]
"""

#Program to print table
table = [lambda x=x: x * 19 for x in range(1, 11)]
for t in table:
    print(t())
"""OUTPUT:-
11
22
33
44
55
66
77
88
99
110"""

#square of a number
square = lambda x: x **2
print("square :- ",cube(11))
"""OUTPUT:-
Cube :- 121
"""
#cube of a number
cube = lambda x: x **3
print("Cube :- ",cube(3))
"""OUTPUT:-
Cube :- 9
"""
