

from random import randint
import os 

#definition d'une fonction qui enleve tout le texte du terminal
clear = lambda: os.system('cls')
#clear()

#definition d'une fonction qui change une chaine de caractere en liste.
def split(word): 
    return [char for char in word]  
#split()


#declaration variable
mot_liste = ["novice","dejeuner","nouilles","filtre","cosmetique","jouer","augmenter","honorer","joue","acheter","vendre","mort","poivre","mouchoir","engrenage","pizza"]
mot = "" 
lettre = ""
lettre_utilisé = []
mot_caché = ""
vie = 10

#choix entre mot tapé par utilisateur et mot aléatoire
i = int(input("voulez vous entrer le mot vous même , ou utiliser un mot aleatoire ?\nTaper 1 ou 2\n(1) entrer mot\n(2) utiliser liste.\n"))

#choix entre mot tapé par utilisateur et mot aléatoire
if i == 1 : 
    mot = input("entrer le mot : ")
    mot = mot.lower()
elif i == 2 :
    mot = mot_liste[randint(0,len(mot_liste))] #choisit un mot aleatoire de la liste 'mot_liste'

#met le nombre de "_" correspondant au lettres du mot dans mot_caché 
for n in range(len(mot)):
    mot_caché = mot_caché + "_"

#convertir mot et mot_caché en liste de lettre
mot = split(mot)
mot_caché = split(mot_caché)

#boucle principale jeu
while vie != 0:
    clear()
    print("vie restante: {0}".format(vie))
    print("lettre utilisé: {0}".format(" , ".join(lettre_utilisé)))
    print("mot caché : {0}".format("".join(mot_caché)))
    lettre = input("entrer lettre a chercher : ")
    lettre = lettre.lower()
    bool = True
    #boucle tant que l'utilisateur entre une lettre deja utilisé
    while bool :
        lettre_correct = True
        if len(lettre_utilisé) == 0: #regarde si la liste des lettre n'est pas vide et si vrai ne continue pas
            break
        
        for i in range(len(lettre_utilisé)): #regarde si la lettre tapé est dans la liste lettre_utilisé et si vrai demande de mettre une autre lettre
            if lettre == lettre_utilisé[i]:
                clear()
                print("vie restante: {0}".format(vie))
                print("lettre utilisé: {0}".format(" , ".join(lettre_utilisé)))
                print("mot caché : {0}".format("".join(mot_caché)))
                print("la lettre est déja utilisé, recommencer")
                lettre = input("entrer lettre a chercher : ")
                lettre = lettre.lower()
                lettre_correct = False
                break
        if lettre_correct == True: # si la lettre saisie est valide, arreter la boucle
            bool = False
                
                

#chercher si lettre est dans le mot
    trouvé = False
    for i in range(len(mot)):
        
        if lettre == mot[i] :
                mot_caché[i] = mot[i]
                trouvé = True
        
#regarder si on doit enlever une vie ou pas
    if trouvé == False:
        vie-= 1

#regarder si le joueur a gagné le jeu
    lettre_utilisé.append(lettre)
    bool = True
    for i in range(len(mot_caché)): # regarde si tout les lettre de mot_caché ont été révélé
        if mot_caché[i] == "_":
            bool = False
    if bool == True:#si toutes lettre de mot_caché sont découvert alors fait gagné
        clear()
        input("bien joué tu as gagné\nle mot était {0}".format(("".join(mot))))
        exit()
    
#message de défaite si vie = 0
clear()
print("vous avez perdu\nle mot était {0}".format(("".join(mot))))


