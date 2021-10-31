num="2 3 4 5 6 454"

summ=0
even=0
odd=0
listnum=[]
num=num.split(" ")
print(num)
for i in range(len(num)):
    listnum=listnum+[int(num[i])]
    
for j in range(len(listnum)):
    if listnum[j]%2==0:
        even=even+1
    else:
        odd=odd+1

        
print("num of odd is ",odd)
print("num of even is ", even)
summ=sum(listnum)
ave=summ/len(listnum)
print(listnum)
print("sum is",summ,"and","ave is",ave)

