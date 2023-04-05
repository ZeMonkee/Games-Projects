import csv

def parcours_attaques():
    """
    Retourne la commande pour ouvrir et lire le fichier "Stats_pokemons_5g.csv".

    """
    return csv.reader(open("Attaques_pokemons_5g.csv", "r", encoding='utf-8'), delimiter=",")


def affichage_attaques(liste):
    """
    liste -- liste contenant toute les stats d'un attaque'
    
    Permet d'afficher proprement les stats d'un attaque.

    """
    print("\nID: "+ liste[0])
    print("Nom: "+ liste[1])
    print("Type: "+ liste[2])
    print("Catégorie: "+ liste[3])
    print("Dégâts: "+ liste[4])
    print("Précision: "+ liste[5])
    print("PP: "+ liste[6])
    

def recherche_id(id_att):
    """
    Fonction qui permet de rechercher un attaque par son ID du Pokédex.
    
    Renvoie les stats du attaque seulement si trouvé dans "Stats_attaques_5g.csv".
    -- ou --
    Renvoie les noms des attaques si plusieurs ID associé à la demandes de l'utilisateur.

    """
    stats_attaques = parcours_attaques() # Ouverture du fichier des stats
    resultat = [] # Liste contenant tout les noms des attaques trouvés
    save = [] # Liste contenant toute les stats du dernier attaque trouvé
    
    for ligne in stats_attaques: # Parcours du fichier des stats

        if id_att == ligne[0]:
            resultat.append(ligne[1])
            save = ligne
    
    return resultat, save
            

def recherche_nom(nom_att):
    """
    Fonction qui permet de rechercher un attaque par son nom dans le Pokédex.
    
    Renvoie les stats du attaque seulement si trouvé dans "Stats_attaques_5g.csv".
    -- ou --
    Renvoie les noms des attaques similaires à la demandes de l'utilisateur.

    """
    stats_attaques = parcours_attaques() # Ouverture du fichier des stats
    resultat = [] # Liste contenant tout les noms des attaques trouvés
    save = [] # Liste contenant toute les stats du dernier attaque trouvé
    
    for ligne in stats_attaques: # Parcours du fichier des stats

        if nom_att in ligne[1]:
            resultat.append(ligne[1])
            save = ligne
    
    return resultat, save
            

def recherche_type(type_att):
    """
    Fonction qui permet de rechercher des attaques par leur(s) type(s).
    
    Renvoie le nom des attaque possedant ce(s) type(s) dans "Stats_attaques_5g.csv".

    """
    stats_attaques = parcours_attaques() # Ouverture du fichier des stats
    resultat = [] # Liste contenant tout les noms des attaques trouvés

    for ligne in stats_attaques: # Parcours du fichier des stats
    
        if type_att in ligne[2]:
            resultat.append(ligne[1])
    
    return resultat


def recherche_categorie(cat_att):
    """
    Fonction qui permet de rechercher des attaques par leur(s) type(s).
    
    Renvoie le nom des attaque possedant ce(s) type(s) dans "Stats_attaques_5g.csv".

    """
    stats_attaques = parcours_attaques() # Ouverture du fichier des stats
    resultat = [] # Liste contenant tout les noms des attaques trouvés

    for ligne in stats_attaques: # Parcours du fichier des stats
    
        if cat_att in ligne[3]:
            resultat.append(ligne[1])
    
    return resultat



def pokedex_attaque():
    
    print("\nBienvenue dans le pokédex des attaques !")
    
    while True:
            
        d_recherche = input("\nQuel type de recherche voulez-vous effectuer ?\n- ID -\n- Nom -\n- Type -\n- Catégorie -\n- Quitter -\n\n=> ")
            
            
        if d_recherche == "ID":
                
            demande_id = input("\nEntrez l'ID du attaque recherché: ")
            res, sa = recherche_id(demande_id)
                
            if res == []:
                print("\nAucun Attaque trouvé")
        
            elif len(res) == 1: # Si un seul attaque trouvé
                affichage_attaques(sa)
        
            else:
                print("\nAttaque(s) trouvé(s): " + ', '.join(res))
            
            
            
        elif d_recherche == "Nom":
                
            demande_nom = input("\nEntrez le nom du attaque recherché: ")
            res, sa = recherche_nom(demande_nom)
                
            if res == []:
                print("\nAucun Attaque trouvé")
        
            elif len(res) == 1: # Si un seul attaque trouvé
                affichage_attaques(sa)
        
            else:
                print("\nAttaque(s) trouvé(s): " + ', '.join(res))
                
            
            
        elif d_recherche == "Type":
                
            demande_type = input("\nEntrez le type de l'attaque recherché: ")
            res = recherche_type(demande_type)
                
            if res == []:
                print("\nAucun Attaque trouvé")
        
            else:
                print("\nAttaque(s) trouvé(s): " + ', '.join(res))
            
            
            
        elif d_recherche == "Catégorie":
                
            demande_categorie = input("\nEntrez la catégorie des attaque recherché: ")
            res = recherche_categorie(demande_categorie)
                
            if res == []:
                print("\nAucun Attaque trouvé")
        
            else:
                print("\nAttaque(s) trouvé(s): " + ', '.join(res))
        
        
        elif d_recherche == "Quitter":
            print("\nAu revoir.")
            break
            
        else:
            print("\nEntrée invalide.")
    