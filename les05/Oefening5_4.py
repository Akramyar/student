getallenrij=[3, 6, 9, 12, 4]
deelbaar3=0
for getal in getallenrij:
    if getal %3==0:
        deelbaar3=deelbaar3+1
print('Het aantal getallen deelbaar door 3 is '+str(deelbaar3))
