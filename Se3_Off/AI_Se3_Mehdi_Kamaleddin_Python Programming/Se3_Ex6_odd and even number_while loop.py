num=int(input("how many numbers do you want to detemine? "))
n=1 #counter for number of the items the user entered
numlist=[] #list of the entered numbers
even=0
odd=0
evenlist=[]
oddlist=[]

while n<=num:
    print(n)
    numlist=numlist+[int(input("enter your number: "))]
    n=n+1

print("your total list of entered numbers is: ",numlist)

i=0 #counter to iterate each item of the numlist
while i<num:
    if numlist[i]%2==0:
        even=even+1 #the no of even numbers
        evenlist=evenlist+[numlist[i]] #concatenate the even numbers with the evenlist
        i=i+1
    else:
        odd=odd+1 #the no of odd numbers
        i=i+1
        for j in numlist:                   #find the odd number to be added in oddlist by finding the 
            for i in evenlist:              #items which are in total numlist but not in evenlist
                if j!=i:
                    oddlist=oddlist+[j] #concatenate the odd numbers with oddlist
    

print('the no of even numbers is: ', len(evenlist))
print(evenlist)

print('the no of odd numbers is: ', len(oddlist))
print(oddlist)
