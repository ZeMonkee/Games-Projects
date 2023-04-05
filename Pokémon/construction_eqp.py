import commande_pokemon as compkm
import commande_attaque as comatt
import Affichage_console as affc
import EV as ev
import random

def constr_attaque(pkm_entrer):
    
    print("\nMaintenant, vous devez chosisir 4 attaques à associer à votre " + pkm_entrer[1] + ", vous avez aussi accès au Pokedex d'attaques et aux autres paramètres précédents !")
    
    attaque_pkm = [[None, "Vide"], [None, "Vide"], [None, "Vide"], [None, "Vide"]]
    
    dmd_a = input("\nQue voulez vous faire ? \n- Entrer (une attaque) -\n- Pokedex (des attaques) -\n- Liste (des attaques entrées) -\n- Confirmer (Les attaques) -\n\n=> ")
    
    while True:
        
        if dmd_a == 'Entrer':
            id_att = input("\nQuel est l'ID de votre attaque ?\n=> ")
            
            try:
                
                nom, res = comatt.recherche_id(id_att)
                
                try:
                    
                    dmd_place = int(input("\nA quelle position voulez vous placer " + res[1] + " ? 1, 2, 3 ou 4 ?\n=> "))
                    
                    attaque_pkm[dmd_place-1] = res
                    
                    dmd_a = input("\nQue voulez vous faire ? \n- Entrer (une attaque) -\n- Pokedex (des attaques) -\n- Liste (des attaques entrées) -\n- Confirmer (Les attaques) -\n\n=> ")

                except ValueError:
                    
                    print("\nPlacement invalide, réessayez")
                    dmd_a = input("\nQue voulez vous faire ? \n- Entrer (une attaque) -\n- Pokedex (des attaques) -\n- Liste (des attaques entrées) -\n- Confirmer (Les attaques) -\n\n=> ")
                    
                
            except IndexError:
                
                print("\nID de l'attaque invalide, réessayez")
                dmd_a = input("\nQue voulez vous faire ? \n- Entrer (une attaque) -\n- Pokedex (des attaques) -\n- Liste (des attaques entrées) -\n- Confirmer (Les attaques) -\n\n=> ")
                
        elif dmd_a == 'Pokedex':
            comatt.pokedex_attaque()
            
            dmd_a = input("\nQue voulez vous faire ? \n- Entrer (une attaque) -\n- Pokedex (des attaques) -\n- Liste (des attaques entrées) -\n- Confirmer (Les attaques) -\n\n=> ")
       
        elif dmd_a == 'Liste':
            print("\nVoici vos attaques attribuées à " + pkm_entrer[1] + " pour l'instant:")
            
            affc.affichage_attaque(attaque_pkm)
            
            dmd_a = input("\nQue voulez vous faire ? \n- Entrer (une attaque) -\n- Pokedex (des attaques) -\n- Liste (des attaques entrées) -\n- Confirmer (Les attaques) -\n\n=> ")
        
        elif dmd_a == 'Confirmer':
            if attaque_pkm[0][0] != None and attaque_pkm[1][0] != None and attaque_pkm[2][0] != None and \
            attaque_pkm[3][0] != None:
                
                print("\nVoici vos attaques attribuées à " + pkm_entrer[1] + ":" )
                
                affc.affichage_attaque(attaque_pkm)
                
                dmd_conf = input("\nEtes vous sûr de votre choix ? \n- Oui -\n- Non -\n\n=> ")
                
                if dmd_conf == "Oui":
                    print("\nTrès bien !")
                    return attaque_pkm
                
                elif dmd_conf == "Non":
                    print("\nConfirmation annulée avec succès !")
                    dmd_a = input("\nQue voulez vous faire ? \n- Entrer (une attaque) -\n- Pokedex (des attaques) -\n- Liste (des attaques entrées) -\n- Confirmer (Les attaques) -\n\n=> ")
            
            else:
                print("\nVos attaques ne sont pas complête, veuillez entrer 4 attaques associées à votre pokémon valides pour finaliser votre pokémon !")
                dmd_a = input("\nQue voulez vous faire ? \n- Entrer (une attaque) -\n- Pokedex (des attaques) -\n- Liste (des attaques entrées) -\n- Confirmer (Les attaques) -\n\n=> ")
        else:
            print("\nOption non valide, veuillez réessayer.")
            dmd_a = input("\nQue voulez vous faire ? \n- Entrer (une attaque) -\n- Pokedex (des attaques) -\n- Liste (des attaques entrées) -\n- Confirmer (Les attaques) -\n\n=> ")





