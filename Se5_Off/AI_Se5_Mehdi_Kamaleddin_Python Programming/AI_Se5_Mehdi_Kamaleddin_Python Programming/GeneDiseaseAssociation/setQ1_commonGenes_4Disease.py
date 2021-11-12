
with open(r'C:\Users\mehdi\OneDrive\Desktop\AI_Python\Se5_Off\AI_Se5_Mehdi_Kamaleddin_Python Programming\AI_Se5_Mehdi_Kamaleddin_Python Programming\GeneDiseaseAssociation\Diabetes_Mellitus.txt','r') as diabetes:
    DMgenes=diabetes.readlines()
    
with open(r'C:\Users\mehdi\OneDrive\Desktop\AI_Python\Se5_Off\AI_Se5_Mehdi_Kamaleddin_Python Programming\AI_Se5_Mehdi_Kamaleddin_Python Programming\GeneDiseaseAssociation\Rheumatoid_Arthritis.txt','r') as arthritis:
    RAgenes=arthritis.readlines()

with open(r'C:\Users\mehdi\OneDrive\Desktop\AI_Python\Se5_Off\AI_Se5_Mehdi_Kamaleddin_Python Programming\AI_Se5_Mehdi_Kamaleddin_Python Programming\GeneDiseaseAssociation\Sjogren_Syndrome.txt','r') as sjogren:
    SjSgenes=sjogren.readlines()
    
with open(r'C:\Users\mehdi\OneDrive\Desktop\AI_Python\Se5_Off\AI_Se5_Mehdi_Kamaleddin_Python Programming\AI_Se5_Mehdi_Kamaleddin_Python Programming\GeneDiseaseAssociation\Dry_Eye_Syndrome_DSI.txt','r') as dryeye:
    DESgenes=dryeye.readlines()

#Top 100 genes according to their Scores
DM100=DMgenes[:100] 
RA100=RAgenes[:100]
SjS100=SjSgenes[:100]
DES100=DESgenes[:100]   #according to its DSI score
    
DMset=set(DM100)
RAset=set(RA100)
SjSset=set(SjS100)
DESset=set(DES100)

print('------------------------------------------')

DMcomRA=DMset.intersection(RAset)
print(len(DMcomRA),': No of Common Genes among DM & RA')

DMcomSjS=DMset.intersection(SjSset)
print(len(DMcomSjS),': No of Common Genes among DM & SjS')

DMcomDES=DMset.intersection(DESset)
print(len(DMcomDES),': No of Common Genes among DM & DES')

RAcomSjS=RAset.intersection(SjSset)
print(len(RAcomSjS),': No of Common Genes among RA & SjS')

RAcomDES=RAset.intersection(DESset)
print(len(RAcomDES),': No of Common Genes among RA & DES')

SjScomDES=SjSset.intersection(DESset)
print(len(SjScomDES),': No of Common Genes among SjS & DES')

print('--------------------------------------------')

with open(r'C:\Users\mehdi\OneDrive\Desktop\AI_Python\Se5_Off\AI_Se5_Mehdi_Kamaleddin_Python Programming\AI_Se5_Mehdi_Kamaleddin_Python Programming\GeneDiseaseAssociation\CommonGenesAmong4Diseases.txt','a') as final:
    
    final.write('Diabetics Mellitus commons with RA: \n')
    for i in DMcomRA :
        final.write(i)
    
    final.write('\n')
    final.write('Diabetics Mellitus commons with Sjogern Syndrome: \n')   
    for i in DMcomSjS :
        final.write(i)
        
    final.write('\n')    
    final.write('Diabetics Mellitus commons with Dry Eye Disease: \n')
    for i in DMcomDES :
        final.write(i)
        
    final.write('\n')      
    final.write('RA commons with Sjogren Syndrom: \n')
    for i in RAcomSjS :
        final.write(i)
        
    final.write('\n')        
    final.write('RA commons with Dry Eye Disease: \n')
    for i in RAcomDES :
        final.write(i)
        
    final.write('\n')   
    final.write('Sjogren commons with Dry Eye Disease: \n')
    for i in SjScomDES :
        final.write(i)


DMcomRAcomSjS=DMcomRA.intersection(DMcomSjS)
print(len(DMcomRAcomSjS),': No of Common Genes among DM & RA & SjS')

print('-------------------------------------------')

DMcomRAcomSjScomDES=DMcomRAcomSjS.intersection(DESset)
print(DMcomRAcomSjScomDES, 'is the ONE & ONLY common gene among 4 disease: DM, RA, SjS, DES')
print('-------------------------------------------')
print(DMcomRAcomSjScomDES,":\n","HLA class II histocompatibility antigen, DRB1-1 beta chain",'\n','\n','The only Approved Drug is:\n','Glatiramer')




















