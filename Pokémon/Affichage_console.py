def affichage_equipe(eqp):
    print("1 - " + eqp[0][0][1])
    print("2 - " + eqp[1][0][1])
    print("3 - " + eqp[2][0][1])
    print("4 - " + eqp[3][0][1])
    print("5 - " + eqp[4][0][1])
    print("6 - " + eqp[5][0][1])
    

def affichage_attaque(l_att):
    print("1 - " + l_att[0][1])
    print("2 - " + l_att[1][1])
    print("3 - " + l_att[2][1])
    print("4 - " + l_att[3][1])
    

def aff_att_combat(pkm):
    print("1 - " + pkm[1][0][1] + " | " + pkm[1][0][2] + " | " + pkm[1][0][3] + " | PP restants: " + pkm[1][0][6])
    print("2 - " + pkm[1][1][1] + " | " + pkm[1][1][2] + " | " + pkm[1][1][3] + " | PP restants: " + pkm[1][1][6])
    print("3 - " + pkm[1][2][1] + " | " + pkm[1][2][2] + " | " + pkm[1][2][3] + " | PP restants: " + pkm[1][2][6])
    print("4 - " + pkm[1][3][1] + " | " + pkm[1][3][2] + " | " + pkm[1][3][3] + " | PP restants: " + pkm[1][3][6])


def aff_eqp_combat(eqp):
    print("1 - " + eqp[0][0][1] + " | " + eqp[0][0][2] + " | PV: " + eqp[0][0][4] + " | STATUT: " + eqp[0][2])
    print("2 - " + eqp[1][0][1] + " | " + eqp[1][0][2] + " | PV: " + eqp[1][0][4] + " | STATUT: " + eqp[1][2])
    print("3 - " + eqp[2][0][1] + " | " + eqp[2][0][2] + " | PV: " + eqp[2][0][4] + " | STATUT: " + eqp[2][2])
    print("4 - " + eqp[3][0][1] + " | " + eqp[3][0][2] + " | PV: " + eqp[3][0][4] + " | STATUT: " + eqp[3][2])
    print("5 - " + eqp[4][0][1] + " | " + eqp[4][0][2] + " | PV: " + eqp[4][0][4] + " | STATUT: " + eqp[4][2])
    print("6 - " + eqp[5][0][1] + " | " + eqp[5][0][2] + " | PV: " + eqp[5][0][4] + " | STATUT: " + eqp[5][2])