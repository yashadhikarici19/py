# Find the sum of the series 3 +33 + 333 + 3333 + .. n terms
n = int(input("Enter number of terms: "))
sum = 0
series = 0
while n:
    series = series*10 + 3
    sum = sum + series
    n-=1
    ###############
######################
print(sum)#Print the following pattern
#   *
#   * *
#   * * *
#   * * * *
#   * * * * *
#   * * * *
#   * * *
#   * *
#   *

for i in range(1,6):
    print(i*"* ")
for i in range(6,10):
    print( (10-i)*"* ")
    
      ###############
##########################
#Program to reverse a given Number.    ex: n=123   Reversed no is 321
num = int(input("Enter a number: "))
rev = 0
while num != 0:
    rev = (rev*10) + (num%10)
    num = num//10

print(rev)
