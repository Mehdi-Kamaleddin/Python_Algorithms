
list1=["mahdi","amin",3,8,"mahdiiii",23,5,3]

for i in range(0,len(list1)):
    n=1
    while n < len(list1) and i!=n:
        if list1[i] ==list1[n]:
            print(list1[n])
            print("i is:",i , "and n is:", n)
            n=n+1
        else:
            n=n+1
