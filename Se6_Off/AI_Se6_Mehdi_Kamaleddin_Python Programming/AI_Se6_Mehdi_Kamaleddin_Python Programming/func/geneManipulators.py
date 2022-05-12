
def gene_translator(gseq: str) -> str :
    
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
    
###version 1----------------------------------------------------------------------------------------------------
    protein=[]
    i=0
    while i < len(gseq):       #ribosome movement
        rib=gseq[i:i+3 :]
        if rib in stop:
            break
        elif len(rib)<3:
            break
                    
        j=0
        while j < len(gcode):
            if rib in gcode[j]:
                protein.append(aacode[j])
                i+=3
                break
            else:
                j+=1
    
    # print(protein)              # KRAS protein aminoacid sequences
    protein_list="".join(protein)
    return protein_list
    # print(protein_list)
    # print(len(protein_list))    #numbner of aminoacids of KRAS protein 
    
    
    
###version2-------------------------------------------------------------------------------------------
    # protein=[]
    # while len(gseq)>=3:
    #     rib=gseq[0:3]
        
    #     for i in range (len(gcode)):
    #         for j in range(len(gcode[i])):
    #             if rib==gcode[i][j]:            #  wihout using the if sth in list:
    #                 protein.append(aacode[i])
    #                 gseq=gseq[3:len(gseq)]
    #                 break
            
            
    #     if len(gseq)<=3:
    #         for m in range(len(stop)):
    #             if rib==stop[m]:
    #                 gseq=gseq[3:len(gseq)]
    #                 print("")
    #                 break
    
    
    # print(protein)


###-----------------------------------------------------------------------------------------------------------------

def reverse_transcription(protein:str) -> str:
    
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
        
    print(len(protein))
    
    codon=[]  
    n=0
    
    for i in protein:
        for n in range(len(aacode)):
            if i==aacode[n]:
                codon.append(gcode[n][0])
                
    print(codon)
    codon.append(stop[0])
    codon_original="".join(codon)
    print(codon_original)
    print(len(codon_original))
    
    
    
###------------------------------------------------------------------------------------------------------------
# def mutatedgenetranslator(gseq:str, mutype:int, munum:int) -> str:
def gene_mutator(gseq:str, substitution:int, deletion:int, insertion:int) -> str:

    """
    munum=int(input("determine the number of mutation: "))
    print("determine the type of mutaion: ")
    print("1- point mutation (substitution) ")
    print("2- Deletion mutation")
    print("3- Insertion mutation ")
    mutype=int(input())
    """
    mutationProcess={
        
        1:substitution,
        2:deletion,
        3:insertion
        }
    
    DNA_nt=["a","c","g","t"]    #DNA nucleotide
    
    print(len(gseq),"--------------length of original gseq")
    gseq_list=list(gseq)
    
###version 1----------------------------------------------------------------------------------------
    gseqCopy=gseq_list.copy()
    #code for randomly mutating the parent gene
    import random
    for keys in mutationProcess:
        if keys ==1 and mutationProcess[keys] !=0:
            for num in range(mutationProcess[keys]):
                
                mutation_point=random.randint(0, len(gseqCopy)-1)
                print('substitution mutation',mutation_point)
                mutation_point_code=gseq_list[mutation_point]    #determine the nucleotide type of the genesequence mutation point where is our point of mutation
                DNA_3_nt=DNA_nt.copy()                      #list of our mutant nucleotide which want to be replaced with the original nuccleotide
                DNA_3_nt.remove(mutation_point_code) #remove the original neocleotide type(where is in the mutation point), from the 4-nucleotide type list
                mutant_nucleotide=DNA_3_nt[random.randint(0,2)]   #random nucleotide between the remained nucleotide except the original nucleotide
                gseqCopy[mutation_point]=mutant_nucleotide #substitute the original bucleotide with the mutatnt one
                
            
        elif keys==2 and mutationProcess[keys] !=0:
            for num in range(mutationProcess[keys]):
                mutation_point=random.randint(0, len(gseqCopy)-1)
                print('deletion mutation',mutation_point)
                gseqCopy.pop(mutation_point)
        
        else:
            for num in range(mutationProcess[keys]):
                mutation_point=random.randint(0, len(gseqCopy)-1)
                print('insertion mutation',mutation_point)

                gseqCopy.insert(mutation_point, DNA_nt[random.randint(0, 3)]) #insert the mutatnt nucleotide in the place of the original one

    mutated_gseq="".join(gseqCopy)
    return mutated_gseq     #mutated gene


# ###version 2----------------------------------------------
#     import random
#     a=0
#     while a < munum:
#         mutation_point=random.randint(0, len(gseq_list)-1)
#         # if mutation_point not in mut_point_list:        #avoid repetitive mutation point
#         #     mut_point_list.append(mutation_point)
#         #     a+=1
#         a=a+1
#         DNA_3_nt=DNA_nt.copy()                      #list of our mutant nucleotide which want to be replaced with the original nuccleotide
#         mutation_point_code=gseq_list[mutation_point]    #determine the nucleotide type of the genesequence mutation point where is our point of mutation
#         DNA_3_nt.remove(mutation_point_code) #remove the original neocleotide type(where is in the mutation point), from the 4-nucleotide type list
#         mutant_nucleotide=DNA_3_nt[random.randint(0,len(DNA_3_nt)-1)]   #random nucleotide between the remained nucleotide except the original nucleotide
    
#         if mutype==1:
#             gseq_list[mutation_point]=mutant_nucleotide #substitute the original bucleotide with the mutatnt one
#         elif mutype==2:
#             gseq_list.pop(mutation_point)
#         else:
#             gseq_list.insert(mutation_point, DNA_nt[random.randint(0, 3)]) #insert the mutatnt nucleotide in the place of the original one
    
#     mutated_gseq="".join(gseq_list)
    
#     print(mutated_gseq,"------ mutant gseq")
#     print(len(mutated_gseq),"-----------length of mutated gene")
    
###--------------------------------------------------------------------------------------------------

def mutation_type(gseq: str, mutated_gseq: str)->str:
    """
    
    Parameters
    ----------
    gseq : str
        original gene sequence
    mutated_gseq : str
        mutated gene sequence, obtained from gene_utator function

    Returns
    original and mutated protein and type of the mutation which has occured
    str

    """
    
    import geneManipulators
    originalPro=geneManipulators.gene_translator(gseq)
    print(originalPro,'Original Pro')
    mutatedPro=geneManipulators.gene_translator(mutated_gseq)
    print(mutatedPro,'Mutated Pro')
    
    if mutatedPro == originalPro:
        print("Silent mutation")
    elif len(mutatedPro)==len(originalPro) and mutatedPro != originalPro:
        print("Missense mutation")
    elif len(mutatedPro)< len(originalPro):
        print("Nonsense mutation")
    else:
        print("Frameshift mutation ")
        for t in range(len(mutatedPro)) :
            if t<len(originalPro):
                if mutatedPro[t]!=originalPro[t]:
                    print(t)
    
    
    
    
    