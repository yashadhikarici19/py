#Program to find digital sum of a given Number
#   ex: n=123  Digital sum----->1+2+3=6
num = int(input("Enter a number: "))
sum = 0
while num != 0 :
    sum = sum + num%10
    num = num//10
print(sum)
#####################################
#####################################
#Program to find the digital product of a given number
#   ex: n=43   Digital product ----->4*3=12

num = int(input("Enter a number: "))
prod = 1
while num != 0 :
    prod = prod * (num%10)
    num = num//10
print(prod)
