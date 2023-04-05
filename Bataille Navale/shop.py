from rassemblement import *
from time import sleep

def affichage(tab):
	""" 
	Auteur : Fasquelle
    
	Affichage d'une grille en mode texte 
	
	Parametre grille : (list) grille sous forme de listes
	Valeur renvoyee : (list) affichage d'un tableau
	"""			
	n= len(tab)		
	for i in range(n):	 # 21=4*4+4+1  4*4 '-' pour des cases de longueur 4 et 4+1 '-' pour les colonnes		
		print('-'*(n*4+n+1))
		for j in range(len(tab)):
			print('|{:{width}}'.format(tab[i][j], width=str(4)),end ='')	#utilisation de .format pour des cases de 4 caracteres
		print('|')
	print('-'*(n*4+n+1))

def achat_missile_j1(a1,m1):
    """
    a1 -- entier (argent du joueur 1)
    
    m1 -- booléens (est-ce que le joueur 1 a un missile)
    
    Permet de demander au joueur 1 s'il veut acheter un missile
    (passage de la variable global de False à True)
    
    Léo
    """
    
    if a1 >= 8:
        print(f"JOUEUR 1, vous avez assez d'argent pour acheter un MISSILE ! Voulez-vous en acheter 1 pour 8 pièces ? (vous avez {a1} pièces)")
        demande = input('Oui = "O", Non = "N": ')
        
        if demande == "O":
            m1 = True
            a1 -= 8
        
        elif demande == "N":
            m1 = False
            
        else:
            achat_missile_j1(a1,m1)
    
    return a1, m1
            
def achat_amelioration_j1(a1):
    """
    a1 -- entier (argent du joueur 1)
    
    Permet de demander au joueur 1 s'il veut acheter une amélioration pour l'un de ses bateaux

    Léo
    """
   
    if a1 >= 6:
        print(f"JOUEUR 1, vous avez assez d'argent pour acheter une AMÉLIORATION ! Voulez-vous en acheter 1 pour 6 pièces ? (vous avez {a1} pièces)")
        demande = input('Oui = "O", Non = "N": ')
        
        if demande == "O":
            a1 -= 6
            pose_amelioration_j1(a1)       
            return a1
        
        elif demande == "N":
            return a1
            
        else:
            achat_amelioration_j1(a1)
            
    return a1
            

def achat_missile_j2(a2,m2):
    """
    a2 -- entier (argent du joueur 2)
    
    m2 -- booléens (est-ce que le joueur 2 a un missile)
    
    Permet de demander au joueur 2 s'il veut acheter un missile
    (passage de la variable global de False à True)

    Léo
    """
    
    if a2 >= 8:
        print(f"JOUEUR 2, vous avez assez d'argent pour acheter un MISSILE ! Voulez-vous en acheter 1 pour 8 pièces ? (vous avez {a2} pièces)")
        demande = input('Oui = "O", Non = "N": ')
        
        if demande == "O":
            m2 = True
            a2 -= 8
        
        elif demande == "N":
            m2 = False
            
        else:
            achat_missile_j2(a2,m2)
    
    return a2,m2


def achat_amelioration_j2(a2):
    """
    a2 -- entier (argent du joueur 2)
    
    Permet au joueur 2 d'acheter une amélioration pour l'un de ses bateaux
    
    Léo
    """
    
    if a2 >= 6:
        print(f"JOUEUR 2, vous avez assez d'argent pour acheter une AMÉLIORATION de bateau ! Voulez-vous en acheter 1 pour 12 pièces ? (vous avez {a2} pièces)")
        demande = input('Oui = "O", Non = "N": ')
        
        if demande == "O":
            a2 -= 6
            pose_amelioration_j2(a2) 
            return a2
        
        elif demande == "N":
            return a2
            
        else:
            achat_amelioration_j2(a2)
            
    return a2
            
            
