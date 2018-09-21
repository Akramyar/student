letters=('A','C','B','B','C','A','C','C','B')
lettersA=letters.count('A')
lettersB=letters.count('B')
lettersC=letters.count('C')
lst=[lettersA, lettersB, lettersC]
print(lst)

lst=[3, 7, -2, 12]
print(max(lst)-min(lst))


cijferICOR=7.0
cijferPROG=8.0
cijferCSN=7.0
gemiddelde=round((cijferICOR + cijferPROG + cijferCSN)/3,2)
beloning='€' + str(cijferICOR*30+cijferPROG*30+cijferCSN*30)
overzicht='Mijn cijfers (gemiddeld een '+ str(gemiddelde) +')'+'leveren een beloning van ' + (beloning) + ' op!'
print(overzicht)



