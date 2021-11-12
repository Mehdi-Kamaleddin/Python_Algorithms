#Covid-19 PCR, Sypmtoms and treatment checker:
    
adminsNo=int(input('How many patients do you want to register? '))
mylist=['name','family','age','PCR','symptoms','pastMedicalHistory']

#REGISTRATION:

mypatients={}
n=0

while n < adminsNo:
    c=1
    for i in mypatients.keys():
        c+=1
    mypatients['patient'+str(c)]=dict.fromkeys(mylist)
    
    print("Patient Number",c,":")
    
    mypatients["patient"+str(c)]['name'] = input('Name '+str(c)+':')
    mypatients["patient"+str(c)]['family'] = input('Family '+str(c)+':')
    mypatients["patient"+str(c)]['age'] = int(input('Age '+str(c)+':'))
    mypatients["patient"+str(c)]['PCR'] = input('PCR Resault(n/p) '+str(c)+':')     #n:negative  p:positive
    mypatients["patient"+str(c)]['symptoms'] = input('symptoms(n/p) '+str(c)+':')
    mypatients["patient"+str(c)]['pastMedicalHistory'] = input('Past Medical History(n/p) '+str(c)+':')
    
    n+=1
    
#TREATMENT ADVICES:
for p in mypatients.keys():
    if mypatients[p]['PCR']=='n':
        print(p,'does NOT have to visit a doctor')
        
    else:
        if mypatients[p]['age'] < 60:
            if mypatients[p]['pastMedicalHistory']=='n' and mypatients[p]['symptoms']=='n':
                print(p, 'should be treated by Health Treatment 1')
                
            if mypatients[p]['pastMedicalHistory']=='p' and mypatients[p]['symptoms']=='p':
                print(p, 'should be treated by Health Treatment 2')
                
        else:
            if mypatients[p]['pastMedicalHistory']=='p' or mypatients[p]['symptoms']=='p':
                print(p, 'should be treated by Health Treatment 3')
    
        


    
    