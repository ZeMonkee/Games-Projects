import random
  

def affichage_ev(l_ev):
    print()
    print("1.EV PV - " + str(l_ev[0]))
    print("2.EV ATT - " + str(l_ev[1]))
    print("3.EV DEF - " + str(l_ev[2]))
    print("4.EV ATT SPE - " + str(l_ev[3]))
    print("5.EV ATT DEF - " + str(l_ev[4]))
    print("6.EV VITESSE - " + str(l_ev[5]))

def repartir_ev():

    total_ev = 510
    ev = [0, 0, 0, 0, 0, 0]
    while total_ev > 0:

        affichage_ev(ev)
        print("\nEV restants :", total_ev)
        choix = input("Choisissez un choix (1-6) ou 's' pour supprimer des EV : ")
        if choix == "s":
            try:
                supprimer = int(input("Combien de EV voulez-vous supprimer ? "))
                if supprimer < 0:
                    raise ValueError("\nNombre EV invalide\n")
                index = int(input("De quel choix voulez-vous supprimer des EV ? "))
                if index > 6 or index < 0:
                    raise ValueError("\nChoix invalide\n")
                if ev[index-1] < supprimer:
                    raise ValueError("\nImpossible de supprimer plus de EV que le choix en possède\n")
                ev[index-1] -= supprimer
                total_ev += supprimer
            except ValueError:
                print("\nChoix invalide\n")
        else:
            try:
                choix = int(choix)
                if choix < 1 or choix > 6:
                    print("\nChoix invalide\n")
                
                else:
                    ev_max = min(255, total_ev)
                    ev_entres = int(input(f"Entrez le nombre de ev pour le choix {choix} (maximum {ev_max}) : "))
                    ev_restants = total_ev - ev_entres
                    if ev_entres > ev_max or ev_entres < 0 or ev[choix-1] + ev_entres > 255 or ev_restants < 0:
                        print("\nNombre de EV invalide\n")

                    else:
                        ev[choix-1] += ev_entres
                        total_ev -= ev_entres
            
            except ValueError:
                print("\nVeuillez entrer un nombre valide.\n")
    
    affichage_ev(ev)
    
    return ev




def calcule_stats(pkm_ig):
     
    Niveau = 100
    stats_pkm = pkm_ig[0]
    
    pk_nom = stats_pkm[1]
    pk_pv = int(stats_pkm[4])
    pk_att = int(stats_pkm[5])
    pk_def = int(stats_pkm[6])
    pk_att_spe = int(stats_pkm[7])
    pk_def_spe = int(stats_pkm[8])
    pk_vitesse = int(stats_pkm[9])
    
    print("\nBien, maintenant vous devez répartir vos points EV (Effort Values) sur votre " + pk_nom + " !")
    print("Les EV permettent en gros de booster, à partir d'un système de répartissions de points, les stats de votre pokémon !")
    
    ev_pv, ev_att, ev_def, ev_att_spe, ev_def_spe, ev_vitesse = repartir_ev()
    
    ev_pv = round((( 31 + 2 * pk_pv + (ev_pv // 4) ) * Niveau // 100 ) + Niveau + 10)
    
    nature = ["Solo","Brave","Rigide","Mauvais","Assuré","Relax","Malin","Lâche",
              "Timide","Pressé","Jovial","Naïf","Modeste","Doux","Discret",
              "Foufou","Calme","Gentil","Malpoli","Prudent","Bizarre","Docile"
              ,"Hardi","Pudique","Sérieux"]
    
    dmd_nature = random.choice(nature)
    
    # Bonus Attaque
    if dmd_nature == "Solo":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1.1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 0.9)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
        
    elif dmd_nature == "Brave":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1.1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 0.9)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
    
    elif dmd_nature == "Rigide":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1.1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 0.9)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
    
    elif dmd_nature == "Mauvais":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1.1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 0.9)
        
    # Bonus Défense
    elif dmd_nature == "Assuré":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 0.9)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1.1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
    
    elif dmd_nature == "Relax":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1.1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 0.9)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
    
    elif dmd_nature == "Malin":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1.1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 0.9)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
    
    elif dmd_nature == "Lâche":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1.1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 0.9)
    
    # Bonus Vitesse
    elif dmd_nature == "Timide":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 0.9)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1.1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
    
    elif dmd_nature == "Pressé":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 0.9)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1.1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
    
    elif dmd_nature == "Jovial":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1.1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 0.9)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
    
    elif dmd_nature == "Naïf":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1.1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 0.9)
    
    # Bonus Attaque Spéciale
    elif dmd_nature == "Modeste":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 0.9)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1.1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
    
    elif dmd_nature == "Doux":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 0.9)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1.1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
    
    elif dmd_nature == "Discret":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 0.9)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1.1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
    
    elif dmd_nature == "Foufou":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1.1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 0.9)
        
    # Bonus Défense Spéciale
    elif dmd_nature == "Calme":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 0.9)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1.1)

    elif dmd_nature == "Gentil":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 0.9)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1.1)        
    
    elif dmd_nature == "Malpoli":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 0.9)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1.1)
    
    elif dmd_nature == "Prudent":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 0.9)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1.1)
    
    # Sans effet
    elif dmd_nature == "Bizarre":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
    
    elif dmd_nature == "Docile":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
    
    elif dmd_nature == "Hardi":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
    
    elif dmd_nature == "Pudique":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
    
    elif dmd_nature == "Sérieux":
        ev_att = round(((( 31 + 2 * pk_att + (ev_att // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def = round(((( 31 + 2 * pk_def + (ev_def // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_vitesse = round(((( 31 + 2 * pk_vitesse + (ev_vitesse // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_att_spe = round(((( 31 + 2 * pk_att_spe + (ev_att_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
        ev_def_spe = round(((( 31 + 2 * pk_def_spe + (ev_def_spe // 4) ) * Niveau // 100 ) + 5 ) * 1)
    
    pkm_ig[0][4] = ev_pv
    pkm_ig[0][5] = ev_att
    pkm_ig[0][6] = ev_def
    pkm_ig[0][7] = ev_att_spe
    pkm_ig[0][8] = ev_def_spe
    pkm_ig[0][9] = ev_vitesse
    
    return pkm_ig
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    