def affinite_type(type_attaque,type_defenseur):
    """
    type_attaque -- Chaine de caractere contenant le type de l'attaque du Pokemon attaquant.
    type_defenseur -- Chaine de caractere contenant le type du pokemon defenseur.
    
    Renvoie un nombre en fonction de l'efficacitee de l'attaque:
        0 = Aucun effet
        0,5 = Inefficace
        1 = Normal
        2 = Très efficace

    """
    res = []
    
    
    type_pokemon = ("Acier","Combat","Dragon","Eau","Électrik","Fee","Feu","Glace","Insecte","Normal","Plante","Poison","Psy","Roche","Sol","Spectre","Ténèbres","Vol")
    
    assert type_attaque in type_pokemon, "Type de l'attaque non valide."
    assert type_defenseur in type_pokemon, "Type du pokemon non valide."
    
    if type_attaque == "Normal":
        
        if type_defenseur in ("Acier","Roche"):
            res.append(0.5)
        
        elif type_defenseur == "Spectre":
            res.append(0)
        
        else:
            res.append(1)
        
    if type_attaque == "Feu":
        
        if type_defenseur in ("Feu","Eau","Roche","Dragon"):
            res.append(0.5)
        
        elif type_defenseur in ("Acier","Plante","Glace","Insecte"):
            res.append(2)
        
        else:
            res.append(1)
        
    if type_attaque == "Eau":
        
        if type_defenseur in ("Eau","Plante","Dragon"):
            res.append(0.5)
        
        elif type_defenseur in ("Feu","Sol","Roche"):
            res.append(2)
        
        else:
            res.append(1)
    
    if type_attaque == "Électrik":
        
        if type_defenseur in ("Électrik","Plante","Dragon"):
            res.append(0.5)
        
        elif type_defenseur == "Sol":
            res.append(0)
        
        elif type_defenseur in ("Eau","Vol"):
            res.append(2)
        
        else:
            res.append(1)
    
    if type_attaque == "Plante":
        
        if type_defenseur in ("Acier","Feu","Plante","Poison","Vol","Insecte","Dragon"):
            res.append(0.5)
        
        elif type_defenseur in ("Eau","Roche","Sol"):
            res.append(2)
        
        else:
            res.append(1)
    
    if type_attaque == "Glace":
        
        if type_defenseur in ("Acier","Eau","Feu","Glace"):
            res.append(0.5)
        
        elif type_defenseur in ("Dragon","Plante","Sol","Vol"):
            res.append(2)
        
        else:
            res.append(1)
    
    if type_attaque == "Combat":
        
        if type_defenseur in ("Fee","Insecte","Poison","Psy","Vol"):
            res.append(0.5)
        
        elif type_defenseur == "Spectre":
            res.append(0)
        
        elif type_defenseur in ("Acier","Glace","Normal","Roche","Ténèbres"):
            res.append(2)
        
        else:
            res.append(1)
    
    if type_attaque == "Poison":
        
        if type_defenseur in ("Poison","Roche","Sol","Spectre"):
            res.append(0.5)
        
        elif type_defenseur == "Acier":
            res.append(0)
        
        elif type_defenseur in ("Fee","Plante"):
            res.append(2)
        
        else:
            res.append(1)
    
    if type_attaque == "Sol":
        
        if type_defenseur in ("Insecte","Plante"):
            res.append(0.5)
        
        elif type_defenseur == "Vol":
            res.append(0)
        
        elif type_defenseur in ("Acier","Électrik","Feu","Poison","Roche"):
            res.append(2)
        
        else:
            res.append(1)
    
    if type_attaque == "Vol":
        
        if type_defenseur in ("Acier","Électrik","Roche"):
            res.append(0.5)
        
        elif type_defenseur in ("Combat","Insecte","Plante"):
            res.append(2)
        
        else:
            res.append(1)
    
    if type_attaque == "Fee":
        
        if type_defenseur in ("Acier","Feu","Poison"):
            res.append(0.5)
        
        elif type_defenseur in ("Combat","Dragon","Ténèbres"):
            res.append(2)
        
        else:
            res.append(1)
        
    if type_attaque == "Insecte":
        
        if type_defenseur in ("Acier","Combat","Fee","Feu","Poison","Spectre","Vol"):
            res.append(0.5)
        
        elif type_defenseur in ("Plante","Psy","Ténèbres"):
            res.append(2)
        
        else:
            res.append(1)
        
    if type_attaque == "Roche":
        
        if type_defenseur in ("Acier","Combat","Sol"):
            res.append(0.5)
        
        elif type_defenseur in ("Feu","Glace","Insecte","Vol"):
            res.append(2)
        
        else:
            res.append(1)
        
    if type_attaque == "Spectre":
        
        if type_defenseur in ("Ténèbres"):
            res.append(0.5)
        
        elif type_defenseur == "Normal":
            res.append(0)
        
        elif type_defenseur in ("Psy","Spectre"):
            res.append(2)
        
        else:
            res.append(1)
        
    if type_attaque == "Dragon":
        
        if type_defenseur == "Acier":
            res.append(0.5)
        
        elif type_defenseur == "Fee":
            res.append(0)
        
        elif type_defenseur == "Dragon":
            res.append(2)
        
        else:
            res.append(1)
        
    if type_attaque == "Acier":
        
        if type_defenseur in ("Acier","Eau","Électrik","Feu"):
            res.append(0.5)
        
        elif type_defenseur in ("Fee","Glace","Roche"):
            res.append(2)
        
        else:
            res.append(1)
        
    if type_attaque == "Psy":
        
        if type_defenseur in ("Acier","Psy"):
            res.append(0.5)
        
        elif type_defenseur in ("Combat","Poison","Ténèbres"):
            res.append(2)
        
        else:
            res.append(1)
        
    if type_attaque == "Ténèbres":
        
        if type_defenseur in ("Combat","Fee","Ténèbres"):
            res.append(0.5)
        
        elif type_defenseur == "Psy":
            res.append(0)
        
        elif type_defenseur in ("Spectre"):
            res.append(2)
        
        else:
            res.append(1)
            
    return res