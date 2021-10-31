#Sum of the numbers from 1 to a given number inputted by a user with for loop

n=int(input())
summ=0
for i in range(1,n):
    if n%i==0:
        summ=summ+i
print(summ)
