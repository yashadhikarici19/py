# 1.Program to show list comprehension

l = [ 'hello' , 'user' , 1 ]

for x in l:
    print(x , end=" ")
    
###############################
my_list=[]
my_list

###############################
my_list=[1,2,3]
my_list

###############################
my_list=[1,"hello", 3.4]
my_list

###############################
my_list=['c', 's', 'i' ,'t', 'a', 'c', 'r', 'o']
my_list[0]

##############################
my_list=['c', 's', 'i' ,'t', 'a', 'c', 'r', 'o', [2,0,1,3]]
my_list[-1][1]

##############################
my_list[2:5]

##############################
my_list[-1][1]= 9 #list are mutable
my_list

##############################
my_list.extend([9,11,14])
my_list

############################
print(my_list  + [11,12,13])

##########################
print(["hello"] *5)

##########################
my_list.insert(1, 90)
my_list

###########################
odd=[1]
my_list.append(odd)
my_list

###########################
my_list= [1,2,2,3,4,5,6,7,8,9]
my_list.remove(3)
my_list
_________________________________________________________________

# 2.Program to demonstrate Tuple

fruit = ("apple",)
fruit.append("hello") #gives error as tuples are immutable

x = list(fruit)
x.append("mango")
y = tuple(x)

###########################
my_tuple=()
my_tuple #or print(my_tuple)

###########################
my_tuple=(1,"hello",3.14)
my_tuple

#########################
#nested tuple
my_tuple=('house',[1,4,5],(3.14,5.5,60.5))
my_tuple

#########################
#unpacking
a,b,c=my_tuple
print(a," ",b," ",c)

########################
____________________________________________________________________

# 3.Program to demonstrate String in Python

s = "Hello friends chai pee lo! "
print(s)         #Hello friends chai pee lo!
print(s[4:10])   #o frie
print(s[1:15:2]) #el red 
print(s[::-1])   #!ol eep iahc sdneirf olleH
