from graphicalgrid import GraphicalGrid

def creer_grille(n):
    grille = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append("")
        grille.append(ligne)
    return grille

def taille_cote(grille):
    taille_cote = 0
    for i in range(len(grille)):
        taille_cote += 1
    return taille_cote

def check_intervalle(grille,ligne,colonne):
    n = taille_cote(grille)
    if int(ligne) < 0 or int(ligne) > n-1 or int(colonne) < 0 or int(colonne) > n-1:
        return False
    else:
        return True

def est_vide(grille,ligne,colonne):
    if check_intervalle(grille,ligne,colonne) == False:
        return False
    elif grille[ligne][colonne] == " " or grille[ligne][colonne] == "":
        return True
    else:
        return False

def symbole_valide(symbole):
    if symbole == "X" or symbole == "O":
        return True
    else:
        return False

def ecrire(grille,ligne,colonne,symbole):
    if est_vide(grille,ligne,colonne) == False or symbole_valide(symbole) == False:
        return False
    else:
        grille[ligne][colonne] = symbole
        return grille

def effacer(grille,ligne,colonne):
    if check_intervalle(grille,ligne,colonne) == True: # On verifie si l'intervalle est vrai
        grille[ligne][colonne] = "" # si intervalle vrai alors on remplace le caractère
        return grille # on retourne la nouvelle grille avec caractère supprimer
    else:
        return False

def est(grille,ligne,colonne,symbole):
    if grille[ligne][colonne]== symbole:
        return True
    else:
        return False

def afficher(grille):
    n = taille_cote(grille)
    for ligne in range(n):  
        for colonne in range(n):
            if grille[ligne][colonne] == "":
                print(" ", end="")            
            print(" " + grille[ligne][colonne] + " ", end="")
            if colonne < n-1:
                print("|", end="")
        if ligne < n-1:
            print("\n" + n * "---" + (n-1) * "-")
    print("")
        
    return grille

def start(compteur):
    grille_size = input('Entrez la taille de la grille : ')
    if in_vide(grille_size,compteur) == True:
        if valide_int(grille_size) == True:                # Si on trouve un entier valide alors on le convertis en int pour creer la grille
            grille = string_to_int(grille_size)
            return creer_grille(grille)
        elif valide_int(grille_size) == False:             # Sinon on print() une erreur a l'utilisateur
            print("Il faut saisir un entier")
            return start(compteur)
    if in_vide(grille_size,compteur) == False:            # Si la saisie est vide on retourne à l'input
        return start(compteur)
    elif grille_size < 3:
        print("Veuillez entrer un nombre supérieur à 3")
        return start(compteur)
    return creer_grille(grille_size)

def continuer():
    keepcont = str(input("On continue ? [O]ui ou [N]on : "))
    if keepcont == "O" or keepcont == "o":
        return True
    if keepcont == "N" or keepcont == "n":
        print("La partie à été interrompue")
        return False
    else:
        print("Valeur incorrect")
        return continuer()

def joueur(compteur):
    x = "X"
    o = "O"
    if compteur % 2 == 0:
        return x        
    else:
        return o

def afficher_joueur(compteur):
    print("C'est au tour de joueur", joueur(compteur))


def in_vide(char,compteur):
    if char == "":
        return False
    else:
        return True

def in_espace(char):
    if char == " ":
        return True
    else:
        return False

def in_nombre(char):
    if char >= "0" and char <= "9":
        return True
    else:
        return False
    
def in_signe(char):
    if char == "+" or char == "-":
        return True
    else:
        return False

def in_tout_caractere(char):
    if char != " " :
        return True
    else:
        return False

def espace_valide(char):
    char_before = 0
    space_between = 0
    char_after = 0
    for i in range(len(char)):
        if in_tout_caractere(char[i]) == True and char_before == 0:
            char_before += 1
        elif char_before + space_between == 1 and in_espace(char[i]):
            space_between += 1
        elif char_before + space_between + char_after == 2 and in_tout_caractere(char[i]):
            char_after += 1
    if char_before + space_between + char_after == 3:
        return False
    else:
        return True

def valid_sign(char):
    sign = 0
    number = 0
    for i in range(len(char)):
        if in_signe(char[i]) == True and number > 0 and sign == 0:
            return False
        elif in_signe(char[i]) == True and number == 0:
            sign += 1
        elif in_nombre(char[i]) == True:
            number += 1
    if sign > 1:
        return False
    else:
        return True

def valide_int(char):
    number = 0
    for i in range(len(char)):
        if in_nombre(char[i]) == True:
            number += 1
    if valid_sign(char) == False:
        return False
    if number == 0:
        return False
    if espace_valide(char) == False:
        return False
    else:
        return True

def string_to_int(char):
    char = int(char)
    return char

def add_histo(historique,compteur):
    historique.append(compteur)
    return historique

def del_histo(historique):
    historique.pop()
    return historique

def dernier_coup_joue(historique,compteur):
    dernier_coup = historique[compteur]
    return dernier_coup

def annulation_coup(historique,compteur):
    dernier_coup = dernier_coup_joue(historique,compteur)
    if compteur > 0:
        print("Dernier coup joué = ligne :" , dernier_coup[0] , "; colonne :" , dernier_coup[1] , "; joueur :" , dernier_coup[2])
        annuler_coup = input("Voulez-vous annulez ce coup ? [O]ui ou [N]on : ")
        while (annuler_coup != "O" and annuler_coup != "N") and (annuler_coup != "o" and annuler_coup != "n"):
            annuler_coup = input("Veuillez répondre par O ou N\nVoulez-vous annulez ce coup ? [O]ui ou [N]on : ")
        if annuler_coup == "O" or annuler_coup == "o":
            return True
        elif annuler_coup == "N" or annuler_coup == "n":
            return False
    return False

