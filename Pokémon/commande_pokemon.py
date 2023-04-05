import csv


"""
def tout():

    for ligne in stats_pokemon:
        affichage_pokemon(ligne)
"""



def test_doublons(liste):
    
    resultat = [] # Liste contenant tout les noms des pokémons trouvés
    id_prec = 0
    id_act = 1
    
    for ligne in liste: # Parcours du fichier des stats
        
        id_act = ligne[0]
        
        if id_act == id_prec:
            resultat.append(id_act)
            
        id_prec = id_act
    
    return resultat
        

def parcours_stats():
    """
    Retourne la commande pour ouvrir et lire le fichier "Stats_pokemon_5g.csv".

    """
    return csv.reader(open("Stats_pokemon_5g.csv", "r", encoding='utf-8'), delimiter=",")


def parcours_talent():
	return csv.reader(open("Pokemon_talent_defini.csv","r", encoding='utf-8'), delimiter=",")


def affichage_pokemon(liste):
    """
    liste -- liste contenant toute les stats d'un pokémon'
    
    Permet d'afficher proprement les stats d'un pokémon.

    """
    print("\nID: "+ liste[0])
    print("Pokémon: "+ liste[1])
    print("Type: "+ liste[2])
    print("Talent: "+ liste[3])
    print("PV: "+ liste[4])
    print("Attaque: "+ liste[5])
    print("Défense: "+ liste[6])
    print("Atq Spécial: "+ liste[7])
    print("Déf Spécial: "+ liste[8])
    print("Vitesse: "+ liste[9])
    print("Génération: "+ liste[10])


def recherche_id(id_pkm):
    """
    Fonction qui permet de rechercher un pokémon par son ID du Pokédex.
    
    Renvoie les stats du pokémon seulement si trouvé dans "Stats_pokemon_5g.csv".
    -- ou --
    Renvoie les noms des pokémons si plusieurs ID associé à la demandes de l'utilisateur.

    """
    stats_pokemon = parcours_stats() # Ouverture du fichier des stats
    resultat = [] # Liste contenant tout les noms des pokémons trouvés
    save = [] # Liste contenant toute les stats du dernier pokémon trouvé
        
    for ligne in stats_pokemon: # Parcours du fichier des stats

        if id_pkm == ligne[0]:
            resultat.append(ligne[1])
            save = ligne
    
    return resultat, save
            

def recherche_nom(nom_pkm):
    """
    Fonction qui permet de rechercher un pokémon par son nom dans le Pokédex.
    
    Renvoie les stats du pokémon seulement si trouvé dans "Stats_pokemon_5g.csv".
    -- ou --
    Renvoie les noms des pokémons similaires à la demandes de l'utilisateur.

    """
    stats_pokemon = parcours_stats() # Ouverture du fichier des stats
    resultat = [] # Liste contenant tout les noms des pokémons trouvés
    save = [] # Liste contenant toute les stats du dernier pokémon trouvé
    
    for ligne in stats_pokemon: # Parcours du fichier des stats
        
        if nom_pkm == ligne[1]:
            resultat = [ligne[1]]
            save = ligne
            
            return resultat, save
        
        elif nom_pkm in ligne[1]:
            resultat.append(ligne[1])
            save = ligne

    return resultat, save
            

def recherche_type(type1,type2):
    """
    Fonction qui permet de rechercher des pokémons par leur(s) type(s).
    
    Renvoie le nom des pokémon possedant ce(s) type(s) dans "Stats_pokemon_5g.csv".

    """
    stats_pokemon = parcours_stats() # Ouverture du fichier des stats
    resultat = [] # Liste contenant tout les noms des pokémons trouvés

    for ligne in stats_pokemon: # Parcours du fichier des stats
    
        if type1 in ligne[2] and type2 in ligne[2]:
            resultat.append(ligne[1])
    
    return resultat


