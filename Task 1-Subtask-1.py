modern_family = ['CLaiRe_DunPhY', 'PHiL_dUnpHY', 'GLoRiA_PriTCheTt', 'CaMErOn_TuCKEr','StELLa']
characters=[]
indices=[]
print("start")
for index,char in enumerate(modern_family):
        indices.append(index)
        characters.append(char.lower().replace('_','-'))

func=lambda list:len(list)
temp=map(func,characters)       

indices=[sum(tuple) for tuple in zip(indices,temp)]

indices=sorted(indices, reverse=True)
Phew_finally={}

for key,value in zip(indices,characters):
   Phew_finally[key]=value
print(Phew_finally)

