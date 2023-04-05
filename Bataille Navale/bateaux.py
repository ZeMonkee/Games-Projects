def testCaseLibre(plateau,lig,col):
    """
    Permet de tester si une case est libre avant d'y poser un bateau
    
    Titouan
    """
    case_invalide = (2,3,4,5,6,7,12,13,14,15,16,17)
    
    if plateau[lig][col] in case_invalide:
        return False


def poseYacht(plateau, ligne, colonne, angle):
    """
    plateau -- liste de listes
    
    ligne -- entier
    
    colonne -- entier
    
    angle -- chaine de caracteres (soit H soit V)
    
    Pose un Yacht (2 cases) à l'endroit choisi
    
    Titouan
    """
    
    if angle == "H":
        
        #Test des cases
        if colonne >= len(plateau[0]) : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne-1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne) == False : return 'Case Invalide'
        
        plateau[ligne-1][colonne] = 2
        plateau[ligne-1][colonne-1] = 2 # Case que le joueur choisit
    
    
    if angle == 'V':
        
        #Test des cases
        if ligne-1 < 1 : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-2, colonne-1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne-1) == False : return 'Case Invalide'
        
        plateau[ligne-2][colonne-1] = 2
        plateau[ligne-1][colonne-1] = 2 # Case que le joueur choisit
        
    
    return plateau


def poseSousMarin(plateau, ligne, colonne, angle):
    """
    plateau -- liste de listes
    
    ligne -- entier
    
    colonne -- entier
    
    angle -- chaine de caracteres (soit H soit V)
    
    Pose un Sous-Marin (3 cases) à l'endroit choisi
    
    Titouan
    """
    
    
    if angle == "H":
        
        #Test des cases
        if colonne >= len(plateau[0]) : return 'Case Invalide'
        if colonne-2 < 0 : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne-1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne-2) == False : return 'Case Invalide'
            
        plateau[ligne-1][colonne] = 3
        plateau[ligne-1][colonne-1] = 3 # Case que le joueur choisit
        plateau[ligne-1][colonne-2] = 3
    
    
    if angle == 'V':
        
        #Test des cases
        if ligne-1 < 1 : return 'Case Invalide'
        if ligne > len(plateau) : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-2, colonne-1) == False: return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne-1) == False: return 'Case Invalide'
        if testCaseLibre(plateau, ligne, colonne-1) == False : return 'Case Invalide'
        
        plateau[ligne-2][colonne-1] = 3
        plateau[ligne-1][colonne-1] = 3 # Case que le joueur choisit
        plateau[ligne][colonne-1] = 3

    return plateau


def poseCroiseur(plateau, ligne, colonne, angle):
    """
    plateau -- liste de listes
    
    ligne -- entier
    
    colonne -- entier
    
    angle -- chaine de caracteres (soit H soit V)
    
    Pose un Croiseur (4 cases) à l'endroit choisi
    
    Titouan
    """
    
    if angle == "H":
        
        #Test des cases
        if colonne+1 >= len(plateau[0]) : return 'Case Invalide'
        if colonne-2 < 0 : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne+1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne-1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne-2) == False : return 'Case Invalide'
        
        plateau[ligne-1][colonne+1] = 4
        plateau[ligne-1][colonne] = 4
        plateau[ligne-1][colonne-1] = 4 # Case que le joueur choisit
        plateau[ligne-1][colonne-2] = 4


    if angle == 'V':
        
        #Test des cases
        if ligne-2 < 1 : return 'Case Invalide'
        if ligne > len(plateau) : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-3, colonne-1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-2, colonne-1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne-1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne, colonne-1) == False : return 'Case Invalide'
            
        plateau[ligne-3][colonne-1] = 4
        plateau[ligne-2][colonne-1] = 4
        plateau[ligne-1][colonne-1] = 4 # Case que le joueur choisit
        plateau[ligne][colonne-1] = 4
        
    return plateau


def posePorteAvion(plateau, ligne, colonne, angle):
    """
    plateau -- liste de listes
    
    ligne -- entier
    
    colonne -- entier
    
    poser un porte-avion (6 cases) à l'endroit choisi
    
    Alessandro
    """
    if angle == 'V':
        
        #Test des cases
        if ligne-2 < 1 : return 'Case Invalide'
        if ligne > len(plateau) : return 'Case Invalide'
        if colonne >= len(plateau[0]) : return 'Case Invalide'
        if testCaseLibre(plateau, ligne, colonne) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-3, colonne-1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-2, colonne-1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne-1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-2, colonne) == False : return 'Case Invalide'
        
        plateau[ligne][colonne] = 6
        plateau[ligne-3][colonne-1] = 6
        plateau[ligne-2][colonne-1] = 6
        plateau[ligne-1][colonne] = 6
        plateau[ligne-1][colonne-1] = 6 # Case que le joueur choisit
        plateau[ligne-2][colonne] = 6
        
    elif angle == 'H':
        
        #Test des cases
        if colonne+1 >= len(plateau[0]) : return 'Case Invalide'
        if colonne-2 < 0 : return 'Case Invalide'
        if ligne-1 >= len(plateau) : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne-1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne+1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne, colonne) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne, colonne-1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne, colonne-2) == False : return 'Case Invalide'
        
        plateau[ligne-1][colonne-1] = 6 # Case que le joueur choisit
        plateau[ligne-1][colonne] = 6
        plateau[ligne-1][colonne+1] = 6
        plateau[ligne][colonne] = 6
        plateau[ligne][colonne-1] = 6
        plateau[ligne][colonne-2] = 6
        
        
        
