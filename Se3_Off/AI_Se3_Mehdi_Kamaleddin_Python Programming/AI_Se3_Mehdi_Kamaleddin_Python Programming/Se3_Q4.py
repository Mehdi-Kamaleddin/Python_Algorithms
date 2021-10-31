#Get the Name, Age, Cancer Type, Tumor Condition, Cancer Stage of a Given Number of Patients and Order the Suitable Treatment
n=int(input("how many patients do you want to administer? "))

namelist=[]
agelist=[]
cancertype=[]
tumorlist=[]
stagelist=[]

for i in range (n):
    print(i+1)
    
    namelist.append(input('your name: '))
    agelist.append(int(input('your age: ')))
    cancertype.append(input('your cancer type: '))
    tumorlist.append(input('if your tumor is benign enter <b> and if malignant, enter<m> : '))
    stagelist.append(int(input(' your cancer stage <1,2,3,4> : ')))

for i in range(n):
    if tumorlist[i]=='b':
        
        if agelist[i]<50:
            if stagelist[i]==1 or stagelist[i]==2:
                print(namelist[i], agelist[i], cancertype[i], stagelist[i], ', the Best treatment is 1-1')
            elif stagelist[i]==3:
                print(namelist[i], agelist[i], cancertype[i], stagelist[i], ', the Best treatment is 2-1')
            else:
                print(namelist[i], agelist[i], cancertype[i], stagelist[i], ', the Best treatment is 3-1')

        if agelist[i]>=50:
            if stagelist[i]==1 or stagelist[i]==2:
                print(namelist[i], agelist[i], cancertype[i], stagelist[i], ', should be treated by 1-2 guidline')
            else:
                print(namelist[i], agelist[i], cancertype[i], stagelist[i], ', shloud be treated by 2-2 guidline')

    else:
        if stagelist[i]==1 or stagelist[i]==2:
            print(namelist[i], agelist[i], cancertype[i], stagelist[i], ', shloud be treated by 1-3 guidline!!!')
        else:
            print(namelist[i], agelist[i], cancertype[i], stagelist[i], ', shloud be treated by 2-3 guidline!!!')