def verif_ligne(compteur,grille):
    in_ligne_true = False
    while (not in_ligne_true):
        in_ligne = input("Entrez le numéro de la ligne (appuyez sur entrée pour annuler la saisie : ")
        if in_vide(in_ligne,compteur) == True:
            if valide_int(in_ligne) == True:
                in_ligne = string_to_int(in_ligne)
                return in_ligne
            elif valide_int(in_ligne) == False:
                print("Il faut saisir un entier")
                return verif_ligne(compteur,grille)
        else:
            return tour_actuel(compteur,grille)

def verif_colonne(compteur,grille):
    in_colonne_true = False
    while (not in_colonne_true):
        in_colonne = input("Entrez le numéro de la colonne (appuyez sur entrée pour annuler la saisie : ")
        if in_vide(in_colonne,compteur) == True:
            if valide_int(in_colonne) == True:
                in_colonne = string_to_int(in_colonne)
                return in_colonne
            elif valide_int(in_colonne) == False:
                print("Il faut saisir un entier")
                return verif_colonne(compteur,grille)
        else:
            return tour_actuel(compteur,grille)

def demande_coord(compteur,grille):
    n = taille_cote(grille)
    ligne = verif_ligne(compteur,grille)
    if int(ligne) < 0:
        print("Veuillez entrer un numéro de ligne valide\n")
        return demande_coord(compteur,grille)
    colonne = verif_colonne(compteur,grille)
    if int(colonne) < 0:
        print("Veuillez entrer un numéro de colonne valide\n")
        return demande_coord(compteur,grille)
    return ligne,colonne                        # Le return appelle les fonctions des coordonnées


def victoire_ligne(grille,ligne,symbole):
    victoire = True       # Variable permettant de valider si tout les symboles sont les mêmes
    for colonne in range(len(grille)):
        if est(grille,ligne,colonne,symbole) == False:
            victoire = False
    return victoire

def victoire_colonne(grille,colonne,symbole):
    victoire = True
    for ligne in range(len(grille)):
        if est(grille,ligne,colonne,symbole) == False:
            victoire = False
    return victoire

def victoire_diagonale(grille,symbole):
    victoire = True
    for diag in range(len(grille)):
        if est(grille,diag,diag,symbole) == False:
            victoire = False
    return victoire

def victoire_diagonale_inverse(grille,symbole):
    victoire = True
    for diagonale in range(len(grille)):
        diagonale_inverse = (len(grille)-1)-diagonale
        if est(grille,diagonale,diagonale_inverse,symbole) == False:
            victoire = False
    return victoire

def verification_victoire(grille,ligne,colonne,symbole):
    if victoire_ligne(grille,ligne,symbole) == True:
        return True
    elif victoire_colonne(grille,colonne,symbole) == True:
        return True
    elif victoire_diagonale(grille,symbole) == True:
        return True
    elif victoire_diagonale_inverse(grille,symbole) == True:
        return True
    else:
        return False

def tour_actuel(compteur,grille):
    afficher_joueur(compteur)
    tuple_coord = demande_coord(compteur,grille)
    ligne = int(tuple_coord[0])
    colonne = int(tuple_coord[1])
    histo_tour_actuel = []
    if not est_vide(grille,ligne,colonne):
        print("La case choisie n'est pas vide")
        return tour_actuel(compteur,grille)
    histo_tour_actuel.append(ligne)
    histo_tour_actuel.append(colonne)
    histo_tour_actuel.append(joueur(compteur))
    return histo_tour_actuel # Renvoie [ligne , colonne , symbole]

def tour(compteur,grille,historique,grille_graphique):
    compteur += 1
    histo_tour_actuel = tour_actuel(compteur,grille)
    ecrire(grille,histo_tour_actuel[0],histo_tour_actuel[1],histo_tour_actuel[2])
    grille_graphique.write(histo_tour_actuel[0],histo_tour_actuel[1],histo_tour_actuel[2])
    historique = add_histo(historique,histo_tour_actuel)
    while annulation_coup(historique,compteur) == True and compteur > 0:
        effacer(grille,historique[len(historique)-1][0],historique[len(historique)-1][1])
        grille_graphique.erase(historique[len(historique)-1][0],historique[len(historique)-1][1])
        historique = del_histo(historique)
        print(historique)
        compteur -= 1
    victoire = verification_victoire(grille,histo_tour_actuel[0],histo_tour_actuel[1],histo_tour_actuel[2])
    return victoire,compteur

def game():
    compteur = 0
    historique = [[0,0,"O"]]
    victoire = False
    grille = start(compteur)
    taille_grille = len(grille) * len(grille)
    if len(grille) < 3:
        print("Veuillez entrer un nombre supérieur à 3")
        return game()
    grille_graphique = GraphicalGrid(len(grille))
    while victoire == False and taille_grille != compteur and continuer() :
        tuple_tour = tour(compteur,grille,historique,grille_graphique)
        compteur = tuple_tour[1]
        victoire = tuple_tour[0]
    if taille_grille == compteur:
        print("Match nul")
    if victoire == True:
        print("Le joueur" , joueur(compteur) , "a gagné !")
    return 0

print(game())