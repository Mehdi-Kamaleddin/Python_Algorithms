# Amino acids codons

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

gcodeStr=['phe1','leu2','ile3','met4','val5','ser6','pro7','thr8','ala9','tyr10',
        'his11','gln12','asn13','lys14','asp15','glt16','cys17','trp18','arg19','gly20']

aacode=['F','L','I','M','V','S','P','T','A','Y','H','Q','N','K','D','E','C','W','R','G']

gseq= 'atgactgaatataaacttgtggtagttggagctggtggcgtaggcaagagtgccttgacgatacagctaattcagaatcattttgtggacgaatatgatccaacaatagaggattcctacaggaagcaagtagtaattgatggagaaacctgtctcttggatattctcgacacagcaggtcaagaggagtacagtgcaatgagggaccagtacatgaggactggggagggctttctttgtgtatttgccataaataatactaaatcatttgaagatattcaccattatagagaacaaattaaaagagttaaggactctgaagatgtacctatggtcctagtaggaaataaatgtgatttgccttctagaacagtagacacaaaacaggctcaggacttagcaagaagttatggaattccttttattgaaacatcagcaaagacaagacagagagtggaggatgctttttatacattggtgagagagatccgacaatacagattgaaaaaaatcagcaaagaagaaaagactcctggctgtgtgaaaattaaaaaatgcattataatgtaa'

protein="MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQVVIDGETCLLDILDTAGQEEYSAMRDQYMRTGEGFLCVFAINNTKSFEDIHHYREQIKRVKDSEDVPMVLVGNKCDLPSRTVDTKQAQDLARSYGIPFIETSAKTRQRVEDAFYTLVREIRQYRLKKISKEEKTPGCVKIKKCIIM"


p={
   'F':{'codon': ['ttt', 'ttc'], 'name':'phe'},
   'L': ['tta', 'ttg', 'ctt', 'ctc', 'cta', 'ctg'],
   'I': ['att', 'atc', 'ata'],
   'M': ['atg'],
   'V': ['gtt', 'gtc', 'gta', 'gtg'],
   'S': ['tct', 'tcc', 'tca', 'tcg', 'agt', 'agc'],
   'P': ['cct', 'ccc', 'cca', 'ccg'],
   'T': ['act', 'acc', 'aca', 'acg'],
   'A': ['gct', 'gcc', 'gca', 'gcg'], 
   'Y': ['tat', 'tac'],
   'H': ['cat', 'cac'],
   'Q': ['caa', 'cag'],
   'N': ['aat', 'aac'], 
   'K': ['aaa', 'aag'],
   'D': ['gat', 'gac'],
   'E': ['gaa', 'gag'],
   'C': ['tgt', 'tgc'], 
   'W': ['tgg'],
   'R': ['cgt', 'cgc', 'cga', 'cgg', 'aga', 'agg'],
   'G': ['ggt', 'ggc', 'gga', 'ggg']
   }

proDictAminoNo=dict.fromkeys(aacode)
for i in protein:
    c=protein.count(i)
    contetn=c/len(protein)*100
    proDictAminoNo[i]="{:.2f}".format(contetn)
    
print(proDictAminoNo)

for i,j in proDictAminoNo.items():
    print(i,"content is:",j,"%")





