# def evenNumChecker (num:int)-> bool:
#     if num %2==0:
#         return True

#     else:
#         return False
    
# mynumbers=[1,32,45,5,43,45,54,42,28,2,2]
# items=filter(evenNumChecker, mynumbers)   
# for item in items:
#     print(item)
    
    
###Example2:------------------------------------------------------------------------------------
# customers={
       
#         'person 1':{'name':'mahdi',
#                   'age':24}
#         ,
            
#         'person 2':{'name':'ahmad',
#                   'age':23}
#         }

# ages=[]
# for i in customers:
#     ages.append(customers.get(i).get('age'))
# print(ages) #extracing each custmer age and append them in a list variable named: "ages"

# valids=filter(evenNumChecker, ages)
# print(valids)   #check each number in the ages variable as are even or odd

# #detecting the customer whose age is even:
# for i in valids:
#     for j in customers.keys():
#         if customers.get(j).get('age')==i:
#             print(j,"is ",i, " years old")


####version1_Example 3:-----------------------------------------------Filter a protein sequence by specific PROTEIN LETTER:
# def pro(letter):    #letter is the alphabet which we want to detect in a protein sequence
#     def Profilter(seq):
#         if seq==letter:
#             return True
#     return Profilter


# def filteredd(letter):
#     proseq="KSNPSBOPLSPBPSLBGNDNB" 
#     filtered=list(filter(pro(letter), proseq))
    
#     print(filtered)
   
# filteredd("P")
    
##################################################################################################################################
####version2_Example 3:--------------------------------------------find the specific PROTEIN INDICE in a protein sequence:

# indices=[]
# def initial(letter,proseq,n=0): #letter is the Protein alphabetic name, which we want to determine its index in a "proseq": protein sequence:
#                                 #"n": the protein sequnece indice No.
#     if proseq[n]==letter:
#         indices.append(n)

#     if n<len(proseq)-1:
#         return initial(letter,proseq,(n+1))     #recursive function to find the next "demanded Protein" in a protein sequence
#     print(indices)
    

# initial('P',"KSNPSBOPLSPBPSLBGNDNB" )


