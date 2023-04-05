import random
import commande_pokemon as compkm
import affinites_types as afft

def R():
    return (random.randint(217, 255)*100)//255

# [[STATS_PKM],[[ATT1], [ATT2], [ATT3], [ATT4]],ETAT,TALENT,STATUT,CRIT_LVL,SEXE,[SMATT,SMDEF,SMPREC,SMESQ],NB_TOURS]

def STAB(n_att, pkm_att_ig):
    
    type_pkm = pkm_att_ig[0][2]
    talent_pkm = pkm_att_ig[3]
    type_att_pkm = pkm_att_ig[1][n_att][2] 
    
    if type_pkm == type_att_pkm and talent_pkm == "Adaptabilité":
        return 2
    
    elif type_pkm == type_att_pkm:
        return 1.5
    
    else:
        return 1
    

def aff_type(n_att, pkm_att_ig, pkm_def_ig):
    
    type1 = [1]
    type2 = [1]
    type_att_pkm = pkm_att_ig[1][n_att][2]
    type_def_ig = pkm_def_ig[0][2].split() # split => coupé une chaine de caractere en 2 quand celle ci est séparé par un espace (place dans une liste)
    
    if len(type_def_ig) == 1:
        
        type_n1 = type_def_ig[0]
        type1 = afft.affinite_type(type_att_pkm, type_n1)
    
    else:
        
        type_n1 = type_def_ig[0]
        type_n2 = type_def_ig[1]
        
        type1 = afft.affinite_type(type_att_pkm, type_n1)
        type2 = afft.affinite_type(type_att_pkm, type_n2)
    
    type1 = type1[0]
    type2 = type2[0]
    
    return type1, type2


def Mod1(n_att, terrain, pkm_att_ig, pkm_def_ig):
    
    BNR = 1
    RL = 1
    SR = 1
    FF = 1
    meteo = terrain[0]
    cat_att = pkm_att_ig[1][n_att][3]
    type_att = pkm_att_ig[1][n_att][2]
    etat_pkm_att = pkm_att_ig[2]
    talent_pkm_att = pkm_att_ig[3]
    statut_pkm_def = pkm_def_ig[4]
    statut_pkm_att = pkm_att_ig[4]
    
    if etat_pkm_att == "Bruler" and cat_att == "Physique" and talent_pkm_att != "Cran":
        
        BNR = 0.5
        
    if "Protection" in statut_pkm_def and cat_att == "Physique":
        
        RL = 0.5
    
    if "Mur Lumière" in statut_pkm_def and cat_att == "Spéciale":
        
        RL = 0.5
        
    if (meteo == "Pluie" and type_att == "Eau") or (meteo == "Soleil" and type_att == "Feu"):
        
        SR = 1.5
    
    if (meteo == "Pluie" and type_att == "Feu") or (meteo == "Soleil" and type_att == "Eau"):
        
        SR = 0.5
        
    if "Torche" in statut_pkm_att and type_att == "Feu":
        
        FF = 1.5
        
    return round(BNR * RL * SR * FF)


def Mod2(n_att, pkm_att_ig):
    
    if pkm_att_ig[1][n_att][1] == "Moi d'Abord":
        
        return 1.5
    
    else:
        return 1
    


def Mod3(n_att, pkm_att_ig, pkm_def_ig):
    
    SRF = 1
    TL = 1
    talent_pkm_def = pkm_def_ig[3]
    talent_pkm_att = pkm_att_ig[3]
    affinité1, affinité2 = aff_type(n_att, pkm_att_ig, pkm_def_ig)
    
    if talent_pkm_def == "Solide-Roc" or talent_pkm_def == "Filtre":
        
        if affinité1 == 1.5 or affinité2 == 1.5:
            
            SRF = 0.75
    
    if talent_pkm_att == "Lentiteintée" and (affinité1 == 0.5 or affinité2 == 0.5):
        
        TL = 2
        
    return round(SRF * TL)



def CC(pkm_att_ig):
    
    crit_lvl_att = int(pkm_att_ig[5])
    talent_pkm_att = pkm_att_ig[3]
    pourc_crit = 0
    
    if crit_lvl_att == 1:
        
        pourc_crit = 6.25
        
    elif crit_lvl_att == 2:
        
        pourc_crit = 12.5
        
    elif crit_lvl_att == 3:
        
        pourc_crit = 25
    
    elif crit_lvl_att == 4:
        
        pourc_crit = 33.3
    
    elif crit_lvl_att == 5:
        
        pourc_crit = 50
        
    
    if random.randint(0,100) < pourc_crit and talent_pkm_att == "Sniper":
        
        print("Coup critique !")
        return 3
    
    elif random.randint(0,100) < pourc_crit:
        
        print("Coup critique !")
        return 2
    
    else:
        
        return 1
        


