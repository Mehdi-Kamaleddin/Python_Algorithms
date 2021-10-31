phe1=['ttt','ttc']
leu2=['tta','ttg','ctt','ctc','cta','ctg']
ile3=['att','atc','ata']
met4=['atg']
val5=['gtt','gtc','gta','gtg']
ser6=['tct','tcc','tca','tcg','agt','agc']
pro7=['cct','ccc','cca','ccg']
thr8=['act','acc','aca','acg']
ala9=['gct','gcc','gca','gcg']
tyr10=['tat','tac']
his11=['cat','cac']
gln12=['caa','cag']
asn13=['aat','aac']
lys14=['aaa','aag']
asp15=['gat','gac']
glt16=['gaa','gag']
cys17=['tgt','tgc']
trp18=['tgg']
arg19=['cgt','cgc','cga','cgg','aga','agg']
gly20=['ggt','ggc','gga','ggg']
stop=['taa','tag','tga']

gcode=[phe1,leu2,ile3,met4,val5,ser6,pro7,thr8,ala9,tyr10,
        his11,gln12,asn13,lys14,asp15,glt16,cys17,trp18,arg19,gly20]
aacode=['F','L','I','M','V','S','P','T','A','Y','H','Q','N','K','D','E','C','W','R','G']

gseq= 'atgactgaatataaacttgtggtagttggagctggtggcgtaggcaagagtgccttgacgatacagctaattcagaatcattttgtggacgaatatgatccaacaatagaggattcctacaggaagcaagtagtaattgatggagaaacctgtctcttggatattctcgacacagcaggtcaagaggagtacagtgcaatgagggaccagtacatgaggactggggagggctttctttgtgtatttgccataaataatactaaatcatttgaagatattcaccattatagagaacaaattaaaagagttaaggactctgaagatgtacctatggtcctagtaggaaataaatgtgatttgccttctagaacagtagacacaaaacaggctcaggacttagcaagaagttatggaattccttttattgaaacatcagcaaagacaagacagagagtggaggatgctttttatacattggtgagagagatccgacaatacagattgaaaaaaatcagcaaagaagaaaagactcctggctgtgtgaaaattaaaaaatgcattataatgtaa'

DNA_nt=["a","c","g","t"]    #DNA nucleotide
DNA_nt_copy=DNA_nt.copy()

import random
print(DNA_nt_copy)



gseq_list=list(gseq)
gseq_list_copy=gseq_list.copy()

deletion_mu=int(input("No of DELETION mutation: "))
insertion_mu=int(input("No of INSERTION mutation: "))
insertion_no=int(input("No of insertion Code: "))
substitution_mu=int(input("No of SUBSTITUTION mutation: "))


mutated_gseq=gseq_list_copy

m=0
while m <deletion_mu:
    mut_point=random.randint(0, len(mutated_gseq))
    print(mut_point,"mut point1")
    mutated_gseq.pop(mut_point-1)
    print(len(mutated_gseq),"length of gene1")
    m=m+1

j=0
while j < insertion_mu:
    mut_point=random.randint(0, len(mutated_gseq))
    print(mut_point,"mutpoint2")

    inser_code=[]                               #this is for insert a sequence with n code in a specific point of the mutated gene
    for n in range(insertion_no):
        inser_code.append(DNA_nt[random.randint(0, 3)])
    inser_code_str="".join(inser_code)
    print(inser_code_str,"insertion")
    mutated_gseq.insert(mut_point,inser_code_str)
    mutated_gseq_str="".join(mutated_gseq)
    mutated_gseq=list(mutated_gseq_str)
    print(len(mutated_gseq),"length of gene2")
    j=j+1

print(mutated_gseq)
i=0
while i < substitution_mu:
    mut_point=random.randint(0, len(mutated_gseq))
    print(mut_point,"mut point")
    DNA_3=["a","c","g","t"]
    DNA_3.remove(mutated_gseq[mut_point])
    mutated_gseq[mut_point]=DNA_3[random.randint(0, 2)]
    i=i+1

print(len(mutated_gseq_str))
#===================================================================================================

#protein translation
mutated_pro=[]
c=0
while c <= len(mutated_gseq_str):       #ribosome movement
    rib=mutated_gseq_str[c:c+3 :]
    print(rib,"rib")
    if rib in stop :
        break
    d=0
   
    while d <= len(gcode):
        if rib in gcode[d]:
            mutated_pro.append(aacode[d])
            c+=3
            break
        else:
            d+=1

print(mutated_pro)
mutated_pro_str="".join(mutated_pro)
print(mutated_pro_str)
print("lenght of mutated pro is: ",len(mutated_pro_str))