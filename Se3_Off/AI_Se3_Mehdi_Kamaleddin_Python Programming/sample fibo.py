n=int(input())
prev1=0
prev2=1
last=0

for i in range(n):
    last=prev1+prev2
    print(last)
    prev1=prev2
    prev2=last
    
