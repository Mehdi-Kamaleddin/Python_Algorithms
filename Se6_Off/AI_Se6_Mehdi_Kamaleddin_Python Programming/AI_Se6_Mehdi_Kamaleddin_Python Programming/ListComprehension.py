# ########################## List Comprehension_Conditional Format_ONE LINE ######################################################################
# ## 1 :------------------------------------------------
# for num in range(1,10):
#     print(num)
    
# ## 2 :------------------------------------------------
# for num in range(1,10): print(num)

# ## 3 :------------------------------------------------
# newnum=[num*2 for num in range(1,10) if num%2==0]
# print(newnum)

# ## 4 :------------------------------------------------ similar to example 6
# print([i for i in "mahdi"])
     
# ### 5 :---------------------------------------------- similar to example 10  
# odd=[]   
# even=[] 
# for i in range(1,10): even.append(i) if i%2==0 else odd.append(i)
# print(odd,even)

# ### 6 :---------------------------------------------- similar to example 4      
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist=[x for x in fruits if x=='banana']
# print(newlist)

# ### 7 :----------------------------------------------       
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x+'---' if x!= 'banana' else x for x in fruits]
# print(newlist)

# ### 8 :---------------------------------------------- 
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]      
# newfruits=[]
# for i in fruits: newfruits.append(i) if i !='banana' else  i
# print(newfruits)

# ### 9 :----------------------------------------------  
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"] 
# newfruitsss=[]
# for f in fruits: f if f == 'banana' else newfruitsss.append(f)
# print(newfruitsss)

# ### 10 :----------------------------------------------  similar to example 5 
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]    
# goodfruits=[]
# badfruits=[]
# for i in fruits: goodfruits.append(i) if i != 'banana' else badfruits.append(i)
# print(goodfruits, badfruits)
    
# ################################ Nested For LOOP List Comprehension ONE LINE ###########################################################
# # ### 1 :----------------------------------------------    
# print([(i*j) for i in 'mahdi' for j in range(1,11)])

# ################################# Conditional Nsted For LOOP List Comprehension ONE LINE ###########################################################
# print([i*j for i in range (1,10)  for j in range (2,5) if i > 3 if j ==4])
    
    
    
    
    
    
    