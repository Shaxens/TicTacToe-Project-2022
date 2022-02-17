from graphicalgrid import GraphicalGrid

#----------------------------
# Création de la grille :
# Entrée : n
# Sortie : -> list[list[int]]
#----------------------------


def creer_grille(n):
    grille = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append("")
        grille.append(ligne)

    return grille

# print(creer_grille(5))

#----------------------------------------------
# On cherche la taille d'un côté de la grille :
# Entrée : grille
# Sortie : -> int
#----------------------------------------------

def taille_cote(grille):
    taille_cote = 0
    for i in range(len(grille)):
        taille_cote += 1
    return taille_cote

#-------------------------------------------------------------
# On vérifie si la ligne et la colonne sont dans l'intervalle
# Entrée : grille, ligne, colonne
# Sortie : False si ligne et/ou colonne hors de l'intervalle
#-------------------------------------------------------------


def check_intervalle(grille,ligne,colonne):
    n = taille_cote(grille)
    if int(ligne) < 0 or int(ligne) > n-1 or int(colonne) < 0 or int(colonne) > n-1:
        return False
    else:
        return True

# ---------------------------------------------------------
# On vérifie si la grille est vide :
# Entrée : grille, i, j
# Sortie : True(vide) ou False(plein ou mauvais intervalle)
# ---------------------------------------------------------

def est_vide(grille,ligne,colonne):
    if check_intervalle(grille,ligne,colonne) == False:
        return False
    elif grille[ligne][colonne] == " " or grille[ligne][colonne] == "":
        return True
    else:
        return False

# print(est_vide(creer_grille(5),2,2))

#-------------------------------------------
# On vérifie si le symbole rentré est valide
# Entrée : symbole
# Sortie : True ou False
#-------------------------------------------

def symbole_valide(symbole):
    if symbole == "X" or symbole == "O":
        return True
    else:
        return False

#------------------------------------------------------------------
# On écrit un symbole dans la grille
# Entrée : grille, ligne, colonne, symbole
# Sortie : False ou "grille"
# False : Si la case contient déjà un symbole
#       : Si ligne et colonne ne sont pas dans l'intervalle
#       : Si le symbole n'est pas "X" ou "O"
# grille : On retourne la grille avec le symbole si tout est validé
#-------------------------------------------------------------------

def ecrire(grille,ligne,colonne,symbole):
    if est_vide(grille,ligne,colonne) == False or symbole_valide(symbole) == False:
        return False
    else:
        grille[ligne][colonne] = symbole
        return grille

# print(ecrire(creer_grille(5),2,2,"X"))

#-----------------------------------------------------
# On efface un symbole dans un index [ligne][colonne]
# Entrée : grille, ligne, colonne
# Sortie : False ou "Impossible d'effacer"
#-----------------------------------------------------

def effacer(grille,ligne,colonne):
    if check_intervalle(grille,ligne,colonne) == True: # On verifie si l'intervalle est vrai
        grille[ligne][colonne] = "" # si intervalle vrai alors on remplace le caractère
        return grille # on retourne la nouvelle grille avec caractère supprimer
    else:
        return False


# grille = creer_grille(5)

# print(effacer(start,5,6))

#---------------------------------------------------------------------
# On vérifie si la case possède le symbole
# Entrée : grille, ligne, colonne, symbole
# Sortie : True ou False
# True : Si la case dans l'intervalle possède le symbole en paramètre
# False : Si l'intervalle ou le symbole n'est pas bon
#---------------------------------------------------------------------

def est(grille,ligne,colonne,symbole):
    if ecrire(grille,ligne,colonne,symbole) == grille:
        return True
    elif check_intervalle(grille,ligne,colonne) == False or symbole_valide(symbole) == False:
        return False

#-----------------------------------------
# On affiche la grille complète
# Entrée : grille
# Sortie : grille affichée en texte
#-----------------------------------------


def afficher(grille):
    n = taille_cote(grille)
    for ligne in range(n):  
        for colonne in range(n):
            if grille[ligne][colonne] == "":
                print(" ", end="")            
            print(" " + grille[ligne][colonne] + " ", end="")
            if colonne < n-1:
                print("|", end="")
            # if colonne == n-2:
            
        if ligne < n-1:
            print("\n" + n * "---" + (n-1) * "-")
    print("")
        
    return grille

################################################################
# On demande la taille de grille (init du jeu)
# Entrée : void
# Sortie : start() si valeur incorrect ou creer_grille(n) si ok
################################################################
def start():
    n = int(input('Entrez la taille de la grille : '))
    if n < 3:
        print("Veuillez entrer un nombre supérieur à 3")
        return start()
    return creer_grille(n)

