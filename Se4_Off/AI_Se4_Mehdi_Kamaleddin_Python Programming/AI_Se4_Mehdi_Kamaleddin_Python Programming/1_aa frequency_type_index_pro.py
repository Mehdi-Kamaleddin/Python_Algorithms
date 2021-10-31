protein="MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQVVIDGETCLLDILDTAGQEEYSAMRDQYMRTGEGFLCVFAINNTKSFEDIHHYREQIKRVKDSEDVPMVLVGNKCDLPSRTVDTKQAQDLARSYGIPFIETSAKTRQRVEDAFYTLVREIRQYRLKKISKEEKTPGCVKIKKCIIM"

aacode=['F','L','I','M','V','S','P','T','A','Y','H','Q','N','K','D','E','C','W','R','G']

for i in aacode:
    indices=[]
    print("---------------------------------------------------------------------------------------------------------")
    n=0
    m=0
    while n < len(protein):
        if protein[n]== i:
            indices.append(n)
            n+=1
            m+=1
        else:
            n+=1
    print("number of ",i, "in protein is",m)
    print("the indexes of",i," are: ",indices)
