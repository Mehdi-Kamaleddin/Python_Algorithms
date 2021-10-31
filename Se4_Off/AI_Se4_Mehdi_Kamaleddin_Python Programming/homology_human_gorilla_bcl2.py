bcl2_human="MAHAGRTGYDNREIVMKYIHYKLSQRGYEWDAGDVGAAPPGAAPAPGIFSSQPGHTPHPAASRDPVARTSPLQTPAAPGAAAGPALSPVPPVVHLTLRQAGDDFSRRYRRDFAEMSSQLHLTPFTARGRFATVVEELFRDGVNWGRIVAFFEFGGVMCVESVNREMSPLVDNIALWMTEYLNRHLHTWIQDNGGWDAFVELYGPSMRPLFDFSWLSLKTLLSLALVGACITLGAYLGHK"
print(len(bcl2_human))
bcl2_gorilla="MAHAGRTGYDNREIVMKYIHYKLSQRGYEWDAGDVGAVPPGAAPAPGIFSSQPGHTPHPAASRDRVARTSPLQTPAAPGAAAGPALSPVPPVVHLTLRQAGDDFSRRYRRDFAEMSSQLHLTPFTARGRFATVVEELFRDGVNWGRIVAFFEFGGVMCVESVNREMSPLVDNIALWMTEYLNRHLHTWIQDNGGWDAFVELYGPSMRPLFDFSWLSLKTLLSLALVGACITLGAYLGHK"
print(len(bcl2_gorilla))



bcl2_h=list(bcl2_human)
bcl2_g=list(bcl2_gorilla)

count=0
for i in range(len(bcl2_h)):
    if bcl2_h[i]!=bcl2_g[i]:
        count+=1
        print("the ",i,"th of the human AA is different from the gorilla's")
        print(bcl2_g[i]," in gorilla, mutated to the", bcl2_h[i] ,"in the human")


print("there are ",count, "different Aminoacids in human in comparison with gorilla")
print("the seuence identity is: ",(1-count/len(bcl2_h))*100, "%")

#=======================================================================================================

j=0
c=0
for aa in bcl2_human:
    if aa != bcl2_gorilla[j]:
        c+=1
        j=j+1
    else:
        j=j+1

print("ther are ",c ,"different Aminoacid in human in comparison with gorilla")
