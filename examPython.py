from random import randint
from colorama import init
init()
from colorama import Fore, Back, Style

# Transformation d'une chaîne de caractères en liste de caractères
def chaine2liste(mot):
    liste = len(mot)*[""]
    for i in range(len(mot)):
        liste[i] = mot[i]
    return liste

# Renvoie l'indice d'apparition d'un caractère dans une liste en supposant qu'il apparaît une et une seule fois
def indice_lettre(lettre,mot):
    for i in range(0,len(mot)):
        if mot[i]== lettre:
            return i

# Détermine si un caractère est dans une liste de de caractères
def lettre_dans_mot(lettre,mot):
    trouve = False
    for i in range(0,len(mot)):
        if mot[i] == lettre:
            trouve = True
    return trouve

# Renvoie une liste des lettres présentes dans le mot, sans répétition et dans leur ordre d'apparition
def liste_lettres(mot):
    liste = len(mot) * [""]
    compteur = 0
    for i in range(0,len(mot)):
        if not(lettre_dans_mot(mot[i],liste)):
            liste[compteur] = mot[i]
            compteur += 1
        # for j in range(0,compteur+1):
            # if (mot[i] != liste[j]):
                # print(compteur)
                # liste[compteur] = mot[i]
                # compteur += 1
    liste_finale = compteur * [""]
    for i in range(0,compteur):
        liste_finale[i] = liste[i]
    return liste_finale

# Renvoie une liste correspondant au nombre d'occurences des lettres apparaissant dans mot, classées grâce à leur ordre d'apparition
def nombre_occurences_lettres(mot):
    liste = liste_lettres(mot)
    nombre_lettres_diff = len(liste)
    occurences = nombre_lettres_diff * [0]
    for i in range(0,len(mot)):
        ind = indice_lettre(mot[i],liste)
        occurences[ind] += 1
    return occurences

# Renvoie une liste comprenant le code couleur ("B","J" ou "R") des lettres du mot essai comparé au mot cible
def couleur_lettres(essai,cible):
    liste_couleur = len(cible) * [""]
    liste_cible = liste_lettres(cible)
    liste_occurences = nombre_occurences_lettres(cible)
    # On réalise un premier parcours pour vérifier les lettres correctement positionnées
    est_bien_placee = len(cible) * [False]
    for i in range(0,len(cible)):
        if essai[i] == cible[i]:
            est_bien_placee[i] = True
            liste_couleur[i] = "R"
            ind_lettre = indice_lettre(essai[i],liste_cible)
            liste_occurences[ind_lettre] -= 1
    # Les lettres bien placées sont maintenant notées en rouge dans liste_couleur,
    # leur emplacement est repérer dans est_bien_placee,
    # et le nombre d'occurences de chaque lettre a été soustrait de liste_occurences.
    #
    # On recherche maintenant pour chaque lettre non rouge si elle apparaît tout de même dans le mot,
    # si oui mais que toutes les occurences de cette lettre ont déjà été prises en compte ailleurs,
    # alors elle sera laissée en bleu. Sinon elle passera en jaune.
    for i in range(0,len(cible)):
        if not(est_bien_placee[i]):
            if lettre_dans_mot(essai[i],cible):
                ind_lettre = indice_lettre(essai[i],liste_cible)
                if liste_occurences[ind_lettre] == 0:
                    liste_couleur[i] = "B"
                else:
                    liste_couleur[i] = "J"
                    liste_occurences[ind_lettre] -= 1
            else:
                liste_couleur[i] = "B"
    return liste_couleur

# Affiche un mot avec les lettres colorees selon le code fourni "R", "B" ou "J"
def affiche_lettres_couleurs(mot,couleurs):
    for i in range(len(mot)):
        if couleurs[i] == "R":
            print(Back.RED + Fore.WHITE + mot[i], end="")
        elif couleurs[i] == "B":
            print(Back.BLUE + Fore.WHITE + mot[i], end="")
        else:
            print(Back.YELLOW + Fore.BLACK + mot[i], end="")
    print("")
    print(Style.RESET_ALL)
    return()

# Jeu principal
# Définition des mots cibles possibles :
mots_possibles = ["accord","brader","bruler","canyon","droite","fougue","genant","huitre","miasme","rototo"]
# Choix du mot parmi ceux-ci :
indice_mot_cible = randint(0,10)
mot_cible = mots_possibles[indice_mot_cible]
print(mot_cible)
l_cible = chaine2liste(mot_cible)
#print(l_cible)
print("Le jeu Motus commence !")
tour = 0
gagne = False

while not(gagne) and tour <8:
    mot_test = input("Veuillez taper le mot à tester :")
    l_test = chaine2liste(mot_test)
    l_couleur = couleur_lettres(l_test,l_cible)
    affiche_lettres_couleurs(l_test,l_couleur)
    if len(mot_cible)*["R"] == l_couleur:
        print("Félicitation, vous avez gagné !")
        gagne = True
    else:   
        print("Bien tenté, mais non..")
        tour += 1

# mot1 = "totoro"
# print(chaine2liste(mot1))

# mot_cible = ["b","o","t","r","o","n"]
# mot_test = ["t","o","t","o","r","o"]
# print(lettre_dans_mot("o",mot_test))
# print(lettre_dans_mot("a",mot_test))
# test = liste_lettres(mot_test)
# print(test)
# print(indice_lettre("o",test))
# print(nombre_occurences_lettres(mot_test))
# print(couleur_lettres(mot_test,mot_cible))

# affiche_lettres_couleurs(mot_test,couleur_lettres(mot_test,mot_cible))

# print(6*["R"] == couleur_lettres(mot_cible,mot_cible))



# print(Fore.RED + 'some red text', end=" ")
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

input()