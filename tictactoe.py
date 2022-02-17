from graphicalgrid import GraphicalGrid

###########################################################################################################
# On créer la grille                                                                                   ####
###########################################################################################################

def creer_grille(n):
    grille = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append("")
        grille.append(ligne)
    return grille

###########################################################################################################
# On calcule la taille d'un côté de la grille                                                          ####
###########################################################################################################

def taille_cote(grille):
    taille_cote = 0
    for i in range(len(grille)):
        taille_cote += 1
    return taille_cote

###########################################################################################################
# On vérifie si la ligne et la colonne sont dans l'intervalle de la grille                             ####
###########################################################################################################

def check_intervalle(grille,ligne,colonne):
    n = taille_cote(grille)
    if int(ligne) < 0 or int(ligne) > n-1 or int(colonne) < 0 or int(colonne) > n-1:
        return False
    else:
        return True

###########################################################################################################
# On vérifie si la grille est vide à indice [ligne][colonne] de la grille                              ####
###########################################################################################################

def est_vide(grille,ligne,colonne):
    if check_intervalle(grille,ligne,colonne) == False:
        return False
    elif grille[ligne][colonne] == " " or grille[ligne][colonne] == "":
        return True
    else:
        return False

###########################################################################################################
# On vérifie si le symbole rentré est valide                                                           ####
###########################################################################################################

def symbole_valide(symbole):
    if symbole == "X" or symbole == "O":
        return True
    else:
        return False

###########################################################################################################
# On écris le symbole à indice [ligne][colonne] dans la grille                                         ####
###########################################################################################################

def ecrire(grille,ligne,colonne,symbole):
    if est_vide(grille,ligne,colonne) == False or symbole_valide(symbole) == False:
        return False
    else:
        grille[ligne][colonne] = symbole
        return grille

###########################################################################################################
# On efface un symbole à indice [ligne][colonne] dans la grille                                        ####
###########################################################################################################

def effacer(grille,ligne,colonne):
    if check_intervalle(grille,ligne,colonne) == True:
        grille[ligne][colonne] = ""
        return grille
    else:
        return False

###########################################################################################################
# On vérifie s'il y a un symbole à indice [ligne][colonne] dans la grille                              ####
###########################################################################################################

def est(grille,ligne,colonne,symbole):
    if grille[ligne][colonne]== symbole:
        return True
    else:
        return False

###########################################################################################################
# On affiche la grille complète                                                                        ####
###########################################################################################################

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

###########################################################################################################
# On demande la taille de grille (init du jeu)                                                         ####
###########################################################################################################

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

###########################################################################################################
# On demande si le joueur veut continuer                                                               ####
###########################################################################################################

def continuer():
    on_continue = str(input("On continue ? [O]ui ou [N]on : "))
    if on_continue == "O" or on_continue == "o":
        return True
    if on_continue == "N" or on_continue == "n":
        return False
    else:
        print("Valeur incorrect")
        return continuer()

###########################################################################################################
# On cherche à qui est le tour                                                                         ####
###########################################################################################################

def joueur(compteur):
    x = "X"
    o = "O"
    if compteur % 2 == 0:
        return x        
    else:
        return o

def afficher_joueur(compteur):
    print("C'est au tour du joueur", joueur(compteur))

###########################################################################################################
# Ici on fait plusieurs vérifications                                                                  ####
# Si c'est vide, s'il y a un espace, un nombre compris entre 0 et 9, un signe ou tout autre caractere  ####
###########################################################################################################

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

###########################################################################################################
# On cherche si l'espace est valide ou non                                                             ####
###########################################################################################################

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

###################################################################################################
# On cherche si le signe est valide ou non                                                     ####
# Et la même chose pour les entiers (valide_int)                                               ####
# Si c'est valide on convertis ensuite les chaines de caractères en entiers                    ####
###################################################################################################

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

###################################################################################################
# Gestion de l'historique                                                                      ####
# On ajoute, supprime et sauvegarde le dernier coup joué a chaque tour                         ####
###################################################################################################


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

