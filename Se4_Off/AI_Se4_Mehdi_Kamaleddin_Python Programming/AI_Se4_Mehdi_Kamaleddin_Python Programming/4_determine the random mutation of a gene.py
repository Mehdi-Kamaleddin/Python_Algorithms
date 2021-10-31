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

gseq_list=list(gseq)
gseq_copy=gseq_list.copy()


mutation_type=["substitution","deletion","insertion"]
import random

mutation_point=random.randint(0, len(gseq_copy))

mu_type=int(input("enter a number from 0 to 2: "))

mutant_nts=["a","c","g","t"]
nt_3_mutant=[]
changable_nt=gseq_copy[mutation_point]

for i in mutant_nts:
    if i != changable_nt:
        nt_3_mutant.append(i)
mutated_nt=nt_3_mutant[random.randint(0, len(nt_3_mutant)-1)]


if mu_type==0:
    gseq_copy[mutation_point]=mutated_nt
    print("the random mutation was, SUBSTITUTION")
elif mu_type==1:
    gseq_copy.pop(mutation_point)
    print("the random mutation was, DELETION")
else:
    gseq_copy.insert(mutation_point, mutated_nt)
    print("the random mutation was, INSERTION")
print(len(gseq_copy))

mutated_gseq="".join(gseq_copy)

mutated_protein=[]
i=0

while i <= len(mutated_gseq):       #ribosome movement
    rib=mutated_gseq[i:i+3 :]
    # print(rib)
    print(rib,"rib")
    if rib in stop or len(rib)<3:
        break
    j=0
    while j <= len(gcode):
        if rib in gcode[j]:
            mutated_protein.append(aacode[j])
            i+=3
            break
        else:
            j+=1
print(mutated_protein)
mutated_pro_seq="".join(mutated_protein)
print(mutated_pro_seq)
print("lenght of mutated pro is: ",len(mutated_pro_seq))

