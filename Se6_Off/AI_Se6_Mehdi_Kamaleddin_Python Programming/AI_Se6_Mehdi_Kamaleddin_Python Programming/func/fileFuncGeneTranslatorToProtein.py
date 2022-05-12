def genetranslator(gseq: str) -> str :  #gene sequence as an input
    with open (r'C:\Users\mehdi\OneDrive\Desktop\AI_Python\Se6_Off\AI_Se6_Mehdi_Kamaleddin_Python Programming\excer\AAcodon.txt', 'r') as aacode:
        aalist=aacode.readlines()
        # print(aalist)
        
    AAsepList=[]
    for i in aalist:
        aasep=i.split('\t')
        AAsepList.append(aasep)
    for i in AAsepList:
        i[0]=i[0].lower()
    # print(AAsepList)
    stop=['taa','tag','tga']
    
    protein=[]
    i=0
    while i < len(gseq):       #ribosome movement
        rib=gseq[i:i+3 :]
        if rib in stop :
            break
        elif len(rib)<3:
            break
                    
        j=0
        while j < len(AAsepList):
            if rib in AAsepList[j]:
                protein.append(AAsepList[j][1])
                i+=3
                break
            else:
                j+=1
    # print(protein)
    protein_list="".join(protein)
    # print(protein_list)
    return protein_list
    
genetranslator('tatccgcctttaaatcgtaag')