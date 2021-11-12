string="   mahdi kamal  eddin eddAAAz ZbDDDDDDDcdef     ghijklmnop abadi"
string_list = list(string)

letter=input("enter your text value: ")
c=len(letter)

n=0
j=0
while j < len(string):
    p=string_list[j:j+c]
    pnew="".join(p)
    if letter==pnew:
        n+=1
        print("indexes of ",letter,"are: ",j,"-", j+c-1)
        j+=1
    else:
        j+=1
        
print("frequency of ","*",letter,"* :",n)