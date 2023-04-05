from rassemblement import *
from shop import *


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
    
    
def tir_normal(plateau, pov):
    """
    plateau -- liste de listes (plateau du joueur adverse)
    
    pov -- liste de listes (plateau du visuel du tireur)
    
    Permet de tirer sur un plateau défini (ici, le plateau adverse), qui modifie la valeur(int) de 
    l'endroit touché par une autre valeur(int) sur les deux plateaux en paramètre.
    
    Léo
    """
    case_tir = (0,2,3,4,5,6,7,12,13,14,15,16,17)     # cases sur lesquels la fonction peut tirer
    case_bateau = (2,3,4,5,6,7)     # cases sur lesquels se trouve un bateau
    case_ameliorer = (12,13,14,15,16,17)    # cases sur lesquels se trouve un bateau amélioré
    case_invalide = (1,8,9)     # cases sur lesquels la fonction ne peut pas tirer
    
    # Demande de l'endroit où tirer
    lig = input("Définissez la ligne de tir : ")
    col = input("Définissez la colonne de tir : ")
    
    # Test si les coordonnées entrées sont valides
    if lig not in ('1','2','3','4','5','6','7','8','9','10') or col not in ('1','2','3','4','5','6','7','8','9','10'):
        print('')
        print('Veuillez rentrer un nombre valide')
        tir_normal(plateau, pov)
        return None
    
    if int(lig) == 0 or int(col) == 0 or int(lig) > 10 or int(col) > 10:
        print("Veuillez rentrer un nombre valide")
        tir_normal(plateau, pov)
        return None
        
    else:
        col = int(col) - 1
        lig = int(lig) - 1
        
        if plateau[lig][col] in case_tir:
            
            # Touché
            if plateau[lig][col] in case_bateau:
                plateau[lig][col] = 1
                pov[lig][col] = 1
                
                affichage(pov)
                print("")
                print("-- TOUCHÉ ! --")
                return True
            
            # Endommagé
            elif plateau[lig][col] in case_ameliorer:
                plateau[lig][col] -= 10
                pov[lig][col] = 11
                
                affichage(pov)
                print("")
                print("-- ENDOMMAGÉ ! --")
            
            # Raté
            else:
                plateau[lig][col] = 9
                pov[lig][col] = 9
                
                affichage(pov)
                print("")
                print("-- RATÉ ! --")
        
        # Si endroit tiré invalide
        elif plateau[lig][col] in case_invalide:
            print("")
            print("-- Tire non validé, réessayez chef ! --")
            tir_normal(plateau, pov)


def tir_missile(plateau, pov):
    """
    plateau -- liste de listes (plateau du joueur adverse)
    
    pov -- liste de listes (plateau du visuel du tireur)
    
    Permet de tirer un missile d'un rayon 3x3 sur un plateau défini (ici, le plateau adverse), qui modifie 
    la valeur(int) de les endroits touchés par d'autres valeurs(int) sur les deux plateaux en 
    paramètre en fonction de ce qui ce trouve à cette case. 
    
    Léo
    """
    global toucher
    toucher = 0 # Nombre de cases bateaux touchées
    
    case_invalide = (1,8,9) # cases sur lesquels la fonction ne peut pas tirer
    
    # Demande de l'endroit où tirer
    lig = input("Définissez la ligne de tir : ")
    col = input("Définissez la colonne de tir : ")
    
    # Test si les coordonnées entrées sont valides
    if lig not in ('1','2','3','4','5','6','7','8','9','10') or col not in ('1','2','3','4','5','6','7','8','9','10'):
        print('')
        print('Veuillez rentrer un nombre valide')
        tir_missile(plateau, pov)
        return None
    
    if int(lig) < 2 or int(col) < 2 or int(lig) > 9 or int(col) > 9:
        print("Emplacement invalide")
        tir_missile(plateau, pov)
        return None
        
    else:
        col = int(col) - 1
        lig = int(lig) - 1
        
        # Si endroit tiré invalide
        if plateau[lig][col] in case_invalide:
            print("")
            print("-- Tire non validé, réessayez chef ! --")
            tir_missile(plateau, pov)
            return None
        
        # Explosion du missile de rayon 3x3
        impact(plateau, pov, lig, col)
        impact(plateau, pov, lig-1, col)
        impact(plateau, pov, lig+1, col)
        impact(plateau, pov, lig, col-1)
        impact(plateau, pov, lig, col+1)
        impact(plateau, pov, lig+1, col+1)
        impact(plateau, pov, lig-1, col-1)
        impact(plateau, pov, lig+1, col-1)
        impact(plateau, pov, lig-1, col+1)
        
        affichage(pov)
        if toucher == 0:
            print("-- RATÉ ! --")
            return toucher
        
        else:
            print(f"-- TOUCHÉ {toucher} fois ! --")
            return toucher
        