###################################################################################################
# On vérifie l'input de la ligne et de la colonne à l'aide des fonctions précédentes           ####
#----------------------------------------------------------------------------------------------####
# Si valide alors on retourne un tuple avec ligne et colonne                                   ####
# Sinon on renvoie un message d'erreur                                                         ####
###################################################################################################

def verif_ligne(compteur,grille):
    in_ligne_true = False
    while (not in_ligne_true):
        in_ligne = input("Entrez le numéro de la ligne (appuyez sur entrée pour annuler la saisie) : ")
        if in_vide(in_ligne,compteur) == True:
            if valide_int(in_ligne) == True:
                in_ligne = string_to_int(in_ligne)
                return in_ligne
            elif valide_int(in_ligne) == False:
                print("Il faut saisir un entier")
                return verif_ligne(compteur,grille)
        else:
            if continuer() == False:
                in_ligne_true = True
            else:
                afficher_joueur(compteur)
    return False

def verif_colonne(compteur,grille):
    in_colonne_true = False
    while (not in_colonne_true):
        in_colonne = input("Entrez le numéro de la colonne (appuyez sur entrée pour annuler la saisie) : ")
        if in_vide(in_colonne,compteur) == True:
            if valide_int(in_colonne) == True:
                in_colonne = string_to_int(in_colonne)
                return in_colonne
            elif valide_int(in_colonne) == False:
                print("Il faut saisir un entier")
                return verif_colonne(compteur,grille)
        else:
            if continuer() == False:
                in_colonne_true = True
            else:
                afficher_joueur(compteur)

    return "Faux"
            

def demande_coord(compteur,grille):
    n = taille_cote(grille)
    ligne = verif_ligne(compteur,grille)
    if str(ligne) == "Faux":
        return "Faux"
    elif int(ligne) < 0:
        print("Veuillez entrer un numéro de ligne valide\n")
        return demande_coord(compteur,grille)

    colonne = verif_colonne(compteur,grille)
    if str(colonne) == "Faux":
        return "Faux"
    elif int(colonne) < 0:
        print("Veuillez entrer un numéro de colonne valide\n")
        return demande_coord(compteur,grille)

    return ligne,colonne

###################################################################################################
# On vérifie ici les conditions de victoire                                                    ####
# D'abord par ligne et ensuite par colonne, diagonale ou diagonale inversée                    ####
###################################################################################################

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

############################################################################################################
# Fonction tour et tour actuel                                                                          ####
# On compte le nombre de tour, on écrit et/ou on supprime les symboles à indice ligne/colonne           ####
############################################################################################################

def tour_actuel(compteur,grille):
    afficher_joueur(compteur)
    tuple_coord = demande_coord(compteur,grille)
    if tuple_coord == "Faux":
        return "Faux"
    else:
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
    if str(histo_tour_actuel) == "Faux":
        return "Faux"
    else:
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

#################################################################################
# Fonction Main                                                              ####
#################################################################################

def game():
    # Initialisation des variables :
    compteur = 0
    historique = [[0,0,"O"]]
    victoire = False
    # On initialise la grille puis on la modifie :
    grille = start(compteur)
    taille_grille = len(grille) * len(grille)

    if len(grille) < 3:
        print("Veuillez entrer un nombre supérieur à 3")
        return game()
    grille_graphique = GraphicalGrid(len(grille))

    # Déroulement du jeu
    while victoire == False and taille_grille != compteur and continuer() :
        tuple_tour = tour(compteur,grille,historique,grille_graphique)

        if str(tuple_tour) == "Faux":
            print("La partie à été interrompue")
            return 1
        compteur = tuple_tour[1]
        victoire = tuple_tour[0]

    if victoire == True:
        print("Le joueur" , joueur(compteur) , "a gagné !")
    elif taille_grille == compteur:
        print("Match nul | La partie est terminée.")
    else:
            print("La partie à été interrompue")
            return 0

print(game())


#################################################################################
# Déclaration des return dans main :                                         ####
#-------------------------------------------------------------------------------#
# return 0 : Bon déroulement du programme avec gagnant ou match nul          ####
# return 1 : La partie à été interrompue volontairement                      ####
#-------------------------------------------------------------------------------#
#################################################################################




##################################################################################################################################################################
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#######################################################################| Fin du programme |#######################################################################
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
##################################################################################################################################################################