def poseTorpilleur(plateau, ligne, colonne, angle):
    """
    plateau -- liste de liste
    
    ligne -- entier
    
    colonne -- entier
    
    poser un torpilleur (4 cases) à l'endroit choisi
    
    Alessandro
    """
    if angle == 'V':
        
        #Test des cases
        if ligne-1 < 1 : return 'Case Invalide'
        if ligne > len(plateau) : return 'Case Invalide'
        if colonne >= len(plateau[0]) : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-2, colonne-1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne-1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne, colonne-1) == False : return 'Case Invalide'
        
        plateau[ligne-1][colonne] = 5
        plateau[ligne-2][colonne-1] = 5
        plateau[ligne-1][colonne-1] = 5 # Case que le joueur choisit
        plateau[ligne][colonne-1] = 5
        
    
    elif angle == 'H':
        
        #Test des cases
        if colonne >= len(plateau[0]) : return 'Case Invalide'
        if colonne-2 < 0 : return 'Case Invalide'
        if ligne-1 >= len(plateau) : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne-2) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne-1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne, colonne-1) == False : return 'Case Invalide'
        
        plateau[ligne-1][colonne-2] = 5
        plateau[ligne-1][colonne] = 5
        plateau[ligne-1][colonne-1] = 5 # Case que le joueur choisit
        plateau[ligne][colonne-1] = 5
        
        
        
def poseTitanic(plateau, ligne, colonne, angle):
    """
    plateau -- liste de listes
    
    ligne -- entier 
    
    colonne -- entier
    
    poser le titanic (5 cases) à l'endroit choisi
    
    Alessandro
    """
    if angle == 'V':
        
        #Test des cases
        if ligne-2 < 1 : return 'Case Invalide'
        if ligne+1 > len(plateau) : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-3, colonne-1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-2, colonne-1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne-1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne, colonne-1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne+1, colonne-1) == False : return 'Case Invalide'
        
        plateau[ligne-3][colonne-1] = 7
        plateau[ligne-2][colonne-1] = 7
        plateau[ligne-1][colonne-1] = 7 # Case que le joueur choisit
        plateau[ligne][colonne-1] = 7
        plateau[ligne+1][colonne-1] = 7
        
    elif angle == 'H':
        
        #Test des cases
        if colonne+1 >= len(plateau[0]) : return 'Case Invalide'
        if colonne-3 < 0 : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne-3) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne-2) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne-1) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne) == False : return 'Case Invalide'
        if testCaseLibre(plateau, ligne-1, colonne+1) == False : return 'Case Invalide'
        
        plateau[ligne-1][colonne-3] = 7
        plateau[ligne-1][colonne-2] = 7
        plateau[ligne-1][colonne-1] = 7 # Case que le joueur choisit
        plateau[ligne-1][colonne] = 7
        plateau[ligne-1][colonne+1] = 7

    
    
def poseBateaux(plateau, ligne, colonne, angle, bateau):
    """
    plateau -- liste de listes
    
    ligne -- entier
    
    colonne -- entier
    
    angle -- chaine de caracteres (soit H soit V)
    
    bateau -- choix du bateau à poser
    
    Cette fonction permet de centraliser la pose des bateaux pour faciliter le programme
    
    Titouan
    """
    
    if 1 > colonne or colonne > len(plateau[0]) : return 'Case Invalide'
    if 1 > ligne or ligne > len(plateau): return 'Case Invalide'
    
    if bateau == "Yacht":
        return poseYacht(plateau, ligne, colonne, angle)
        
    elif bateau == "SousMarin":
        return poseSousMarin(plateau, ligne, colonne, angle)
        
    elif bateau == "Croiseur":
        return poseCroiseur(plateau, ligne, colonne, angle)
        
    elif bateau == "Torpilleur":
        return poseTorpilleur(plateau, ligne, colonne, angle)
        
    elif bateau == "PorteAvion":
        return posePorteAvion(plateau, ligne, colonne, angle)
        
    elif bateau == "Titanic":
        return poseTitanic(plateau, ligne, colonne, angle)
    
    else :
        return False


    
    
    
    
    
    