#Faire liste des max de chaque bit-> mettre dans une liste le max des max
#Voir quel k_hypmax correspond à ce max du coup
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Le but ici est d'obtenir la clé avec les résultats de tous les bits.
#On regarde le max entre chaque max(i) pour chaque octet et donc max(i)[0] devient max[0]...
import numpy as np


from  traces_3516 import *




# On crée une liste de liste qui comprend les maximums de diff de chaque bit
maxi=[max1]+[max2]+[max3]+[max4]+[max5]+[max6]+[max7]+[max8]


k_hypmax=[k_hypmax1]+[k_hypmax2]+[k_hypmax3]+[k_hypmax4]+[k_hypmax5]+[k_hypmax6]+[k_hypmax7]+[k_hypmax8]


cle=[]


maxi=np.max(maxi,axis=0) 
print(maxi)

for i in maxi:
	
	if i in max1:
		print("C'est dans max1")
		ind=max1.index(i)
		
		cle.append(k_hypmax1[ind])

	elif i in max2:
		print("C'est dans max2")
		ind=max2.index(i)
		
		cle.append(k_hypmax2[ind])
	elif i in max3:
		ind=max3.index(i)
		print("C'est dans max3")
		cle.append(k_hypmax3[ind])
	elif i in max4:
		ind=max4.index(i)
		print("C'est dans max4")
		cle.append(k_hypmax4[ind])
	elif i in max5:
		ind=max5.index(i)
		print("C'est dans max5")
		cle.append(k_hypmax5[ind])
	elif i in max6:
		ind=max6.index(i)
		print("C'est dans max6")
		cle.append(k_hypmax6[ind])
	elif i in max7:
		ind=max7.index(i)

		print("C'est dans max7")
		cle.append(k_hypmax7[ind])
	elif i in max8:
		ind=max8.index(i)
		print("C'est dans max8")
		cle.append(k_hypmax8[ind])

print("La clé obtenu avec l'intervalle aléatoire est: ")
print(cle)



