#Plateau des joueurs
plateau_j1 = [[0 for col in range(10)] for lig in range(10)]
plateau_j2 = [[0 for col in range(10)] for lig in range(10)]

#Plateau de tir
plateau_pov1 = [[0 for col in range(10)] for lig in range(10)]
plateau_pov2 = [[0 for col in range(10)] for lig in range(10)]

#Définition des variables permettant de conserver l'argent
argent_j1 = 0
argent_j2 = 0

#Définition des variables permettant de savoir si un joueur a un missile
missile_j1 = False
missile_j2 = False


import os
from IPython import get_ipython
from time import sleep

from bateaux import *
from tir import *
from shop import *


def effacer():
    """
    Efface la console afin d'éviter la triche
    
    Titouan
    """
    if os.name == 'nt': 
        get_ipython().magic('cls')
    else:
        get_ipython().magic('clear')

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
  
def demande_j1(bateau):
    """
    bateau -- chaine de caractères et nom d'un bateau défini
    
    Permet de placer un bateau défini sur le plateau_j1 (plateau du joueur 1)
    
    Titouan
    """      
    L = input(f"Joueur 1, en quelle ligne voulez vous placez votre {bateau} ? : ")
    C = input("En quelle colonne ? : ")
    A = input("Vertical (V) ou Horizontal (H) : ")
    
    if L not in ('1','2','3','4','5','6','7','8','9','10') or C not in ('1','2','3','4','5','6','7','8','9','10'):
        print('')
        print('Veuillez rentrer un nombre valide')
        demande_j1(bateau)
        return None
        
    if A not in ('H','V'):
        print('')
        print("Choix de l'inclinaison invalide, veuillez réessayer")
        demande_j1(bateau)
        return None
        
    if poseBateaux(plateau_j1, int(L), int(C), A, bateau) == "Case Invalide":
        print('')
        print("Case Invalide, veuillez réessayer")
        demande_j1(bateau)
        return None
        
    poseBateaux(plateau_j1, int(L), int(C), A, bateau)
    affichage(plateau_j1)
    
def demande_j2(bateau):
    """
    bateau -- chaine de caractères et nom d'un bateau défini
    
    Permet de placer un bateau défini sur le plateau_j2 (plateau du joueur 2)
    
    Titouan
    """        
    L = input(f"Joueur 2, en quelle ligne voulez vous placez votre {bateau} ? : ")
    C = input("En quelle colonne ? : ")
    A = input("Vertical (V) ou Horizontal (H) : ")
    
    if L not in ('1','2','3','4','5','6','7','8','9','10') or C not in ('1','2','3','4','5','6','7','8','9','10'):
        print('')
        print('Veuillez rentrer un nombre valide')
        demande_j2(bateau)
        return None
        
    if A not in ('H','V'):
        print('')
        print("Choix de l'inclinaison invalide, veuillez réessayer")
        demande_j2(bateau)
        return None
    
    if poseBateaux(plateau_j2, int(L), int(C), A, bateau) == "Case Invalide":
        print('')
        print("Case Invalide, veuillez réessayer")
        demande_j2(bateau)
        return None
        
    poseBateaux(plateau_j2, int(L), int(C), A, bateau)
    affichage(plateau_j2)
   
def menu():
    """
    Interface permettant au joueur de choisir entre lancer une partie ou sortir du jeu 
    (nous permettra de rejouer après la fin d'une première partie)
    
    Alessandro 
    """
    
    effacer()
    
    #Plateau des joueurs
    plateau_j1 = [[0 for col in range(10)] for lig in range(10)]
    plateau_j2 = [[0 for col in range(10)] for lig in range(10)]

    #Plateau de tir
    plateau_pov1 = [[0 for col in range(10)] for lig in range(10)]
    plateau_pov2 = [[0 for col in range(10)] for lig in range(10)]
    
    #Argents
    argent_j1 = 0
    argent_j2 = 0
    
    #Missiles
    missile_j1 = False
    missile_j2 = False
    
    def demande():
        
        demande_jouer = input('Entrez "J" pour JOUER ou "Q" pour QUITTER: ')
    
        if demande_jouer == "J":
            jeu(plateau_j1, plateau_j2, argent_j1, argent_j2, missile_j1, missile_j2, plateau_pov1, plateau_pov2)
        
        elif demande_jouer == "Q":
            return True
        
        elif demande_jouer not in ('J','Q'):
            print("Invalide, entrez la lettre correspondante !")
            sleep(1)
            print("")
            demande()
    
    print("Bienvenue dans la bataille navale + mieux que les autres !")
    sleep(1)
    print("")
    print("Que voulez vous faire ?")
    sleep(1)         
    if demande() == True: 
        print('')
        print('Au revoir !')
        return None


