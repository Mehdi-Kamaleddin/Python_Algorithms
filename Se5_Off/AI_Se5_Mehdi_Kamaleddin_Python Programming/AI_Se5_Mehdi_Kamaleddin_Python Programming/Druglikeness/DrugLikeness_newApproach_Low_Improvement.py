#PhysicoChemical Properties' Set:
myprop={'mw', 'logp', 'na', 'nd', 'rotbond','tpsa'}

#dictionary for Phisochemical Properties and their Pass-Values:s
mydictprop=dict.fromkeys(myprop)

#assign the intended molecule PhysicoChemical Properties' Value into the previous dictionary:
for i in mydictprop.keys():
    print('enter your','"',i,'":',end='')
    mydictprop.update({i:float(input())})

print(mydictprop)

##method1

#the top-3 PhisicoChemical Properties' Filters:
druglikeness={
    
    'Lipinski':{
        
        'mw': 500,
        'logp': 5,
        'na': 10,
        'nd': 5
        },
    
    'Veber':{
        
        'rotbond':10,
        'tpsa':140,
        },
    
    'Egan':{
        
        'logp':5.88,
        'tpsa':131.6
        }
    
    }

print('==================================================')

for filter in druglikeness.keys():
    print('-----------------------------------')
    print(filter,': ')
    p=0
    for i in druglikeness.get(filter).keys():
        if mydictprop[i]==0:    #if the intended molecule's properties does NOT meet the filter assessmets parameter:
            p+=1


    if p ==0:   #if the intended molecule "has" value for "all" the filter's parameter:( there is NO "0" for the filter's assessment parameter)
        filterViolation=[]
        for j in druglikeness.get(filter).keys():   #for the specific filter's parameter:
                if  mydictprop[j] >= druglikeness.get(filter)[j]: #if the molecule's parameter does NOT meet the standard properties' value:
                    filterViolation.append(j) #appebd the violant parameter to the empty list
                    
        if filterViolation==[]: #if all the molecule's parameter meet the standard filter's parameters:
            print(filter,'filter drug-likeness: YES')
        else:
            print('The UNMET Standard Parameters are',filterViolation) #if some of the molecule's parameters, does NOT meet the standard filter's parameters, print that violant parameter
            
    else:  #if the intended molecule "has NOT" value for "all" the filter's parameter:( there is "0" for the filter's assessment parameter)
        print('The molecule can NOT be evaluated by the',filter)


##----------------------------------------------------------------------------------------------------------
##method2
# propStrList=properties.split()

# for i in propStrList:
#     print(type(i))
# mw, logp, na, nd =int(propStrList[0]), int(propStrList[1]), int(propStrList[2]), int(propStrList[3], int(propStrList[4]))
# print(my,logp,na,nd)

# if mw <lipinski.get('mw') and logp<lipinski.get('logp') and na<lipinski.get('na') and nd<lipinski.get('nd'):
#     print('lipinski drug-likeness ACCEPTED')
# else:
#     print('lipinski drug-likeness REJECTED!!!!')
##-----------------------------------------------------------------------------------------------------------

