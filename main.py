import random

nombre=random.randint(0,36)
capital=1000
mise=int(input("Entre la mise initiale : "))
capital=capital-mise
n=0
while(capital>0):
	nombre=random.randint(0,36)
	if(nombre%2 == 0):
		print("gg")
		capital =+ mise * 2
	elif (nombre==0 or nombre%2 != 0):
		print("perdu")
	print(nombre)
	n=+1

print("T'as perdu au bout de ",n,)