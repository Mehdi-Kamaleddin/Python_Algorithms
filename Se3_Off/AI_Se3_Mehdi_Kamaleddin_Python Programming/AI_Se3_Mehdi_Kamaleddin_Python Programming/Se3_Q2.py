#Get the First name, Last Name, Age, PCR Report, Symptoms, Past Medical History   of a Demanded Number of Patients and Recommend a Suitable Treatment
num=int(input('How Many Patients are Administered?'))

namelist=[]
familylist=[]
agelist=[]
pcrlist=[]
covid_symplist=[]
historylist=[]

for i in range (0,num):
    
    name=input('enter your name: ')
    namelist.append(name)
    
    family=input('enter your family name: ')
    familylist.append(family)

    age=input('enter your age: ')
    agelist.append(age)

    pcr=input('resualt of PCR test: neg/pos ')
    pcrlist.append(pcr)
    
    covid_symp=input('Do you have any symptoms? yes/no ')
    covid_symplist.append(covid_symp)

    history=input('Do you have any past medical history? yes/no ')
    historylist.append(history)

for j in range(0,num):
    
    if pcrlist[j]=='neg':
        print ('Patient NO.',j+1, ' dos NOT have to visit a Doctor.')
    else:
        if int(agelist[j])<60:
            if historylist[j]=='no' and covid_symplist[j]=='no':
                print('Patient NO.', j+1, ' should be trated by Health Treatment 2')  
        else:
            if historylist[j]=="yes" or covid_symplist[j]=="yes" :
                print( 'Patient NO.', j+1, ' should be treated by Health Treatment 3')



