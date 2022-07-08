import numpy as np
import pandas as pd
nuclProp=pd.read_csv(r'C:\Users\mehdi\OneDrive\Desktop\AI_Python\Se9_Off\AI_Se9_Mehdi_Kamaleddin_Python Programming\AI_Se9_Mehdi_Kamaleddin_Python Programming\nucleotidesProp.csv')
nuclProp
nuclProp.index=nuclProp.iloc[:,0]
prop=['seq','len','A','C','G','T','U','GC content','MW','pro']
seqList=[]
nucleotides=['a','c','g','t','u']


###obtaining 3 valid sequence from user
i=1
while i< 4:
    seq=input('enter your '+str(i)+' seq:')
    seqList.append(seq) #appending seq to seqList (list of user's sequences)

    for j in seq:       #checking each nucleotide if it's a member of valid nucleotides 'A C G T U' or not
        if j not in nucleotides:
            seqList.pop(i-1)    #if a nucleotide in user's seq was out of valid nucleotides, pop it from the "sequence list"
                                #i-1 --> index of the invalid seq which has to be ommited
            print('invalid seq:'+"  "+j)    #raise this note 
            i-=1                    #again get a sequence from user
            break                   #go to the while loop
    
    i+=1            #if the condition in "for loop" did not execute, get the next sequence from user
    

print(seqList)
seqProp=pd.DataFrame(columns=prop)
seqProp.iloc[:,0]=[i for i in seqList]

seqProp

import fileFuncGeneTranslatorToProtein as translator

p=0
for i in seqProp.iloc[:,0]:
    ####Method1 START:
    seqProp.iloc[p,1]=len(i)
    seqProp.iloc[p,1]=len(i)
    seqProp.iloc[p,2]=i.count('a')
    seqProp.iloc[p,3]=i.count('c')
    seqProp.iloc[p,4]=i.count('g')
    seqProp.iloc[p,5]=i.count('t')
    seqProp.iloc[p,6]=i.count('u')
    seqProp.iloc[p,7]=np.sum((seqProp.iloc[p, 3:5].values))/np.sum((seqProp.iloc[p,2:7].values)) #seqProp.iloc[0,:] type is: series, then we can use "numpy" modules to use the method: np.sum(array) to calculate the sum of items in an array
    total=0
    ####Method1 END.
    
    ####Method2 START:by using "for loop", counting each element of the nucleotide in a DNA sequences
    # q=2
    # for j in nucleotides:
    #     seqProp.iloc[p,q]=i.count(j)
    #     q+=1
    ####Method2 END.
    
    seqProp.iloc[p,7]=np.sum((seqProp.iloc[p, 3:5].values))/np.sum((seqProp.iloc[p,2:7].values)) #seqProp.iloc[0,:] type is: series, then we can use "numpy" modules to use the method: np.sum(array) to calculate the sum of items in an array
    
    total=0
    for n in seqProp.columns[2:7]:
        for m in nuclProp.index:
            if n==m:
                total+=seqProp.loc[p,n]*nuclProp.loc[n,'dNMP']
                
    seqProp.iloc[p,8]=total#calculating total molecular weight of a gene seq
    seqProp.iloc[p,9]=translator.genetranslator(seqProp.iloc[p,0])#translating gene seq to protein seq
    p+=1

print(seqProp)





