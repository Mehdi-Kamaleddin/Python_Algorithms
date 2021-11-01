new_num=[21,45,78,45,65,85]

i=0
m=45

while i < len(new_num):
    if new_num[i]==m:
        new_num.remove(m)
        i=0
    else:
        i=i+1

print(new_num)
