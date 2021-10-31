#Sum of the numbers from 1 to a given number inputted by a user with while loop
number=int(input('enter your number'))

n=1
summ=0

while n <= number:
    summ=summ+n
    n=n+1

print("the sum of 1 to the number is",summ)
    