def impact(tableau, tab_pov, ligne, colonne):
    """
    tableau --  liste de listes (plateau du joueur adverse)
    
    tab_pov -- liste de listes (plateau du visuel du tireur)
    
    ligne -- int
    
    colonne -- int
    
    Modifie la valeur(int) de case entré par les coordonnées ligne, colonne, par une autre
    valeur(int) en fonction de ce qui ce trouve à cette case. 
    
    Est utilisé pour créer le rayon d'impact du missile.
    
    Léo
    """
    
    
    global toucher
    
    case_tir = (0,2,3,4,5,6,7,10,12,13,14,15,16,17)     # cases sur lesquels la fonction peut tirer
    case_bateau = (2,3,4,5,6,7)     # cases sur lesquels se trouve un bateau
    case_ameliorer = (12,13,14,15,16,17)    # cases sur lesquels se trouve un bateau amélioré
    
    if tableau[ligne][colonne] in case_tir:
            # Touché
            if tableau[ligne][colonne] in case_bateau:
                tableau[ligne][colonne] = 1
                tab_pov[ligne][colonne] = 1
            
                toucher += 1
            
            # Endommagé
            elif tableau[ligne][colonne] in case_ameliorer:
                tableau[ligne][colonne] -= 10
                tab_pov[ligne][colonne] = 11
            
            # Raté
            else:
                tableau[ligne][colonne] = 9
                tab_pov[ligne][colonne] = 9


def tir_j1(a1,m1,pov1):
     """
     a1 -- entier (argent du joueur 1)
     
     m1 -- booléens (est-ce que le joueur 1 a un missile)
     
     pov1 -- liste de listes (plateau que vois le joueur 1 quand il tire)
     
     Fonction rassemblant tir_normal et tir_missile pour permettre au joueur 1 de tirer
     soit un coup normal, soit un missile si il en possède un.
     
     Léo
     """
     
     # Possède un missile
     if m1 == True:
         touch = tir_missile(plateau_j2, pov1)
         if touch == 0 :
             a1 = a1
             print('')
             print(f'Argent joueur 1 : {a1}')
             m1 = False
             return a1
         else :
             a1 = a1 + 2*touch
         
             print('')
             print(f'Argent joueur 1 : {a1}')
             m1 = False
             return a1,m1
    
    # Tir normal
     elif tir_normal(plateau_j2, pov1) == True:
         a1 += 2
         
         print('')
         print(f'Argent joueur 1 : {a1}')
         return a1,m1
     
     else:
         return a1,m1
     
         
def tir_j2(a2,m2,pov2):
     """
     a2 -- entier (argent du joueur 2)
     
     m2 -- booléens (est-ce que le joueur 2 a un missile)
     
     pov2 -- liste de listes (plateau que vois le joueur 2 quand il tire)
     
     Fonction rassemblant tir_normal et tir_missile pour permettre au joueur 2 de tirer
     soit un coup normal, soit un missile si il en possède un.
     
     Léo
     """
     
     # Possède un missile
     if m2 == True:
         a2 = a2 + 2*tir_missile(plateau_j1, pov2)
         
         print('')
         print(f'Argent joueur 2 : {a2}')
         m2 = False
         return a2,m2
         
    # Tir normal
     elif tir_normal(plateau_j1, pov2) == True:
         a2 += 2
         
         print('')
         print(f'Argent joueur 2 : {a2}')
         return a2,m2
     
     else:
         return a2,m2
        