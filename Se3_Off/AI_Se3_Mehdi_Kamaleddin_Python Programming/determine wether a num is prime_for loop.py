#prime number detection using the for loop
n=int(input())
j=0
for i in range (2,n):
    r=n%i
    j=j+1
    if r==0:
        print("sorry")
        break        

if j==n-2:
    print(n ,"is prime")
    
