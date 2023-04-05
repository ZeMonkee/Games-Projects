import Modulo_attaque as modatt
import Affichage_console as affc
import construction_eqp as ceqp


def attaque(num_attaque, attaquant, defenseur, ter):
    
    Niveau = 100
    Puissance = modatt.F_Puissance(num_attaque, ter, attaquant, defenseur)
    Attaque = modatt.F_Attaque(num_attaque, ter, attaquant)
    Defense = modatt.F_Defense(num_attaque, ter, attaquant, defenseur)
    Mod1 = modatt.Mod1(num_attaque, ter, attaquant, defenseur)
    Mod2 = modatt.Mod2(num_attaque, attaquant)
    Mod3 = modatt.Mod3(num_attaque, attaquant, defenseur)
    STAB = modatt.STAB(num_attaque, attaquant)
    CC = modatt.CC(attaquant)
    R = modatt.R()
    Type1, Type2 = modatt.aff_type(num_attaque, attaquant, defenseur)
    
    if Type1 == 0 or Type2 == 0:
        print("\nInefficace !")
        
    elif Type1 == 0.5 or Type2 == 0.5:
        print("\nPas très efficace !")
        
    elif Type1 == 2 or Type2 == 2:
        print("\nSuper efficace !")
    
    PV_defenseur = int(defenseur[0][4])
    
    pv_perdus = (((((((Niveau * 2 // 5) + 2) * Puissance * Attaque // 50) // Defense) * Mod1) + 2) * CC * Mod2 * R // 100) * STAB * Type1 * Type2 * Mod3
    
    PV_defenseur -= pv_perdus
    
    defenseur[0][4] = str(PV_defenseur)
    return round(pv_perdus)





def changement_pokemon(joueur, eqp_joueur, pkm_joueur):
    
    print()
    affc.aff_eqp_combat(eqp_joueur)
    
    dmd_envoie_pokemon = input("\nEntrez le numéro du pokémon à envoyer dans l'arène ! \n\n=> ")
    
    while True:
        
        try:
            if 1 < int(dmd_envoie_pokemon) > 6:
                print("N° de Pokémon invalide, choisissez un nombre entre 1 (premier pokémon) et 6 (le dernier) !")
                dmd_envoie_pokemon = input("\nEntrez le numéro du pokémon à envoyer dans l'arène ! \n\n=> ")
            
            else:
                verif_pkm = eqp_joueur[int(dmd_envoie_pokemon)-1]
        
            if int(verif_pkm[0][4]) <= 0:
                print("Pokemon KO ou invalide !")
                dmd_envoie_pokemon = input("\nEntrez le numéro du pokémon à envoyer dans l'arène ! \n\n=> ")
            
            elif pkm_joueur[9] == int(dmd_envoie_pokemon):
                print("Pokemon déjà sur le terrain !")
                dmd_envoie_pokemon = input("\nEntrez le numéro du pokémon à envoyer dans l'arène ! \n\n=> ")
            
            else:
                eqp_joueur[pkm_joueur[9]-1] = pkm_joueur
                pkm_joueur = verif_pkm
                print("\n" + pkm_joueur[0][1] + " GO !")
                return eqp_joueur, pkm_joueur
        
        except ValueError:
            
            print("\nNuméro de pokémon invalide, réessayez")
            dmd_envoie_pokemon = input("\nEntrez le numéro du pokémon à envoyer dans l'arène ! \n\n=> ")
    




def dialogue(nom_joueur, eqp_joueur, pokemon_j):
    
    print("\nTour de " + nom_joueur + ", choisissez l'action à effecter pour votre " + pokemon_j[0][1] + ":")
    dmd = input("\n- Attaque -\n- Sac -\n- Equipe -\n\n=> ")
    
    while True:
        
        if dmd ==  "Attaque":
            
            print()
            affc.aff_att_combat(pokemon_j)
            
            try:
                    
                dmd_attaque = int(input("\n" + nom_joueur + ", entrez le n° de l'attaque à effectuer pour " + pokemon_j[0][1] + ": "))
                
                return dmd_attaque-1
                

            except ValueError:
                    
                print("\nAttaque invalide, réessayez")
                dmd = input("\n- Attaque -\n- Sac -\n- Equipe -\n\n=> ")
        
        
        elif dmd == "Sac":
            
            print("\nSac vide...")
            dmd = input("\n- Attaque -\n- Sac -\n- Equipe -\n\n=> ")
        
        
        elif dmd == "Equipe":
            
            print()
            affc.aff_eqp_combat(eqp_joueur)
            print("\nQue voulez faire ?")
            dmd_eqp = input("\n- Changement -\n- Sortir -\n\n=> ")
                
            if dmd_eqp == "Changement":
                
                return "chgmt"
                
            elif dmd_eqp == "Sortir":
                
                dmd = input("\n- Attaque -\n- Sac -\n- Equipe -\n\n=> ")
                
            else:
                
                print("\nOption invalide, réessayez !")
                dmd = input("\n- Attaque -\n- Sac -\n- Equipe -\n\n=> ")
        
        else:
            
            print("\n\nChoix invalide, réessayez !")
            dmd = input("\n- Attaque -\n- Sac -\n- Equipe -\n\n=> ")
            
            
            
    

def arene(nom_j1, nom_j2, eqp_joueur1, eqp_joueur2, pkm_j1_res, pkm_j2_res, pokemon_j1, pokemon_j2, terrain):
    
    if int(pokemon_j1[0][9]) >= int(pokemon_j2[0][9]): # Le pokémon avec la plus grande vitesse commence => Joueur1
        
    
        #TOUR DU JOUEUR 1
        if int(pokemon_j1[0][4]) > 0 and int(pokemon_j2[0][4]) > 0:
            
            res_dial = dialogue(nom_j1, eqp_joueur1, pokemon_j1)
            
            if res_dial == "chgmt":
                
                eqp_joueur1, pokemon_j1 = changement_pokemon(nom_j1, eqp_joueur1, pokemon_j1)
                print("\nChangement de pokémon du joueur 1 effectué !")
            
            else:
                pokemon_j1[8] += 1
                degat = attaque(res_dial, pokemon_j1, pokemon_j2, terrain)
                print("\nPokémon de " + nom_j2 +" touché ! -" + str(degat) + " hp, pv restants de " + pokemon_j2[0][1] + ": " + pokemon_j2[0][4])
            
        elif int(pokemon_j1[0][4]) <= 0:
            
            pkm_j1_res -= 1
            
            if pkm_j1_res > 0:
                
                print(nom_j1 + ", Pokémon KO: " + pokemon_j1[0][1] + ", Pokémons restants: " + str(pkm_j1_res))
                eqp_joueur1, pokemon_j1 = changement_pokemon(nom_j1, eqp_joueur1, pokemon_j1)
        
            else:
                print(pokemon_j1[0][1] + " KO, " + nom_j1 + " n'a plus de pokémon debout !")
                return("End 2")
        #FIN DU TOUR DU JOUEUR 1
        
        
        #TOUR DU JOUEUR 2
        if int(pokemon_j2[0][4]) > 0 and int(pokemon_j1[0][4]) > 0:
            
            res_dial = dialogue(nom_j2, eqp_joueur2, pokemon_j2)
            
            if res_dial == "chgmt":
                
                eqp_joueur2, pokemon_j2 = changement_pokemon(nom_j2, eqp_joueur2, pokemon_j2)
                print("\nChangement de pokémon du joueur 2 effectué !")
            
            else:
                pokemon_j2[8] += 1
                degat = attaque(res_dial, pokemon_j2, pokemon_j1, terrain)
                print("\nPokémon de " + nom_j1 +" touché ! -" + str(degat) + " hp, pv restants de " + pokemon_j1[0][1] + ": " + pokemon_j1[0][4])
            
        elif int(pokemon_j2[0][4]) <= 0:
            pkm_j2_res -= 1
            
            if pkm_j2_res > 0:
                
                print(nom_j2 + ", Pokémon KO: " + pokemon_j2[0][1] + ", Pokémons restants: " + str(pkm_j2_res))
                eqp_joueur2, pokemon_j2 = changement_pokemon(nom_j2, eqp_joueur2, pokemon_j2)
            
            else:
                print(pokemon_j2[0][1] + " KO, " + nom_j2 + " n'a plus de pokémon debout !")
                return("End 1")
        #FIN DU TOUR DU JOUEUR 2
    
    
    
    elif int(pokemon_j1[0][9]) < int(pokemon_j2[0][9]): # Le pokémon avec la plus grande vitesse commence => Joueur2
        
    
        #TOUR DU JOUEUR 2
        if int(pokemon_j2[0][4]) > 0 and int(pokemon_j1[0][4]) > 0:
            
            res_dial = dialogue(nom_j2, eqp_joueur2, pokemon_j2)
            
            if res_dial == "chgmt":
                
                eqp_joueur2, pokemon_j2 = changement_pokemon(nom_j2, eqp_joueur2, pokemon_j2)
                print("\nChangement de pokémon du joueur 2 effectué !")
            
            else:
                pokemon_j2[8] += 1
                degat = attaque(res_dial, pokemon_j2, pokemon_j1, terrain)
                print("\nPokémon de " + nom_j1 +" touché ! -" + str(degat) + " hp, pv restants de " + pokemon_j1[0][1] + ": " + pokemon_j1[0][4])
            
        elif int(pokemon_j2[0][4]) <= 0:
            pkm_j2_res -= 1
            
            if pkm_j2_res > 0:
                
                print(nom_j2 + ", Pokémon KO: " + pokemon_j2[0][1] + ", Pokémons restants: " + str(pkm_j2_res))
                eqp_joueur2, pokemon_j2 = changement_pokemon(nom_j2, eqp_joueur2, pokemon_j2)
            
            else:
                print(pokemon_j2[0][1] + " KO, " + nom_j2 + " n'a plus de pokémon debout !")
                return("End 1")
        #FIN DU TOUR DU JOUEUR 2
        
        
        #TOUR DU JOUEUR 1
        if int(pokemon_j1[0][4]) > 0 and int(pokemon_j2[0][4]) > 0:
            
            res_dial = dialogue(nom_j1, eqp_joueur1, pokemon_j1)
            
            if res_dial == "chgmt":
                
                eqp_joueur1, pokemon_j1 = changement_pokemon(nom_j1, eqp_joueur1, pokemon_j1)
                print("\nChangement de pokémon du joueur 1 effectué !")
            
            else:
                pokemon_j1[8] += 1
                degat = attaque(res_dial, pokemon_j1, pokemon_j2, terrain)
                print("\nPokémon de " + nom_j2 +" touché ! -" + str(degat) + " hp, pv restants de " + pokemon_j2[0][1] + ": " + pokemon_j2[0][4])
            
        elif int(pokemon_j1[0][4]) <= 0:
            
            pkm_j1_res -= 1
            
            if pkm_j1_res > 0:
                
                print(nom_j1 + ", Pokémon KO: " + pokemon_j1[0][1] + ", Pokémons restants: " + str(pkm_j1_res))
                eqp_joueur1, pokemon_j1 = changement_pokemon(nom_j1, eqp_joueur1, pokemon_j1)
        
            else:
                print(pokemon_j1[0][1] + " KO, " + nom_j1 + " n'a plus de pokémon debout !")
                return("End 2")
        #FIN DU TOUR DU JOUEUR 1
    
    
    return eqp_joueur1, eqp_joueur2, pkm_j1_res, pkm_j2_res, pokemon_j1, pokemon_j2, terrain






def jeu():
    print("\nBIENVENUE DANS LE PLUS GRANDE JEU DE COMBAT POKÉMON DE L'HISTOIRE ! (ou pas)")
    print("\nLe principe est simple, 2 joueurs forment chacun une équipe de 6 pokémons parmis tout ceux de la 1er à la 5ème Générations,")
    print("la victoire revient à celui qui arrivera à vaincre les 6 pokémons de l'adversaire !")
    
    print("\nTrès bien, maintenant, veuillez s'il vous plait saisir vos noms !")
    
    dmd_n = False
    while dmd_n == False:
        
        nom_joueur_1 = str(input("\nNom du Joueur n°1: "))
        nom_joueur_2 = str(input("Nom du Joueur n°2: "))
        
        conf_nom = input("\n" + nom_joueur_1 + " et " + nom_joueur_2 + ", c'est bien ca ?\n\n- Oui -\n- Non -\n\n=> ")
        if conf_nom == "Oui":
            dmd_n = True
            
        elif conf_nom == "Non":
            print("\nVeuillez ressaisir vos noms dans ce cas.")
        
        else:
            print("\nConfirmation invalide... veuillez ressaisir vos noms svp.")
        
    print("\nParfait !")
    
    eqp_joueur1_jeu = ceqp.construction_equipes(nom_joueur_1)
    eqp_joueur2_jeu = ceqp.construction_equipes(nom_joueur_2)
    
    print(eqp_joueur1_jeu)
    print(eqp_joueur2_jeu)
    
    print("\nLes équipes sont maintant complêtes, que le combat commence !!\n")
    
    pkm_j1_res_jeu = 6
    pkm_j2_res_jeu = 6
    
    terrain_jeu = ["Aucun", "Aucun", "Aucun", "Aucun"]
    
    pokemon_j1_jeu = eqp_joueur1_jeu[0]
    pokemon_j2_jeu = eqp_joueur2_jeu[0]
    
    game_on = True
    
    print("1ER TOUR, C'EST PARTI !")
    while game_on == True:
        
        res = arene(nom_joueur_1, nom_joueur_2, eqp_joueur1_jeu, eqp_joueur2_jeu, pkm_j1_res_jeu, pkm_j2_res_jeu, pokemon_j1_jeu, pokemon_j2_jeu, terrain_jeu)
        
        if res == "End 1":
            game_on = False
            return("Fin de la partie, victoire de " + nom_joueur_1 + " !")
        
        elif res == "End 2":
            game_on = False
            return("Fin de la partie, victoire de " + nom_joueur_2 + " !")
        
        else:
            print("\n\nTOUR SUIVANT !")
            eqp_joueur1_jeu, eqp_joueur2_jeu, pkm_j1_res_jeu, pkm_j2_res_jeu, pokemon_j1_jeu, pokemon_j2_jeu, terrain_jeu = res
    