#################################################################
# On demande si le joueur veut continuer
# Entrée : Void
# Sortie : True si oui, False si non, continuer() si incorrect
#################################################################


def continuer():
    keepcont = str(input("On continue ? [O]ui ou [N]on : "))
    if keepcont == "O" or keepcont == "o":
        return True
    if keepcont == "N" or keepcont == "n":
        print("La partie est finie")
        return False
    else:
        print("Valeur incorrect")
        return continuer()

############################################
# On cherche a qui est le tour
# Entrée : compteur
# Sortie : Print() le tour du joueur
############################################

def joueur(compteur):
    x = "X"
    o = "O"
    if compteur % 2 == 0:
        return x        
    else:
        return o

def afficher_joueur(compteur):
    print("C'est au tour de joueur", joueur(compteur))


###########################################################################################################
# On demande les coordonnées                                                                           ####
# Entrée : compteur, grille                                                                            ####
# Sortie : si valeur incorrect on redemande les coordonnées, sinon on retourne un tuple de coordonnées ####
###########################################################################################################

def in_void(char,compteur,grille):
    if char == "":
        return tour(compteur,grille)
    else:
        return True

def in_espace(char):
    if char == " ":
        return True
    else:
        return False

def in_number(char):
    if char >= "0" and char <= "9":
        return True
    else:
        return False
    
def in_sign(char):
    if char == "+" or char == "-":
        return True
    else:
        return False

def in_something(char):
    if char != " " :
        return True
    else:
        return False

# On cherche si l'espace est valide ou non

def valid_space(char):
    char_before = 0
    space_between = 0
    char_after = 0
    for i in range(len(char)):
        if in_something(char[i]) == True and char_before == 0:
            char_before += 1
        elif char_before + space_between == 1 and in_espace(char[i]):
            space_between += 1
        elif char_before + space_between + char_after == 2 and in_something(char[i]):
            char_after += 1
    if char_before + space_between + char_after == 3:
        return False
    else:
        return True

# On cherche si le signe est valide ou non

def valid_sign(char):
    sign = 0
    number = 0
    for i in range(len(char)):
        if in_sign(char[i]) == True and number > 0 and sign == 0:
            return False
        elif in_sign(char[i]) == True and number == 0:
            sign += 1
        elif in_number(char[i]) == True:
            number += 1
    if sign > 1:
        return False
    else:
        return True

def valid_int(char):
    number = 0
    for i in range(len(char)):
        if in_number(char[i]) == True:
            number += 1
    if valid_sign(char) == False:
        return False
    if number == 0:
        return False
    if valid_space(char) == False:
        return False
    else:
        return True

def string_to_int(char):
    char = int(char)
    return char

def line_check(compteur,grille):
    in_line_true = False
    while (not in_line_true):
        in_line = input("Entrez le numéro de la ligne (appuyez sur entrée pour annuler la saisie : ")
        if in_void(in_line,compteur,grille) == True:
            if valid_int(in_line) == True:
                in_line = string_to_int(in_line)
                return in_line
            elif valid_int(in_line) == False:
                print("Il faut saisir un entier")
                return line_check(compteur,grille)

def column_check(compteur,grille):
    in_column_true = False
    while (not in_column_true):
        in_column = input("Entrez le numéro de la colonne (appuyez sur entrée pour annuler la saisie : ")
        if in_void(in_column,compteur,grille) == True:
            if valid_int(in_column) == True:
                in_column = string_to_int(in_column)
                return in_column
            elif valid_int(in_column) == False:
                print("Il faut saisir un entier")
                return column_check(compteur,grille)

def demande_coord(compteur,grille):
    n = taille_cote(grille)
    line = line_check(compteur,grille)
    column = column_check(compteur,grille)
    return line,column                          # Le return appelle les fonctions des coordonnées

############################################################################################################
# On compte le nombre de tour
# Entrée : compteur, grille
# Sortie : return tour pour passer au tour suivant, fin si on souhaite pas continuer
############################################################################################################

def tour(compteur,grille):
    if continuer():
        afficher_joueur(compteur)
        tuple_coord = demande_coord(compteur,grille)
        ligne = int(tuple_coord[0])
        colonne = int(tuple_coord[1])
        if not est_vide(grille,ligne,colonne):
            print("La case choisie n'est pas vide")
            return tour(compteur,grille)
        else:
            ecrire(grille,ligne,colonne,joueur(compteur))
        afficher(grille)
        compteur += 1
        return tour(compteur,grille)
    else:
        print("fin")

#################################################################################
# Fonction Main
#################################################################################

def game():

    compteur = 1
    grille = start()
    tour(compteur,grille)

print(game())