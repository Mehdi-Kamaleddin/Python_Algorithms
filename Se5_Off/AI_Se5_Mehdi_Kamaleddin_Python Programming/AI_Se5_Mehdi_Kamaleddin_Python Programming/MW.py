<<<<<<< HEAD
molecule = input('enter your molecule formula: ')

# atomic weight dictionary:
atomW = {
    'c': 12.01,
    'h': 1,
    'o': 16,
    'n': 14,
    's': 32.06,
    'p': 30.97
}

molList = list(molecule)
print(molList)
print('molecular list len :', len(molList))

totalcalc = 0
i = 0
while i < len(molList):
    # if the indice of the number of each atom is less than the total length (before reaching to the end of the formula)
    if molList[i] in atomW and i+1 < len(molList):
        # if there is a numeric object after the atom, that would be the number of atom which should be multiplied by the atomic weight
        if molList[i+1] not in atomW:
            # if the number of atom is "2-digits" or more:
            number = []
            for j in range(i+1, len(molList)):
                if molList[j].isnumeric():
                    number.append(molList[j])
                else:
                    break
            intnumber = int("".join(number))
            print(intnumber)
            atomcalc = atomW[molList[i]] * intnumber
            totalcalc += atomcalc
            i += 1
        else:
            # if there will be just "one" atom, there is no numeric object after that atom
            atomcalc = atomW[molList[i]]
            totalcalc += atomcalc
            i += 1
    # if it reached to the last atom of the formula
    elif molList[i] in atomW and i+1 >= len(molList):
        atomcalc = atomW[molList[i]]
        totalcalc += atomcalc
        i += 1
    else:
        i += 1

print('total molecular weight is: ', totalcalc)
=======
myformula = '22'
print(myformula.isalpha())
>>>>>>> bfcb76f26c7db4ba66c5f462aa61d4c8f36912da