def recherche_talent(talent1,talent2,talent3):
    """
    Fonction qui permet de rechercher des pokémons par leur(s) talent(s).
    
    Renvoie le nom des pokémon possedant ce(s) talent(s) dans "Stats_pokemon_5g.csv".

    """
    stats_pokemon = parcours_stats()
    resultat = [] # Liste contenant tout les noms des pokémons trouvés

    for ligne in stats_pokemon: # Parcours du fichier des stats
    
        if talent1 in ligne[3] and talent2 in ligne[3] and talent3 in ligne[3]:
            resultat.append(ligne[1])
    
    return resultat
    

def definition_talent(talent):
	"""
    Fonction qui permet de chercher la définition d'un talent.
    
    Renvoie la définition de ce talent dans "Pokemon_talent_defini.csv".

    """
	talent_pokemon = parcours_talent()
	save = []
	resultat = []
	
	for ligne in talent_pokemon:
		if talent == ligne[0]:
			resultat.append(ligne[0])
			save = ligne
	
	return resultat, save



def pokedex():
    
    print("\nBienvenue dans le pokédex !")
    
    while True:
        d_entrer = input("\nQue voulez-vous rechercher ?\n- Pokémon -\n- Talent -\n- Quitter -\n\n=> ")
        
        if d_entrer == "Pokémon":
            
            d_recherche = input("\nQuel type de recherche voulez-vous effectuer ?\n- ID -\n- Nom -\n- Type -\n- Talent -\n\n=> ")
            
            
            if d_recherche == "ID":
                
                demande_id = input("\nEntrez l'ID du pokémon recherché: ")
                res, sa = recherche_id(demande_id)
                
                if res == []:
                    print("\nAucun Pokémon trouvé")
        
                elif len(res) == 1: # Si un seul pokémon trouvé
                    affichage_pokemon(sa)
                
                else:
                    print("\nPokémon(s) trouvé(s): " + ', '.join(res))
            
            
            elif d_recherche == "Nom":
                
                demande_nom = input("\nEntrez le nom du pokémon recherché: ")
                res, sa = recherche_nom(demande_nom)
                
                if res == []:
                    print("\nAucun Pokémon trouvé")
        
                elif len(res) == 1: # Si un seul pokémon trouvé
                    affichage_pokemon(sa)
        
                else:
                    print("\nPokémon(s) trouvé(s): " + ', '.join(res))
                
            
            
            elif d_recherche == "Type":
                
                demande_type_1 = input("\nEntrez le 1er type de pokémon recherché: ")
                demande_type_2 = input("Entrez le 2nd type de pokémon recherché (rentrez vide si 1 type): ")
                res = recherche_type(demande_type_1,demande_type_2)
                
                if res == []:
                    print("\nAucun Pokémon trouvé")
        
                else:
                    print("\nPokémon(s) trouvé(s): " + ', '.join(res))
            
            
            
            elif d_recherche == "Talent":
                
                demande_talent_1 = input("\nEntrez le talent 1er des pokémon recherché: ")
                demande_talent_2 = input("Entrez le talent 2nd des pokémon recherché (rentrez vide si 1 talent): ")
                demande_talent_3 = input("Entrez le talent 3ème des pokémon recherché (rentrez vide si 1 ou 2 talents): ")
                res = recherche_talent(demande_talent_1,demande_talent_2,demande_talent_3)
                
                if res == []:
                    print("\nAucun Pokémon trouvé")
        
                else:
                    print("\nPokémon(s) trouvé(s): " + ', '.join(res))
            
            
            else:
                print("\nType recherche invalide.")
                pokedex()
        
        
        elif d_entrer == "Talent":
            
            demande_talent = input("\nEntrez le Talent recherché: ")
            res, sav = definition_talent(demande_talent)
            
            if res == []:
                print("\nAucun Talent trouvé")
    	
            elif len(res) == 1:
                print("\nDéfinition: "+ sav[1])
    	
            else:
                print("Talent(s) trouvé(s): " + ', '.join(res))
        
        
        elif d_entrer == "Quitter":
            
            print("\nAu revoir.")
            
            break
            
        else:
            print("\nEntrée invalide.")
        
    