def pose_amelioration_j1(a1):
    """
    a1 -- entier (argent du joueur 1)
    
    Pose l'amélioration du joueur 1 à l'endroit qu'il souhaite 
    (On fait +10 sur la case choisie)
    
    Léo
    """
    
    case_bateau = (2,3,4,5,6,7)
    print('')
    print("Joueur 2, ne regardez pas l'écran")
    sleep(1)
    affichage(plateau_j1)
    sleep(1)
    print('')
    
    lig = input("Choisissez la ligne pour poser l'amélioration de bateau: ")
    col = input("Choisissez la colonne pour poser l'amélioration de bateau: ")
    
    if lig not in ('1','2','3','4','5','6','7','8','9','10') or col not in ('1','2','3','4','5','6','7','8','9','10'):
        print("")
        print("Veuillez entrer un nombre valide")
        pose_amelioration_j1(a1)
        
    if int(lig) == 0 or int(col) == 0 or int(lig) > 10 or int(col) > 10:
        print("Veuillez rentrer un nombre valide")
        pose_amelioration_j1(a1)
    
    # Si la case choisie n'est pas un bateau  
    else:
        col = int(col) - 1
        lig = int(lig) - 1
    
        if plateau_j1[lig][col] in case_bateau:
            plateau_j1[lig][col] += 10
                
            affichage(plateau_j1)
            print("")
            print("-- Case améliorée avec succès ! --")
            print("-- Argent: " + str(a1) + " --")
            
        else:
            print("Emplacement invalide")
            pose_amelioration_j1(a1)
            

def pose_amelioration_j2(a2):
    """
    a2 -- entier (argent du joueur 2)
    
    Pose l'amélioration du joueur 1 à l'endroit qu'il souhaite 
    (On fait +10 sur la case choisie)
    
    Léo
    """

    case_bateau = (2,3,4,5,6,7)
    
    print('')
    print("Joueur 1, ne regardez pas l'écran")
    sleep(1)
    affichage(plateau_j2)
    sleep(1)
    print('')
    
    lig = input("Choisissez la ligne pour poser l'amélioration de bateau: ")
    col = input("Choisissez la colonne pour poser l'amélioration de bateau: ")
    
    if lig not in ('1','2','3','4','5','6','7','8','9','10') or col not in ('1','2','3','4','5','6','7','8','9','10'):
        print("")
        print("Veuillez entrer un nombre")
        pose_amelioration_j2(a2)
        
    if int(lig) == 0 or int(col) == 0 or int(lig) > 10 or int(col) > 10:
        print("Veuillez rentrer un nombre valide")
        pose_amelioration_j2(a2) 
        
    else:
        col = int(col) - 1
        lig = int(lig) - 1
    
        if plateau_j2[lig][col] in case_bateau:
            plateau_j2[lig][col] += 10
                
            affichage(plateau_j2)
            print("")
            print("-- Case améliorée avec succès ! --")
            print("-- Argent: " + str(a2) + " --")

        # Si la case choisie n'est pas un bateau  
        else:
            print("Emplacement invalide")
            pose_amelioration_j2(a2)
            
            
def achat_j1(a1,m1):
    """
    a1 -- entier (argent du joueur 1)
    
    m1 -- booléens (est-ce que le joueur 1 a un missile)
    
    centralise les demandes au joueur 1 pour acheter soit un missile soit une amélioration
    
    Léo 
    """
    a1 = achat_amelioration_j1(a1)
    a1,m1 = achat_missile_j1(a1,m1)
    return a1,m1
    
def achat_j2(a2,m2):
    """
    a2 -- entier (argent du joueur 2)
    
    m2 -- booléens (est-ce que le joueur 2 a un missile)
    
    centralise les demandes au joueur 2 pour acheter soit un missile soit une amélioration
    
    Léo 
    """
    a2 = achat_amelioration_j2(a2)
    a2,m2 = achat_missile_j2(a2,m2)
    return a2,m2
            

    
    