mutation_no=int(input("determine the number of mutation: "))
print("determine the type of mutaion: ")
print("1- point mutation (substitution) ")
print("2- Deletion mutation")
print("3- Insertion mutation ")
mutation_type=int(input())

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

#code for translation of native gene
protein=[]
while len(gseq)>=3:
    rib=gseq[0:3]
    for j in range(len(gcode)):
        if rib in gcode[j]:
            protein.append(aacode[j])
            break
    gseq=gseq[3:]
    if rib in stop:
        break

protein_seq="".join(protein)
print(protein_seq,"-----------original protein sequences")
#--------------------------------------------------------------------------------------------------

gseq= 'atgactgaatataaacttgtggtagttggagctggtggcgtaggcaagagtgccttgacgatacagctaattcagaatcattttgtggacgaatatgatccaacaatagaggattcctacaggaagcaagtagtaattgatggagaaacctgtctcttggatattctcgacacagcaggtcaagaggagtacagtgcaatgagggaccagtacatgaggactggggagggctttctttgtgtatttgccataaataatactaaatcatttgaagatattcaccattatagagaacaaattaaaagagttaaggactctgaagatgtacctatggtcctagtaggaaataaatgtgatttgccttctagaacagtagacacaaaacaggctcaggacttagcaagaagttatggaattccttttattgaaacatcagcaaagacaagacagagagtggaggatgctttttatacattggtgagagagatccgacaatacagattgaaaaaaatcagcaaagaagaaaagactcctggctgtgtgaaaattaaaaaatgcattataatgtaa'
print(len(gseq),"--------------length of original gseq")
gseq_list=list(gseq)

#code for randomly mutating the native gene
import random
mut_point_list=[]

a=0
while a < mutation_no:
    mutation_point=random.randint(0, len(gseq_list)-1)
    # if mutation_point not in mut_point_list:        #avoid repetitive mutation point
    #     mut_point_list.append(mutation_point)
    #     a+=1
    a=a+1
    DNA_3_nt=DNA_nt.copy()                      #list of our mutant nucleotide which want to be replaced with the original nuccleotide
    mutation_point_code=gseq_list[mutation_point]    #determine the nucleotide type of the genesequence mutation point where is our point of mutation
    DNA_3_nt.remove(mutation_point_code) #remove the original neocleotide type(where is in the mutation point), from the 4-nucleotide type list
    mutant_nucleotide=DNA_3_nt[random.randint(0,len(DNA_3_nt)-1)]   #random nucleotide between the remained nucleotide except the original nucleotide

    if mutation_type==1:
        gseq_list[mutation_point]=mutant_nucleotide #substitute the original bucleotide with the mutatnt one
    elif mutation_type==2:
        gseq_list.pop(mutation_point)
    else:
        gseq_list.insert(mutation_point, DNA_nt[random.randint(0, 3)]) #insert the mutatnt nucleotide in the place of the original one

mutated_gseq="".join(gseq_list)

print(mutated_gseq,"------ mutant gseq")
print(mut_point_list,"--------mut_point list")

print(len(mutated_gseq),"-----------length of mutated gene")
# #------------------------------------------------------------------------
# #determination of presence the repetitive mutation points in mut_point_list
# d=0
# n=0
# tek=[]
# for m in mut_point_list:
#     d=0
#     if m not in tek:
#         for c in range(mutation_no):
#             if m==mut_point_list[c]:
#                 d=d+1
    
#         if d >=2:
#             n=n+1
#             tek.append(m)

# print(tek,"tek")
# print(n,"tekrati")
# #---------------------------------------------------------------------------------------------------
#========================================================================
#translation of mutated genes

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
#==================================================================================

if mutated_pro_seq == protein_seq:
    print("Silent mutation")
elif len(mutated_pro_seq)==len(protein_seq) and mutated_pro_seq!=protein_seq:
    print("Missense mutation")
elif len(mutated_pro_seq)< len(protein_seq):
    print("Nonsense mutation")
else:
    print("Frameshift mutation ")
    for t in range(len(mutated_pro_seq)) :
        if t<len(protein_seq):
            if mutated_pro_seq[t]!=protein_seq[t]:
                print(t)