def v1():
    """
    Vérifie si le joueur 2 a gagné, soit si il n'y a plus aucun bateaux sur le plateau du joueur 1
    
    Alessandro
    """
    case_bateaux = (2,3,4,5,6,7,12,13,14,15,16,17)
    Win = True
        
    for ligne in plateau_j1:
        for element in ligne:
            if element in case_bateaux:
                Win = False
    return Win
                   
def v2():
    """
    Vérifie si le joueur 1 a gagné, soit si il n'y a plus aucun bateaux sur le plateau du joueur 2
    
    Alessandro
    """
    case_bateaux = (2,3,4,5,6,7,12,13,14,15,16,17)
    Win = True
        
    for ligne in plateau_j2:
        for element in ligne:
            if element in case_bateaux:
                Win = False
    return Win
    


def jeu(p1,p2,arg_j1,arg_j2,miss_j1,miss_j2,pov1,pov2):
    """
    p1 -- liste de listes (plateau du joueur 1)
    
    p2 -- liste de listes (plateau du joueur 2)
    
    arg_j1 -- entier (argent du joueur 1)
    
    arg_j2 -- entier (argent du joueur 2)
    
    miss_j1 -- booléens (permet de savoir si le joueur 1 à un missile)
    
    miss_j2 -- booléens (permet de savoir si le joueur 2 à un missile)
    
    pov1 -- liste de listes (plateau que vois le joueur 1 quand il tire)
    
    pov1 -- liste de listes (plateau que vois le joueur 1 quand il tire)
    
    Permet de lancer le jeu, d'abord en demandant aux joueurs où placer leurs bateaux, puis
    en les faisant tirer chacun leur tour.
    
    Si l'un des deux joueurs gagne, on relance la fonction menu et donc la partie
    
    Titouan
    """
    
    effacer()
    
    demande_j1("Titanic")
    demande_j1("PorteAvion")
    demande_j1("Torpilleur")
    demande_j1("Croiseur")
    demande_j1("SousMarin")
    demande_j1("Yacht")
    
    print("Laissez la place au joueur 2")
    sleep(3)
    effacer()
    
    demande_j2("Titanic")
    demande_j2("PorteAvion")
    demande_j2("Torpilleur")
    demande_j2("Croiseur")
    demande_j2("SousMarin")
    demande_j2("Yacht")
    
  
    sleep(3)
    effacer()
    sleep(1)
    
    while True:
        
        print("C'est au tour du joueur 1")
        sleep(1)
        affichage(pov1)
        arg_j1, miss_j1 = tir_j1(arg_j1,miss_j1,pov1)
        if v2() == True:
            print('')
            print('Victoire du joueur 1 !')
            sleep(4)
            menu()
            return None
        
        sleep(5)
        arg_j1,miss_j1 = achat_j1(arg_j1,miss_j1)
        sleep(1)
        
        effacer()
        
        print("C'est au tour du joueur 2")
        sleep(1)
        affichage(pov2)
        arg_j2, miss_j2 = tir_j2(arg_j2,miss_j2,pov2)
        if v1() == True:
            print('')
            print('Victoire du joueur 2 !')
            sleep(4)
            menu()
            return None
        
        sleep(5)
        arg_j2,miss_j2 = achat_j2(arg_j2, miss_j2)
        sleep(1)
    
        effacer()




