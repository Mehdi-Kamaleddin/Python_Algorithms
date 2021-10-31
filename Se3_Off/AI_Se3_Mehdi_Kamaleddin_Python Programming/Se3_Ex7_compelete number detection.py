num=int(input('enter a number: '))
i=1
summ=0

while i <num: 
    if num%i==0: #i is the num devidands
        summ=summ+i #sum of the devidands of num
        print(i)
        i=i+1
        
    else:
        i=i+1

if summ==num: #compelete number condition
    print('your entered number ',num, ' is compelete')
else:
    print(num, ' is NOT copelete number')
