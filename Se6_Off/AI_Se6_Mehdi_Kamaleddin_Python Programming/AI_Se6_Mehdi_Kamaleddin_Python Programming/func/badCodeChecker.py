# ###wrong DNA code, harrasment and extract the "correct" DNA nucleotide sequences
# def badCodeChecker(letter:str)->bool:
#     allowedLetter=["A","G","T","C"]
#     return letter in allowedLetter


# def badCodeHarrasment(gseq):
#     correctgseq="".join(list(filter(badCodeChecker, gseq)))
#     print(correctgseq)  #show the correct form of a DNA nucleotide
    
# badCodeHarrasment("STBFNNLFKJDBUISVFNNCSERIUSENIKAKJALKNKAJCUICGBIUVC")

# ##-----------------------------------------------------------------------------------------
# ##extracting the "wrong" part of the DNA sequnece
# def CodeChecker(letter:str)->bool:  #return TRUE when a letter not be in allowed code
#     allowedLetter=["A","G","T","C", "u"]
#     return letter not in allowedLetter


# def wrongCodeExtractor(gseq):     #filter the bad codes in a gene sequences
#     badCodes="".join(list(filter(CodeChecker, gseq)))
#     print(badCodes)

# wrongCodeExtractor("STBFNNLFKJDBUISVFNNCSERIUSENIKAKJALKNKAJCUICGBIUVC")


###-----------------------------------------------------------------------------------------------
### define codeChecker function for both DNA and RNA /// the seqTypeChecker, provide INPUT for codeChecker function
###the filter function is designed by the codeChecker function which return the BOOLEAN value: True / False

def seqTypeChecker(seqType):    #seqType: dna    or     rna
    def codeChecker(letter):   #iterables from the sequence
        if seqType=='dna':
            allowedLetter=["A","G","T","C"]
        elif seqType=='rna':
            allowedLetter=["A","G", "C", "U"]
        else:
            print("Invalid sequence Type!!!")
        return letter in allowedLetter
        
    return codeChecker


def seqFilter(seqTYPE): #seqTYPE: dna or rna??
    seq="AEDOFIANHLVUISHYTRUIBGJS"
    filteredSeq="".join(list(filter(seqTypeChecker(seqType=seqTYPE), seq)))
    print(filteredSeq)



