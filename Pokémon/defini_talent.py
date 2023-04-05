import csv

def parcours_talent():
	return csv.reader(open("Pokemon_talent_defini.csv","r", encoding='utf-8'), delimiter=",")
	
def defini_talent(talent):
	"""
    Fonction qui permet de chercher la définition d'un talent.
    
    Renvoie la définition de ce talent dans "Pokemon_talent_defini.csv".

    """
	talent_pokemon = parcours_talent()
	demande_talent = input("Entrez le Talent recherché: ")
	save = []
	resultat = []
	
	for ligne in talent_pokemon:
		if demande_talent in ligne[0]:
			resultat.append(ligne[0])
			save = ligne
	
	if resultat == []:
		return print("\nAucun Talent trouvé")
	
	elif len(resultat) == 1:
         return print(save[1])
	
	else:
		return print("Talent(s) trouvé(s): " + ', '.join(resultat))
		