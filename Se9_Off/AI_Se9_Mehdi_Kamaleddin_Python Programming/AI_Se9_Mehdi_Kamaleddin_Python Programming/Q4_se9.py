import numpy as np
import pandas as pd
patientInfo=pd.read_csv(r"C:\Users\mehdi\OneDrive\Desktop\AI_Python\Se9_Off\AI_Se9_Mehdi_Kamaleddin_Python Programming\AI_Se9_Mehdi_Kamaleddin_Python Programming\new.csv")
# patientProp=['name','family', 'age','cancer type','benign/malignant (b/m)','stage']

# p=2 #number of patients which we want to register
# patientInfo=pd.DataFrame(columns=patientProp,index=[i for i in range(p)])  
# patientInfo=pd.DataFrame({input(i) for i in patientProp})
# total=0
patientInfo.index=patientInfo.iloc[:,0]
p=patientInfo.index
indexList=[]
for i in p:
    print(i)
    indexList.append(i)
c=len(indexList)

print(len(indexList))
for i in range(1,3):
    # total+=1
    for j in patientInfo.columns:
        if j == "age" or j=="stage":
            while True:
                try:
                    patientInfo.loc[i+c,j]=int(input(j + ": ")) 
                except:
                    print('this is not Number!!!!')
                else:
                    break
        
        else:
            patientInfo.loc[i+c,j]=input(j + ": ")
        
# for i in patientInfo.index:
#     if patientInfo.loc[i,"benign/malignant (b/m)"] == "m":
#         if patientInfo.loc[i,"age"]< 50:
#             if patientInfo.loc[i,"stage"]== 1 or patientInfo.loc[i,"stage"] ==2:
#                 patientInfo.loc[i,"treatment"]= '1-1'
            
#             elif patientInfo.loc[i,"stage"]==3:
#                 patientInfo.loc[i,"treatment"]='1-2'
#             else:
#                 patientInfo.loc[i,"treatment"]='1-3'
                
#         else:
#             if patientInfo.loc[i,"stage"]==1 or patientInfo.loc[i,"stage"]==2:
#                 patientInfo.loc[i,'treatment']='2-1'
#             else:
#                 patientInfo.loc[i,'treatment']='2-2'
#     else:
#         if patientInfo.loc[i,'stage']==1 or patientInfo.loc[i,'stage']==2:
#             patientInfo.loc[i,'treatment']='3-1'
#         else:
#             patientInfo.loc[i,'treatment']='3-2'   


 
patientInfo=patientInfo.iloc[:,1:]
patientInfo.to_csv(r"C:\Users\mehdi\OneDrive\Desktop\AI_Python\Se9_Off\AI_Se9_Mehdi_Kamaleddin_Python Programming\AI_Se9_Mehdi_Kamaleddin_Python Programming\new.csv")  
             
patientInfo

####for adding a new set of data from new patients which have been registered lately
# total-=1
# n=0/
# while n < 2:
#     total+=1
#     n+=1

#     for j in patientInfo.columns:
#         patientInfo.loc[total,j]=input(j)











