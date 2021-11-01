alphlist_uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphlist_lowercase="abcdefghijklmnopqrstuvwxyz"
string="   mahdi kamal  eddin ezAAAz ZbDDDDDDDcdef     ghijklmnop abadi"
string_list=list(string)

n=0
while n < len(string):              #  n  is the index of the first word
    if string[n] != " " and n==0:
        break
    elif string[n] != " ":          # in case of that some of the first indices of the string are " ".
        break
    else:
        n+=1
print("first word index in your string is :", n)


if string[n] in alphlist_uppercase:
    print("the Capitalized format is as same as the original string: ",string)
else:
    indice=alphlist_lowercase.index(string[n])
    string_list[n]=alphlist_uppercase[indice]  # exchange the lower case of the first word with the upper one
    new_string="".join(string_list)
    print("the Capitalized format: ", new_string)
    
    
    
    
    
    
    
    
    