titans=[]
class Titandex:
 def __init__(self,nameOfTitan, heightOfTitan, strengthOfTitan,winningStreak=0):
           self.nameOfTitan=nameOfTitan
           self.heightOfTitan= heightOfTitan
           self.strengthOfTitan=strengthOfTitan
           self.winningStreak=winningStreak
           titans.append(self)

 def TitanvsScout(self,nameOfScout,strengthOfScout):
  if(self.strengthOfTitan>strengthOfScout):
    self.winningStreak+=1
  else:
    self.winningStreak=0

 def TitanvsTitan(self):
    for titan in titans:
        if(titan.nameOfTitan!=self.nameOfTitan):
            if(self.strengthOfTitan>titan.strengthOfTitan):
                self.winningStreak+=1
            else:
                self.winningStreak=0       
    
haha=Titandex('Founding Titan',13,350)
# hehe=Titandex('Attack Titan',15,275)
# haha=Titandex('Armored Titan',15,250)
# haha=Titandex('Colossal Titan',60,300)
# haha=Titandex('War Hammer Titan',15,235)
hehe=Titandex('Beast Titan',17,250)
# haha=Titandex('Cart Titan',4,175)
# haha=Titandex('Female Titan',14,270)
# haha=Titandex('Jaw Titan',5,225)

haha.TitanvsScout('Levi',300)
haha.TitanvsScout('Mikasa',275)
haha.TitanvsScout('Eren',270)
haha.TitanvsScout('Armin',250)
haha.TitanvsScout('Erwin',275)
haha.TitanvsScout('Hange',230)
haha.TitanvsScout('Jean',230)
haha.TitanvsScout('Sasha',200)
haha.TitanvsScout('Connie',180)

hehe.TitanvsTitan()
# hehe.TitanvsTitan()
# hehe.TitanvsTitan()
# hehe.TitanvsTitan()
# hehe.TitanvsTitan()
# hehe.TitanvsTitan()
# hehe.TitanvsTitan()
# hehe.TitanvsTitan()
# hehe.TitanvsTitan()


print(haha.winningStreak)
print(hehe.winningStreak)