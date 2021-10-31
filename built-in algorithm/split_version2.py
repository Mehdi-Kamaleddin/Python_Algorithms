a = input("enter your number: ")
seperator = input("enter your seperator character: ")

mynum = []
i = 0
while i < len(a):
    b = a[i]
    i = i+1
    while a[i] != seperator:
        b = b+a[i]
        i = i+1
        if i == len(a):
            break
    mynum = mynum + [int(b)]
    i = i+1


print(mynum)
