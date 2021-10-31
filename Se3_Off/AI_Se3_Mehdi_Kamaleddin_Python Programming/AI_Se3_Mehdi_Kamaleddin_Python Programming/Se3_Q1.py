#Get and Print the First name, Last Name and Age of a Demanded Number of Patients
num=int(input('How many people do you want to identify?')) 

namelist=[]
familylist=[]
agelist=[]

for i in range (0,num):
    
    name=input('enter your name: ')
    namelist.append(name)
    

    family=input('enter your family name: ')
    familylist.append(family)

    age=input('enter your age: ')
    agelist.append(age)

j=0
while j<num:
    print(j+1," ", namelist[j], familylist[j], agelist[j])
    j=j+1
    
    