def demande_talent(pkm_entrer):
    
    talents = pkm_entrer[3].split()
    print("\nMaintenant, vous devez définir 1 talent à mettre sur votre " + pkm_entrer[1] + ", vous pouvez aussi accéder à leurs définitions !")
    dmd_t = input("\nQue voulez vous faire ? \n- Choisir (un talent) -\n- Definition (des talents) -\n\n=> ")
    
    while True:
        
        if dmd_t == "Choisir":
            
            print("\nChoisissez un talent parmis ceux proposés pour " + pkm_entrer[1] + ":\n")
            if len(talents) == 1:
                print("1 - " + talents[0])
                print("2 - Aucun Talent")
                
                dmd_tal = input("\n1 ou 2 ? \n\n=> ")
                
                if dmd_tal not in ("1","2"):
                    
                    print("\nTalent invalide, réessayez !\n")
                    dmd_t = input("\nQue voulez vous faire ? \n- Choisir (un talent) -\n- Definition (des talents) -\n\n=> ")
                
                elif dmd_tal == "2":
                    
                    return "Aucun Talent"
                
                else:
                    
                    dmd_tal = int(dmd_tal)
                    return talents[dmd_tal-1]
            
            elif len(talents) == 2:
                print("1 - " + talents[0])
                print("2 - " + talents[1])
                print("3 - Aucun Talent")
                
                dmd_tal = input("\n1, 2 ou 3 ? \n\n=> ")
                
                if dmd_tal not in ("1","2","3"):
                    
                    print("\nTalent invalide, réessayez !\n")
                    dmd_t = input("\nQue voulez vous faire ? \n- Choisir (un talent) -\n- Definition (des talents) -\n\n=> ")
                
                elif dmd_tal == "3":
                    
                    return "Aucun Talent"
                
                else:
                    
                    dmd_tal = int(dmd_tal)
                    return talents[dmd_tal-1]
                
            elif len(talents) == 3:
                print("1 - " + talents[0])
                print("2 - " + talents[1])
                print("3 - " + talents[2])
                print("4 - Aucun Talent")
                
                dmd_tal = input("\n1, 2, 3 ou 4 ? \n\n=> ")
                
                if dmd_tal not in ("1","2","3","4"):
                    
                    print("\nTalent invalide, réessayez !")
                    dmd_t = input("\nQue voulez vous faire ? \n- Choisir (un talent) -\n- Definition (des talents) -\n\n=> ")
                    
                elif dmd_tal == "4":
                    
                    return "Aucun Talent"
                
                else:
                    
                    dmd_tal = int(dmd_tal)
                    return talents[dmd_tal-1]
        
        
        elif dmd_t == "Definition":
            
            for i in talents:
                res, sav = compkm.definition_talent(i)
                
                print("\n" + i + ": " + sav[1])
            
            dmd_t = input("\nQue voulez vous faire ? \n- Choisir (un talent) -\n- Definition (des talents) -\n\n=> ")
            
        else:
            
            print("\nOption non valide, veuillez réessayer.")
            dmd_t = input("\nQue voulez vous faire ? \n- Choisir (un talent) -\n- Definition (des talents) -\n\n=> ")





def demande_sexe(pkm):
    
    dmd_sexe = input("\nChoisissez quel sexe attribué à votre " + pkm[1] + ' parmis "Male", "Female", "Asexual" \n\n=> ')
    
    while True:
        
        if dmd_sexe == "Male":
        
            return "Male"
    
        elif dmd_sexe == "Female":
        
            return "Female"
    
        elif dmd_sexe == "Asexual":
        
            return "Asexual"
    
        else:
        
            print("\nSexe invalide, réessayez !")
            dmd_sexe = input("\nChoisissez quel sexe attribué à votre " + pkm[1] + ' parmis "Male", "Female", "Asexual" \n\n=> ')
    




def demande_place(pkm):
    
    dmd_place = input("\nA quelle position voulez vous placer " + pkm[1] + " ? 1, 2, 3, 4, 5 ou 6 ?\n\n=> ")
    
    while True:
        
        if dmd_place not in ("1","2","3","4","5","6"):
        
            print("\nPlacement invalide, réessayez !")
            dmd_place = input("\nA quelle position voulez vous placer " + pkm[1] + " ? 1, 2, 3, 4, 5 ou 6 ?\n\n=> ")
        
        else:
            dmd_place = int(dmd_place)
            return dmd_place
    
def shiney_unlock():
    
    if random.randint(0,100) < 1:
        
        return True
    
    else:
        
        return False


