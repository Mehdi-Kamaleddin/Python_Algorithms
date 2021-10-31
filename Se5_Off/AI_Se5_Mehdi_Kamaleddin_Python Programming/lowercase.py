alphlist_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphlist_lowercase = "abcdefghijklmnopqrstuvwxyz"
string = "RESTN WRNT RWYN  edth  DDDDDDDDDDDDD   hsrhtjhs    RTETTxxxxTTTTTTTTTT"

newname = []
for i in string:
    if i != " " and i not in alphlist_lowercase:
        indice = alphlist_uppercase.index(i)
        newname.append(alphlist_lowercase[indice])
    else:
        if i != " " and i in alphlist_lowercase:
            newname.append(i)

n = 0
while n < len(string):
    if string[n] == " ":
        newname.insert(n, " ")
        n += 1
    else:
        n += 1


new_name = "".join(newname)
print(new_name)
