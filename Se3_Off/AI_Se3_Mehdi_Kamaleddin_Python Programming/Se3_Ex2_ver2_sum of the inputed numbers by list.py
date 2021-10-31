nums=[]
number=int(input('how many umbers do you want to calculate its sum & ave?: '))

n=1 #the number of items, which a user input

while n <=number:
    print(n) #printing n as a counter
    nums=nums+[int(input('enter your number'))]
    n=n+1
    
print('your list number is: ',nums)
print('the sum is: ', sum(nums))
print('the ave is: ', sum(nums)/number)
