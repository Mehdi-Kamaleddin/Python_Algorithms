n=int(input())
for i in range (1,n+1): #i is the single number from 1 to n, which we want to know if i is compelete number or not
    summ=0
    for j in range (1,i): #j is the devidands of i
        if i%j==0:
            summ=summ+j
            
    #print (summ)
    if summ==i:
        print("this is compelete",i)
        
    
