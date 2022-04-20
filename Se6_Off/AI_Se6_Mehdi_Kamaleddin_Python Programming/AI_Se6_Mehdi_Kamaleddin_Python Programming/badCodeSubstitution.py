###version 1----------------------------------------------------------------------------
import random
def initial(seqq):
    new=[]
    n=0
    
    def reposition(digit,n):
        allowedLetter=['a','g','t','c']
        
        if digit not in allowedLetter:  #if the nucleotide is wrong--> substitute with the correct form
            new.append(allowedLetter[random.randint(0, 3)]) #substitute the wrong nucleotide with the random code in allowed code
            
            if n < len(seqq)-1:
                return reposition(seqq[n+1],n+1)    #go to the next nucleotide
       
        else:
            new.append(digit)   #if the nucleotide is correct--> append it to the new list
            
            if n <=len(seqq):
                return reposition(seqq[n+1],n+1)    #go to the next nucleotide
            
        print('modified sequence:  ',"".join(new))
        print('incorrect sequence: ',seqq)
    return reposition(seqq[n],n)

initial('sgrtgrmcccpm')

####version 2----------------------------------------------------------------------------
# import random
# def dnaCodeModifier(seqq,n):
#     allowedLetter=['a','g','t','c']     
#     if seqq[n] not in allowedLetter:
#         seqq[n]=allowedLetter[random.randint(0, 3)] #choosing a correct nucleotide through out the allowedLetter
#         n-=1 
#     else:
#         n-=1
#     if n < 0:   #if we reach to the end of sequence:
#         return seqq
#     return dnaCodeModifier(seqq,n)

# seqq='xxxtgax'
# n=len(seqq)-1
# print(dnaCodeModifier(list(seqq),n))

