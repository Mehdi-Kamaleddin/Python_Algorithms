#prime number detection using the while loop

num=int(input('your number: '))
n=1
m=0
while n< num:
    if num%n==0:
        n=n+1
        m=m+1
    else:
        n=n+1

if m==1:
    print('your number is prime')
else:
    print('sorry!')
