import random
import statistics

# definition des variables globales
NBPARIS = 500
NBIT = 10000
choix = 'pair'
miseDep = 20
valeurs = ["pair", "impair", "0"]
proba = [18 / 37, 18 / 37, 1 / 37]

print("############ Martingale classique ############")
capitaux = []
faillites = 0
benefices = 0
for j in range(NBIT):
    capital = 1000
    mise = miseDep
    for i in range(NBPARIS):
        if capital - mise <= 0:
            faillites = faillites + 1
            break
        capital = capital - mise
        resultat = random.choices(valeurs, proba)
        if resultat[0] == 'pair':
            capital = capital + (mise * 2)
            mise = miseDep
        else:
            mise = mise * 2
    if capital > 1000:
        benefices = benefices + 1
    capitaux.append(capital)
moyenne = statistics.fmean(capitaux)
print("La moyenne des capitaux avec la méthode de la martingale est de ", moyenne, " et le maximum est", max(capitaux),
      ". le pourcentage de personnes qui ressortent sans argent est de ", (faillites * 100 / NBIT),
      "%. Et le pourcentages de personnes qui réalisent des bénéfices est de :", benefices * 100 / NBIT)
############


print("############ Fibonacci ############")
capitaux = []
faillites = 0
benefices = 0
for j in range(NBIT):
    capital = 1000

    mises = [miseDep]
    idx = 0
    mise = sum(mises)
    for i in range(NBPARIS):
        if capital - mise <= 0:
            faillites = faillites + 1
            break
        capital = capital - mise
        resultat = random.choices(valeurs, proba)
        if resultat[0] == 'pair':
            capital = capital + (mise * 2)
            idx = 0
            mises = [miseDep]
            mise = sum(mises)
        else:
            if idx == 0:
                mises.append(miseDep)
                idx = idx + 1
                mise = sum(mises)
            else:
                mises.append(mises[idx - 1] + mises[idx])
                idx = idx + 1
                mise = mises[idx - 1] + mises[idx]
    if capital > 1000:
        benefices = benefices + 1
    capitaux.append(capital)
moyenne = statistics.fmean(capitaux)
print("La moyenne des capitaux avec la méthode Fibonacci est de ", moyenne, " et le maximum est", max(capitaux),
      ". le pourcentage de personnes qui ressortent sans argent est de ", (faillites * 100 / NBIT),
      "%. Et le pourcentages de personnes qui réalisent des bénéfices est de :", benefices * 100 / NBIT)

############


print("############ Mise fixe ############")
capitaux = []
faillites = 0
benefices = 0
for j in range(NBIT):
    capital = 1000

    for i in range(NBPARIS):
        mise = miseDep
        if capital - mise <= 0:
            faillites = faillites + 1
            break
        capital = capital - mise
        resultat = random.choices(valeurs, proba)
        if resultat[0] == 'pair':
            capital = capital + (mise * 2)
    if capital > 1000:
        benefices = benefices + 1
    capitaux.append(capital)
moyenne = statistics.fmean(capitaux)
print("La moyenne des capitaux avec la méthode de la mise fixe est de ", moyenne, " et le maximum est", max(capitaux),
      ". le pourcentage de personnes qui ressortent sans argent est de ", (faillites * 100 / NBIT),
      "%. Et le pourcentages de personnes qui réalisent des bénéfices est de :", benefices * 100 / NBIT)

print("############ Mise proportionnelle ############")
capitaux = []
faillites = 0
benefices = 0
proportion = 0.1
for j in range(NBIT):
    capital = 1000
    for i in range(NBPARIS):
        mise = capital * proportion
        if capital - mise <= 0:
            faillites = faillites + 1
            break
        capital = capital - mise
        resultat = random.choices(valeurs, proba)
        if resultat[0] == 'pair':
            capital = capital + (mise * 2)
    if capital > 1000:
        benefices = benefices + 1
    capitaux.append(capital)
moyenne = statistics.fmean(capitaux)
print("La moyenne des capitaux avec la méthode de la mise fixe est de ", moyenne, " et le maximum est", max(capitaux),
      ". le pourcentage de personnes qui ressortent sans argent est de ", (faillites * 100 / NBIT),
      "%. Et le pourcentages de personnes qui réalisent des bénéfices est de :", benefices * 100 / NBIT)
