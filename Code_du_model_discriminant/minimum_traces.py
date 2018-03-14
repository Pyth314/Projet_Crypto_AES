from model_discriminant import *
import random
import numpy as np



# renvoie une liste de n indice compris entre 0 et 2999
def liste_contenu_ale(n,traces=traces):
	liste_indice=[]
	Liste_trace=[]
	Liste_plain_text=[]
	for i in range(0,n):
		N=random.randint(0,3000)
		while N in liste_indice:
			N = random.randint(0, 3000)
		liste_indice.append(N)
		Liste_trace.append(traces[N])
		Liste_plain_text.append(plaintext[N])
	return liste_indice,Liste_trace,Liste_plain_text


Liste_info_max=[(43, 53 ,0.0120477293996),(126, 118 ,0.0189586853827),(21 ,2113 ,0.0157706155446),(22, 317 ,0.0174460119363),(40 ,453 ,0.013325879048),(174 ,518 ,0.0172781568624),(210 ,2169 ,0.015950494713),(166 ,718 ,0.0179796145757),(171 ,917 ,0.013508896038),(247, 1997 ,0.0193363575042),(21 ,2477 ,0.0182781408814),(136 ,2957, 0.0204488045378),(9 ,1253 ,0.0138573463356),(207, 1781 ,0.0207237858424),(79 ,2265 ,0.0290595265543),(60 ,2742, 0.0359028394679)]

def Test_find_min(Nb_traces_deb_test,pourcentage_reussite_successive,traces=traces,plaintext=plaintext):
	Resultat_des_tests=[]

#	Liste_info_max=test_octect()
	Sortir_boucle_for=False
	for n in range(Nb_traces_deb_test,3000):
		print n
		liste_indice, Liste_trace, Liste_plain_text=liste_contenu_ale(n)
		Liste_info_max_local=test_octect(regle_model_subbytes,Liste_plain_text,Liste_trace)
		clef_trouvee=True
		Enssemble_de_test=[]

		compteur=0

		for i in range(0,len(Liste_info_max)):
			clef_pour_max, point_max, diff_au_bruit =Liste_info_max[i]
			clef_pour_max_local, point_max_local, diff_au_bruit_local=Liste_info_max_local[i]
			clef_trouvee= clef_pour_max==clef_pour_max_local
			Enssemble_de_test.append(clef_pour_max==clef_pour_max_local)
			Enssemble_de_test.append(point_max==point_max_local)
			Enssemble_de_test.append(abs(diff_au_bruit-diff_au_bruit_local))
		Resultat_des_tests.append((clef_trouvee,Enssemble_de_test))
		print "\n"
		print n
		print (clef_trouvee,Enssemble_de_test)
		if clef_trouvee :
			compteur+=1
			if compteur==int(pourcentage_reussite_successive*3000):
				Sortir_boucle_for=True
		else:
			dernier_indice_faux=n
			compteur=0
		if Sortir_boucle_for:
			break
	print Enssemble_de_test[dernier_indice_faux-10:dernier_indice_faux+2]
	return dernier_indice_faux

Test_find_min(100,0.005)

# Theoriquement cette algorythme finira par trouver le bon resultat mais cela rique d'etre tres long
# l ameliorer par recherche de dicotomie avec test de stabilite
