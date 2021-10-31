alphlist_uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphlist_lowercase="abcdefghijklmnopqrstuvwxyz"
string="mahdi kamal  eddin ezAAAz ZbDDDDDDDcdef           ghijklmnop abadi"
string_list=list(string)

n=0
myindice_firstwords=[]
while n < len(string):                          # find the first digits' indexes of the words in a string (each word seperated by 1 or >1 spaces)
    if string[n] ==" " and string[n+1]!=" ":    # find the first digits' indexes of the words except the first word
        myindice_firstwords.append(n+1)
        n+=1
    elif string[n]!=" " and n==0:               # find the first digits' index of the first word of the string if its index=0
        myindice_firstwords.append(n)
        n+=1
    else:
        n+=1
print("the first digits' indexes of each word in the given string: ",myindice_firstwords)

for i in myindice_firstwords:
    if string[i] not in alphlist_uppercase:     # exchange the lower case of the first digits' words of the given string  with the upper one
        indice=alphlist_lowercase.index(string[i])
        string_list[i]=alphlist_uppercase[indice]

new_string="".join(string_list)

print("primary format of string: ", string)
print("Titled format of string:  ",new_string)
