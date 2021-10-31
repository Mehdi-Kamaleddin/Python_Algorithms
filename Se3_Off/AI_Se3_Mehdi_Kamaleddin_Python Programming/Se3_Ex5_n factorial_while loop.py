#N factoriel using while loop

num=int(input('input a number: '))

i=1
total=1

while i<=num:
    total=total*i
    i=i+1

print("the num! is :",total)
