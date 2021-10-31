#sum of the 1-digit unmbers inouted by a user

numlist=input('enter your numbers seperated by space')
mynumlist=[]
n=0

while n<len(numlist):
    mynumlist=mynumlist+[int(numlist[n])]
    n=n+2

print(mynumlist)
print("sum of the numlist is: ", sum(mynumlist))
print('ave of the numbers is: ', sum(mynumlist)/len(mynumlist))

    
