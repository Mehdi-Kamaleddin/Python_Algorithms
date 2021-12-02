
with open(r'C:\Users\mehdi\OneDrive\Desktop\AI_Python\Se5_Off\AI_Se5_Mehdi_Kamaleddin_Python Programming\AI_Se5_Mehdi_Kamaleddin_Python Programming\keggDrugsUSA2.txt', 'r') as USAdrugs:

    usaDrug = USAdrugs.readlines()

    druglist = []
    companylist = []

    for i in usaDrug:
        druglinelist = i.split()
        print(druglinelist)
        # extracting drug name
        if druglinelist[2].isalpha():
            # if the 3rd column is alphabetic value (if the row has No ATC code, the drug name will be in 3rd column or indice number 2)
            druglist.append(druglinelist[2])
        else:
            # if there is an ATC code in 3rd column, the drug name will be in 4th column or indice number 3
            druglist.append(druglinelist[3])

        # extracting the company name
        if druglinelist[-1].isupper():
            if len(druglinelist[-2]) <= 3:
                # to concatenate the companies which has "Inc" in their name
                new = druglinelist[-3]+" "+druglinelist[-2]
                # if there is a remark value in the final column(indice -1), the company name will be in its previous column(inidce -2)
                companylist.append(new)

            else:
                companylist.append(druglinelist[-2])
        else:
            # if there is NOT a remark value in the last column, the company name will be in the last column (indice -1)
            companylist.append(druglinelist[-1])

    drugStr = "\n".join(druglist)

    companyStr = "\n".join(companylist)
    print(companyStr)

    company = []
    for j in companylist:
        if j not in company:
            company.append(j)

    for m in company:
        c = companylist.count(m)

        # print(m, "has developed: ", c, "new drug")


with open(r'C:\Users\mehdi\OneDrive\Desktop\AI_Python\Se5_Off\AI_Se5_Mehdi_Kamaleddin_Python Programming\AI_Se5_Mehdi_Kamaleddin_Python Programming\USAdrugsName.txt', 'w') as USAdrugname:
    USAdrugname.write(drugStr)

with open(r'C:\Users\mehdi\OneDrive\Desktop\AI_Python\Se5_Off\AI_Se5_Mehdi_Kamaleddin_Python Programming\AI_Se5_Mehdi_Kamaleddin_Python Programming\USAcompany.txt', 'w') as USAcompany:
    USAcompany.write(companyStr)
