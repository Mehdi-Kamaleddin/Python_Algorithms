#gene="atgactgaatataaacttgtggtagttggagctggtggcgtaggcaagagtgccttgacgatacagctaattcagaatcattttgtggacgaatatgatccaacaatagaggattcctacaggaagcaagtagtaattgatggagaaacctgtctcttggatattctcgacacagcaggtcaagaggagtacagtgcaatgagggaccagtacatgaggactggggagggctttctttgtgtatttgccataaataatactaaatcatttgaagatattcaccattatagagaacaaattaaaagagttaaggactctgaagatgtacctatggtcctagtaggaaataaatgtgatttgccttctagaacagtagacacaaaacaggctcaggacttagcaagaagttatggaattccttttattgaaacatcagcaaagacaagacagagagtggaggatgctttttatacattggtgagagagatccgacaatacagattgaaaaaaatcagcaaagaagaaaagactcctggctgtgtgaaaattaaaaaatgcattataatgtaa"

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


protein=[]
i=0
while i <= len(gseq):       #ribosome movement
    rib=gseq[i:i+3 :]
    # print(rib)
    if rib in stop:
        break
    j=0
    while j <= len(gcode):
        if rib in gcode[j]:
            protein.append(aacode[j])
            i+=3
            break
        else:
            j+=1

print(protein)              # KRAS protein aminoacid sequences
protein_list="".join(protein)
print(protein_list)
print(len(protein_list))    #numbner of aminoacids of KRAS protein 



print("====================================================================================")

while len(gseq)>=3:
    print(len(gseq))
    rib=gseq[0:3]
    
    for i in range (len(gcode)):
        for j in range(len(gcode[i])):
            if rib==gcode[i][j]:            #  wihout using the if sth in list:
                protein.append(aacode[i])
                gseq=gseq[3:len(gseq)]
                break
        
        
    if len(gseq)<=3:
        for m in range(len(stop)):
            if rib==stop[m]:
                gseq=gseq[3:len(gseq)]
                print("")
                break


print(protein)