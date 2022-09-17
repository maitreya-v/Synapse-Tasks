modern_family = ['CLaiRe_DunPhY', 'PHiL_dUnpHY', 'GLoRiA_PriTCheTt', 'CaMErOn_TuCKEr','StELLa']
characters=[]
indices=[]
for index,char in enumerate(modern_family):
        indices.append(index)
        characters.append(char.lower().replace('_','-'))
        
x=lambda list:len(list)
temp=map(x,characters)
# print(list(temp))
# temp_list=zip(indices,temp)
indices=[x+y for (x,y) in zip(indices,temp)]
# print(indices)
for x,y in zip(indices,temp):
        indices[x]=sum(y)
# print(indices)        
# print(x(modern_family))
indices=sorted(indices, reverse=True)
# print(indices)
Phew_finally={key:value for key,value in zip(indices,characters)}
print(Phew_finally)
# print(characters)        

