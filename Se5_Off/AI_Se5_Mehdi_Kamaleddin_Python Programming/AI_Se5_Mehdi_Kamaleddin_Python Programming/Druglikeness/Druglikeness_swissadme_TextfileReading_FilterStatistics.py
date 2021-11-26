
with open(r'C:\Users\mehdi\OneDrive\Desktop\AI_Python\Se5_Off\AI_Se5_Mehdi_Kamaleddin_Python Programming\AI_Se5_Mehdi_Kamaleddin_Python Programming\Druglikeness\swissadme.txt', 'r')as drug:
    drugs = drug.readlines()

prprty = []
totaldrug = []

# the key:value which are the properties and their locations in the read textfile and appended in the 'totaldrug' list
myprop = {
    'name': 0,
    'mw': 3,
    'logp': 14,
    'na': 8,
    'nd': 9,
    'rotbond': 7,
    'tpsa': 11
}

for i in drugs:
    drugslist = i.split()
    totaldrug.append(drugslist)
    prprty.append(dict.fromkeys(myprop))

m = 0
while m < len(totaldrug):  # the number of all drugs in the list read from text file
    for i, j in myprop.items():  # assign each property=key and its value=value to the drugdict with the same "property name"=key (i) and its value which is attainable from its index no (j)
        # exampel: 3rd drug---> 'name'==3rd drug in total druglist, its value for the key 'name', is in index number '0'
        prprty[m][i] = totaldrug[m][j]

    m += 1

# print(totaldrug[2].index('61.44'))    -----> determine the index of the MW for example
# print(totaldrug[5])
# print(prprty[2])


druglikeness = {

    'Lipinski': {

        'mw': 500,
        'logp': 5,
        'na': 10,
        'nd': 5
    },

    'Veber': {

        'rotbond': 10,
        'tpsa': 140,
    },

    'Egan': {

        'logp': 5.88,
        'tpsa': 131.6
    }

}
approved = 0
rejected = 0
print('==================================================')
filterStatics = {
    'Lipinski': [],
    'Veber': [],
    'Egan': []
}

for drug in prprty:

    print('==================================================')
    print(drug['name'])
    for filter in druglikeness.keys():
        approved = 0

        print('----------------------------------')

        print(filter)

        filterViolation = []
        for property in druglikeness.get(filter).keys():
            if float(drug[property]) >= float(druglikeness.get(filter)[property]):
                filterViolation.append(property)

        # if all the molecule's parameter meet the standard filter's parameters:
        if filterViolation == []:
            print(filter, 'filter drug-likeness: YES')
            filterStatics[filter].append(drug['name'])

        else:
            # if some of the molecule's parameters, does NOT meet the standard filter's parameters, print that violant parameter
            print('The UNMET Standard Parameters are', filterViolation)


print('------------------------------------')
# how many drugs were well-defined by each filter?
# dictionary of the each filter which is tolerable with each drug
print(filterStatics)
for i, j in filterStatics.items():
    print(i, len(j))
