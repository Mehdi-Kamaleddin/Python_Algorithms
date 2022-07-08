import numpy as np
import pandas as pd

aaprop=pd.read_csv(r"C:\Users\mehdi\OneDrive\Desktop\AI_Python\Se9_Off\AminoAcidsProperties.csv")
aaprop
aa=[i for i in aaprop.loc[:,"Code"]]    #aminoacid 1 letter code
print(aa)

proNo=int(input("How many protein seq do you wnat to analyze?"))    #take the No of protein sequence from the user which want to be analyzed:
proseqList=[]   #list of protein sequences
i=1 #No of protein sequences
while i <= proNo:
    proseq=input("enter your "+str(i)+" protein seq: ")
    proseqList.append(proseq)
    invalidSeq=[]
    for j in proseq:    #checking if the user input the valid protein Codes
        if j not in aa:
            invalidSeq.append(j)

    if len(invalidSeq) !=0: #checking if the whole protein sequence is in its correct form
        print(invalidSeq)
        proseqList.pop(i-1) #eliminate the wrong protein sequence code
        i-=1

    i+=1
                
print(proseqList)

aaset=set(proseqList)
aaset.clear() #building an empty set to find the intersection of aminoacids of all the protein sequences

for i in proseqList:
    for j in i:
        aaset.add(j)

aalist=[i for i in aaset]
print(aalist)   #intersection of all aminoacids in all protein sequences
proProp=[["TOTAL len"]+aalist+['MW']+['AtomicFormula']]   #protein sequences total properties
print(proProp)

proSeqProp=pd.DataFrame(columns=proProp,index=proseqList)

for j in proSeqProp.index:#protein sequences
    proSeqProp.loc[j,"TOTAL len"]=len(j)    #length of each protein seq
    for i in aalist:
        proSeqProp.loc[j,i]=(j.count(i)/len(j))*100 #percentage of each aminoacid in each pro seq

        
print(proSeqProp)










