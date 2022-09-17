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

titan1=Titandex('Founding Titan',13,350) #erenTheGoat
titan2=Titandex('Attack Titan',15,275)
titan3=Titandex('Armored Titan',15,250)
titan4=Titandex('Colossal Titan',60,300)
titan5=Titandex('War Hammer Titan',15,235)
titan6=Titandex('Beast Titan',17,250)
titan7=Titandex('Cart Titan',4,175)
titan8=Titandex('Female Titan',14,270)
titan9=Titandex('Jaw Titan',5,225)

titan2.TitanvsScout('Levi',300)
titan2.TitanvsScout('Levi',300)
titan2.TitanvsScout('Mikasa',275)
titan2.TitanvsScout('Eren',270)
titan2.TitanvsScout('Armin',250)
titan2.TitanvsScout('Erwin',275)
titan2.TitanvsScout('Hange',230)
titan2.TitanvsScout('Jean',230)
titan2.TitanvsScout('Sasha',200)
titan2.TitanvsScout('Connie',180)

print(titan2.winningStreak)