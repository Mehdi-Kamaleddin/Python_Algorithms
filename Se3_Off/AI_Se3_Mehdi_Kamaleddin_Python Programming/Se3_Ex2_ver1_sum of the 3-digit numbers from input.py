nums=input('input your numbers:(maximum with 3-digit followed by a space) ')
mylist=[]


for i in range(len(nums)):
    

    #seperate the 3-digit numbers
    if nums[i]!=" " and nums[i+1]!=" " and nums[i+2]!=" ":
        mylist=mylist+[nums[i]+nums[i+1]+nums[i+2]]
        
    #seperate the 2-digit numbers
    elif nums[i]!=" " and nums[i+1]!=" " and nums[i+2]==" " and nums[i-1]==" ":
        mylist=mylist+[nums[i]+nums[i+1]]
        
    #seperate the 1-digit numbers
    else:
        if nums[i]!=" " and nums[i+1]==" " and nums[i-1]==" ":
            mylist=mylist+[nums[i]]

print('your list of numbers is: ',mylist)
print('your item numbers in your list is: ',len(mylist))

summ=0
for i in range(len(mylist)):
    summ=summ+int(mylist[i])
    
print('the sum of the numbers are: ',summ)
print(' the avereage of the numbers is: ', summ/len(mylist))
