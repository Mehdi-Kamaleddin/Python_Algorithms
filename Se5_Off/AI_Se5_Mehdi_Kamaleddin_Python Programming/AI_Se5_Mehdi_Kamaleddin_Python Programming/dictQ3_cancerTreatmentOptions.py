#Cancer Medical Treatment Approach Program by Python Dictionary Data Structure

adminsNo=int(input('How many patients do you want to register? '))

#REGISTRATION:
mypatients={}
n=0
while n < adminsNo:
    c=1
    for i in mypatients.keys():
        c+=1
    # mypatients["patient"+str(c)]=dict.fromkeys(mylist)
    
    print('------------------------------------')
    print("Patient Number",c,":")
    
    mypatients["patient"+str(c)]['name'] = input('Name '+str(c)+':')
    mypatients["patient"+str(c)]['age'] = int(input('Age '+str(c)+':'))
    mypatients["patient"+str(c)]['cancerType'] = input('Cancer Type '+str(c)+':')
    mypatients["patient"+str(c)]['cancerCondition'] = input('Benign/Malignant(B/M) '+str(c)+':')
    mypatients["patient"+str(c)]['stage'] = int(input('Stage(1,2,3,4) '+str(c)+':'))
    
    n+=1
print(mypatients)

#TREATMENT ADVICES:
for p in mypatients.keys():
    
    if mypatients[p]['cancerCondition']=='b':  #for benign conditions:
        if mypatients[p]['age'] < 50:
            if mypatients[p]['stage']== 1 or mypatients[p]['stage']== 2:
                print('The best treatment for',p,':','1-1')
            elif mypatients[p]['stage']==3:
                print('The best treatment for',p,':','2-1')
            else:
                print('The best treatment for',p,':','3-1')
        
        if mypatients[p]['age'] >= 50:
            if mypatients[p]['stage']== 1 or mypatients[p]['stage']== 2:
                print('The best treatment for',p,':','1-2')
            else:
                print('The best treatment for',p,':','2-2')

    else:  #for malignant conditions:
        if mypatients[p]['stage']== 1 or mypatients[p]['stage']== 2:
            print('The best treatment for',p,':','1-3')
        else:
            print('The best treatment for',p,':','2-3')