def construction_equipes(nom_joueur):
    
    eqp_pokemons = [[[None, "Vide"]], [[None, "Vide"]], [[None, "Vide"]], [[None, "Vide"]], [[None, "Vide"]], [[None, "Vide"]]]
    
    constr_pkm = []
    
    print("\n" + nom_joueur + ", vous allez maintenant choisir votre équipe !")
    print("Pour choisir un pokémon, tapper 'Entrer', vous devrez alors entrer l'ID de celui-ci,")
    print("pour ce faire, vous pouvez consulter le pokédex en entrant l'option 'Pokedex' !")
    print("Lorsque vous entrerez l'ID du pokémon, choisissez ensuite son placement entre 1 et 6,")
    print("si vous entrez un pokémon par erreur, remplacez le tout simplement en entrant son placement avec le bon pokémon !")
    print("Enfin, vous pouvez consulter votre équipe en entrant 'Equipe', puis lorsque votre équipe sera au complet,")
    print("vous pourrez entrer 'Confirmer' pour valider votre équipe (à condition que celle ci contienne bien 6 pokémons) !")
    
    dmd_j = input("\nQue voulez vous faire ? \n- Entrer (un pokémon) -\n- Pokedex (des pokémons) -\n- Equipe (vos pokémons entrés) -\n- Confirmer (L'équipe) -\n\n=> ")
    
    while True:
        
        if dmd_j == 'Entrer':
            id_pkm = input("\nQuel est l'ID de votre pokémon ?\n=> ")
            
            try:
                
                nom, res = compkm.recherche_id(id_pkm)
                attaques = constr_attaque(res)
                talent = demande_talent(res)
                sexe = demande_sexe(res)
                print()
                affc.affichage_equipe(eqp_pokemons)
                place = demande_place(res)
                shiney = shiney_unlock()
                
                constr_pkm = ev.calcule_stats([res,attaques,"Aucun",talent,None,1,sexe,[1,1,1,1,1,1],0,place,shiney])
                
                eqp_pokemons[place-1] = constr_pkm
                
                print("\n" + nom + " a été ajouté dans votre équipe !\n")
                
                constr_pkm = []
                
                dmd_j = input("\nQue voulez vous faire ? \n- Entrer (un pokémon) -\n- Pokedex (des pokémons) -\n- Equipe (vos pokémons entrés) -\n- Confirmer (L'équipe) -\n\n=> ")
                
            except IndexError:
                
                print("\nPokémon invalide, réessayez")
                dmd_j = input("\nQue voulez vous faire ? \n- Entrer (un pokémon) -\n- Pokedex (des pokémons) -\n- Equipe (vos pokémons entrés) -\n- Confirmer (L'équipe) -\n\n=> ")
                
        elif dmd_j == 'Pokedex':
            compkm.pokedex()
            dmd_j = input("\nQue voulez vous faire ? \n- Entrer (un pokémon) -\n- Pokedex (des pokémons) -\n- Equipe (vos pokémons entrés) -\n- Confirmer (L'équipe) -\n\n=> ")
       
        elif dmd_j == 'Equipe':
            print("\nVoici votre équipe pour l'instant:")
            
            affc.affichage_equipe(eqp_pokemons)
            
            dmd_j = input("\nQue voulez vous faire ? \n- Entrer (un pokémon) -\n- Pokedex (des pokémons) -\n- Equipe (vos pokémons entrés) -\n- Confirmer (L'équipe) -\n\n=> ")
        
        elif dmd_j == 'Confirmer':
            if eqp_pokemons[0][0][0] != None and eqp_pokemons[1][0][0] != None and eqp_pokemons[2][0][0] != None and \
            eqp_pokemons[3][0][0] != None and eqp_pokemons[4][0][0] != None and eqp_pokemons[5][0][0] != None:
                
                print("\nVoici votre équipe complete:")
                
                affc.affichage_equipe(eqp_pokemons)
                
                dmd_conf = input("\n" + nom_joueur + ", êtes vous sûr de votre choix ? \n- Oui -\n- Non -\n\n=> ")
                
                if dmd_conf == "Oui":
                    print("\nTrès bien !")
                    return eqp_pokemons
                
                elif dmd_conf == "Non":
                    print("\nConfirmation annulée avec succès !")
                    dmd_j = input("\nQue voulez vous faire ? \n- Entrer (un pokémon) -\n- Pokedex (des pokémons) -\n- Equipe (vos pokémons entrés) -\n- Confirmer (L'équipe) -\n\n=> ")
            
            else:
                print("\nVotre équipe n'est pas complête, veuillez entrer 6 pokémons valides pour finaliser votre équipe !")
                dmd_j = input("\nQue voulez vous faire ? \n- Entrer (un pokémon) -\n- Pokedex (des pokémons) -\n- Equipe (vos pokémons entrés) -\n- Confirmer (L'équipe) -\n\n=> ")
        else:
            print("\nOption non valide, veuillez réessayer.")
            dmd_j = input("\nQue voulez vous faire ? \n- Entrer (un pokémon) -\n- Pokedex (des pokémons) -\n- Equipe (vos pokémons entrés) -\n- Confirmer (L'équipe) -\n\n=> ")