def F_Puissance(n_att, terrain, pkm_att_ig, pkm_def_ig):
    
    type_att = pkm_att_ig[1][n_att][2]
    pv_pkm_att = int(pkm_att_ig[0][4])
    nom, pv_base_pkm_att = compkm.recherche_id(pkm_att_ig[0][0])
    statut_pkm_att = pkm_att_ig[4]
    etat_gen_terr = terrain[3]
    talent_pkm_def = pkm_def_ig[3]
    talent_pkm_att = pkm_att_ig[3]
    sexe_pkm_att = pkm_att_ig[6]
    sexe_pkm_def = pkm_def_ig[6]
    nom_att = pkm_att_ig[1][n_att][1]
    attaque_contre_coup = ("Bélier", "Boutefeu", "Damoclès", "Éclair Fou", "Électacle", "Fracass'Tête", "Peignée", "Pied Sauté", "Pied Voltige", "Rapace", "Sacrifice")
    
    BP = int(pkm_att_ig[1][n_att][4])
    CHG = 1
    MS = 1
    WS = 1
    UA = 1
    FA = 1
    
    if "Chargeur" in statut_pkm_att and type_att == "Électrik":
        CHG = 2
        
    if "Lance-Boue" in etat_gen_terr and type_att == "Électrik":
        MS = 0.5
    
    if "Tourniquet" in etat_gen_terr and type_att == "Feu":
        WS = 0.5
        
    if talent_pkm_att == "Rivalité":
        
        if (sexe_pkm_att == "Male" and sexe_pkm_def == "Male") or (sexe_pkm_att == "Female" and sexe_pkm_def == "Female"):
            
            UA = 1.25
        
        elif (sexe_pkm_att == "Male" and sexe_pkm_def == "Female") or (sexe_pkm_att == "Female" and sexe_pkm_def == "Male"):
            
            UA = 0.75
    
    if pv_pkm_att < (int(pv_base_pkm_att[4]) // 1//3):
        
        if talent_pkm_att == "Brasier" and type_att == "Feu":
            
            UA = 1.5
            
        elif talent_pkm_att == "Torrent" and type_att == "Eau":
            
            UA = 1.5
            
        elif talent_pkm_att == "Engrais" and type_att == "Plante":
            
            UA = 1.5
        
        elif talent_pkm_att == "Essaim" and type_att == "Insecte":
            
            UA = 1.5
        
    if talent_pkm_att == "Technicien" and BP <= 60:
        
        UA = 1.5
        
    if talent_pkm_att == "Poing-de-Fer" and ("Poing" in nom_att or "poing" in nom_att or "percut" in nom_att):
        
        UA = 1.2
        
    if talent_pkm_att == "Téméraire" and nom_att in attaque_contre_coup:
        
        UA = 1.2
        
    if talent_pkm_def == "Isograisse" and (type_att == "Feu" or type_att == "Glace"):
        
        FA = 0.5
        
    if talent_pkm_def == "Ignifuge" and type_att == "Feu":
        
        FA = 0.5
        
    if talent_pkm_def == "Peau-Sèche" and type_att == "Feu":
        
        FA = 1.25
        
    return round(BP * CHG * MS * WS * UA * FA)
        
    
    
def F_Attaque(n_att, terrain, pkm_att_ig):
    
    cat_att = pkm_att_ig[1][n_att][3]
    talent_pkm_att = pkm_att_ig[3]
    meteo = terrain[0]
    etat_pkm_att = pkm_att_ig[2]
    nb_tours_pkm_att = pkm_att_ig[8]
    
    Stat = 0
    SM = 0
    AM = 1
    
    if cat_att == "Physique":
        
        Stat = int(pkm_att_ig[0][5])
        SM = int(pkm_att_ig[7][0])
        
        if talent_pkm_att == "Force-Pure" or talent_pkm_att == "Coloforce":
            
            AM = 2
            
        if talent_pkm_att == "Don-Floral" and meteo == "Soleil":
            
            AM = 1.5
            
        if talent_pkm_att == "Cran" and etat_pkm_att in ("Bruler", "Paralyser", "Empoisonner", "Endormi", "Geler"):
            
            AM = 1.5
            
        if talent_pkm_att == "Agitation":
            
            AM = 1.5
            
        if talent_pkm_att == "Début-Calme" and nb_tours_pkm_att < 5:
            
            AM = 0.5
        
        
    elif cat_att ==  "Spéciale":
        
        Stat = int(pkm_att_ig[0][7])
        SM = int(pkm_att_ig[7][2])
    
        if talent_pkm_att == "Force-Soleil" and meteo == "Soleil":
            
            AM = 1.5
    
    return round(Stat * SM * AM)


def F_Defense(n_att, terrain, pkm_att_ig, pkm_def_ig):
    
    cat_att = pkm_att_ig[1][n_att][3]
    nom_att = pkm_att_ig[1][n_att][1]
    talent_pkm_def = pkm_def_ig[3]
    etat_pkm_def = pkm_def_ig[2]
    meteo = terrain[0]
    type_pkm_def = pkm_def_ig[0][2]
    
    Stat = 0
    SM = 0
    Mod = 1
    SX = 1
    
    if cat_att == "Physique":
        
        Stat = int(pkm_def_ig[0][6])
        SM = int(pkm_att_ig[7][1])
        
        if talent_pkm_def == "Écaille-Spéciale" and etat_pkm_def in ("Bruler", "Paralyser", "Empoisonner", "Endormi", "Geler"):
            
            Mod = 1.5
            
        
    elif cat_att == "Spécial":
    
        Stat = int(pkm_att_ig[0][8])
        SM = int(pkm_att_ig[7][3])
        
        if meteo == "Tempete de sable" and "Roche" in type_pkm_def:
            
            Mod = 1.5
            
        if talent_pkm_def == "Don-Floral" and meteo == "Soleil":
            
            Mod = 1.5
         
    if nom_att == "Destruction" or nom_att == "Explosion":
        
        SX = 0.5
        
    
    return round(Stat * SM * Mod * SX)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    