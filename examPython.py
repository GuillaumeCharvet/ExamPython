from colorama import init
init()
from colorama import Fore, Back, Style

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

# Renvoie une liste des lettres présentes dans le mot, sans répétition et dans leur ordre d'apparence
def liste_lettres(mot):
    liste = 6 * [""]
    compteur = 0
    for i in range(0,6):
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

#
# def nombre_occurences_lettres(mot):
    # liste = liste_lettres(mot)
    # nombre_lettres_diff = len(liste)
    # occurences = nombre_lettres_diff * [0]
    # for i in range 


mot_test = ["t","o","t","o","r","o"]
print(lettre_dans_mot("o",mot_test))
print(lettre_dans_mot("a",mot_test))
test = liste_lettres(mot_test)
print(test)
print(indice_lettre("o",test))


# print(Fore.RED + 'some red text', end=" ")
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

input()