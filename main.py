import random
import numpy as np
#definition des variables globales
NBIT = 500
choix = 'pair'

miseDep = 20
valeurs = ["pair", "impair", "0"]
proba = [18/37,18/37,1/37]
mise=miseDep
capitaux=np.array()
print("Martingale classique")
for j in range(10000):
	
	capitalCumule=0
	capital=1000
	for i in range(NBIT):

		capital=capital-mise
		if(capital<=0):
			#print("Plus d'argent au bout de", i,"iterations")
			break
		resultat = random.choices(valeurs,proba)
		if(resultat[0] == 'pair'):
			capital=capital+(mise*2)
			mise=miseDep
			#print("G", mise, capital)
		elif(resultat[0] == 'impair'):
			mise=mise*2
			#print("P",mise, capital)	
	capitaux.add(capital)
moyenne=capitaux.mean(capitaux,axis=None)
print(moyenne)
