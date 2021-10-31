alphlist_uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphlist_lowercase="abcdefghijklmnopqrstuvwxyz"
string="mahdi kamal  eddin ezz abDDDDDDDcdef           ghijklmnop abadi"

newname=[]
for i in string:
    if i != " " and i not in alphlist_uppercase:
        indice=alphlist_lowercase.index(i)
        newname.append(alphlist_uppercase[indice])
    else:
        if i!=" " and i in alphlist_uppercase:
            newname.append(i)

n=0
while n < len(string):
    if string[n] ==" ":
        newname.insert(n, " ")
        n+=1
    else:
        n+=1


new_name="".join(newname)
print(new_name)