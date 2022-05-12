
import pandas as pd

ncl={'A','T','G','C','U'}
prop=['Abr','Code','AtomicNumber','MW','Solubility']
nclDic=dict.fromkeys(ncl)
print(nclDic)

# nclProp=pd.DataFrame(index=ncl,columns=prop)
# nclProp
nclProp=pd.DataFrame(nclDic,index=ncl,columns=prop)
nclProp
#########
# my=[i for i in nclprop.index]
# nclprop.loc[my,:]=[['Uracil','u',314,32453,52],['esrg0','fs',5653,3652,2355],['sbsb','f',25,35,35],['erg','r',5623,25,2],['esrr','h',25,25,25]]
# dict={
#       'A':{
#           'mw':24,
#           'atomic':45
#           },
#       'C':{
#           'mw':462,
#           'atomic':433535
#           }
#       }

# dicdic=pd.DataFrame(dict)
# dicdic
############
nclProp.loc['U', :]=['Uracil','u',314,32453,5552]
nuclProp=pd.read_csv(r'C:\Users\mehdi\OneDrive\Desktop\AI_Python\Se9_Off\AI_Se9_Mehdi_Kamaleddin_Python Programming\AI_Se9_Mehdi_Kamaleddin_Python Programming\nucleotidesProp.csv')
nuclProp













