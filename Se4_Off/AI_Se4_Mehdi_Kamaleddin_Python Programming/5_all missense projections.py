phe1 = ['ttt', 'ttc']
leu2 = ['tta', 'ttg', 'ctt', 'ctc', 'cta', 'ctg']
ile3 = ['att', 'atc', 'ata']
met4 = ['atg']
val5 = ['gtt', 'gtc', 'gta', 'gtg']
ser6 = ['tct', 'tcc', 'tca', 'tcg', 'agt', 'agc']
pro7 = ['cct', 'ccc', 'cca', 'ccg']
thr8 = ['act', 'acc', 'aca', 'acg']
ala9 = ['gct', 'gcc', 'gca', 'gcg']
tyr10 = ['tat', 'tac']
his11 = ['cat', 'cac']
gln12 = ['caa', 'cag']
asn13 = ['aat', 'aac']
lys14 = ['aaa', 'aag']
asp15 = ['gat', 'gac']
glt16 = ['gaa', 'gag']
cys17 = ['tgt', 'tgc']
trp18 = ['tgg']
arg19 = ['cgt', 'cgc', 'cga', 'cgg', 'aga', 'agg']
gly20 = ['ggt', 'ggc', 'gga', 'ggg']
stop = ['taa', 'tag', 'tga']

gcode = [phe1, leu2, ile3, met4, val5, ser6, pro7, thr8, ala9, tyr10,
         his11, gln12, asn13, lys14, asp15, glt16, cys17, trp18, arg19, gly20]
aacode = ['F', 'L', 'I', 'M', 'V', 'S', 'P', 'T', 'A',
          'Y', 'H', 'Q', 'N', 'K', 'D', 'E', 'C', 'W', 'R', 'G']

gseq = 'atgactgaatataaacttgtggtagttggagctggtggcgtaggcaagagtgccttgacgatacagctaattcagaatcattttgtggacgaatatgatccaacaatagaggattcctacaggaagcaagtagtaattgatggagaaacctgtctcttggatattctcgacacagcaggtcaagaggagtacagtgcaatgagggaccagtacatgaggactggggagggctttctttgtgtatttgccataaataatactaaatcatttgaagatattcaccattatagagaacaaattaaaagagttaaggactctgaagatgtacctatggtcctagtaggaaataaatgtgatttgccttctagaacagtagacacaaaacaggctcaggacttagcaagaagttatggaattccttttattgaaacatcagcaaagacaagacagagagtggaggatgctttttatacattggtgagagagatccgacaatacagattgaaaaaaatcagcaaagaagaaaagactcctggctgtgtgaaaattaaaaaatgcattataatgtaa'


protein_list = []
i = 0
while i <= len(gseq):  # ribosome movement
    rib = gseq[i:i+3:]
    # print(rib)
    if rib in stop:
        break
    j = 0
    while j <= len(gcode):
        if rib in gcode[j]:
            protein_list.append(aacode[j])
            i += 3
            break
        else:
            j += 1

print(protein_list)              # KRAS protein aminoacid sequences
protein_str = "".join(protein_list)
print(protein_str)
print(len(protein_str))  # numbner of aminoacids of KRAS protein

# ==========================================================================================


rib_no = int(len(gseq)/3)  # number of ribosome movement

gseq_gseq = []
for i in range(rib_no):
    gseq_gseq.append(gseq[i*3:i*3+3])  # devided gseq to 3-nucleotide form
n = 0
p = 0
while n < rib_no:  # n is the index number of 3-nucleotide
    gcode_copy = []
    gseq_copy = gseq_gseq.copy()
    trna = gseq_copy[n]  # trna codon
    print("tRNA: ", trna)  # trna codon checking

    i = 0
    while i < len(gcode):
        if trna in gcode[i]:
            gcode_copy = gcode.copy()  # everytime the gcode will be reseted
            # remove the aminoacid which was in the origical sequence
            gcode_copy.remove(gcode_copy[i])
            # everytime print the aminoacids which can be replaced by the original one
            print("gcode mutated codons: ", gcode_copy)
            break

        else:
            i = i + 1

    for m in gcode_copy:
        # this is one of the replacable aminoacids
        print("replacable aminoacids are: ", m)
        # m[0] is the first index of sequence of new aminoacid
        gseq_copy[n] = m[0]
        gseq_new_str = "".join(gseq_copy)
        print("this is the mutated gene sequence", gseq_new_str)
        p += 1  # p is the number of mutation in gene sequence
        # number of the first loop ---> the ribosom movement ==the number of tRNA which is being mutated
        print("n is :", n)
        print(p, "========================================================================")
    n += 1
