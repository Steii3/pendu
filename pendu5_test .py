
# a faire :
#   ecran de titre
#   
#   faire un pendu en ascii et le montrer


from random import randint
from time import sleep 
import os

#definition d'une fonction qui enleve tout le texte du terminal
def clear():
    '''clear console'''
    return os.system('cls')
#clear()

#definition d'une fonction qui change une chaine de caractere en liste.
def split(word):
    '''list to string'''
    return [char for char in word]
#split()

def ascii_switch(vie):
    switcher = {
        10: '''








====================
            ''',
        9: '''

   ||
   ||
   ||
   ||
   ||
   ||
  /||
 //||
====================''',
        8: '''  
  ,==========Y===
   ||       
   ||      
   ||      
   ||      
   ||       
   ||
  /||
 //||
====================''',
        7: '''
  ,==========Y===
   ||  /     
   || /     
   ||/      
   ||      
   ||       
   ||
  /||
 //||
====================''',
        6: '''  
  ,==========Y===
   ||  /      |
   || /       |
   ||/        
   ||        
   ||        
   ||
  /||
 //||
====================''',
        5: '''
  ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||        
   ||        
   ||
  /||
 //||
====================''',
        4: '''  
  ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||         |
   ||        
   ||
  /||
 //||
====================''',
        3: '''  
  ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||        /|
   ||        
   ||
  /||
 //||
====================''',
        2: '''  
  ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||        /|\\
   ||        
   ||
  /||
 //||
==================== ''',
        1: '''  
  ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||        /|\\
   ||        /
   ||
  /||
 //||
====================''',
        0: '''  
  ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||        /|\\
   ||        / \\
   ||
  /||
 //||
====================''' 

    }
    return switcher.get(vie,"erreur dans la saisie de la fonction de switch ascii")

#declaration variable
mot_liste = ["novice", "dejeuner", "nouilles", "filtre", "cosmetique", "jouer", "augmenter",
             "honorer", "joue", "acheter", "vendre", "mort", "poivre", "mouchoir", "engrenage", "pizza"]
mot = ""
lettre = ""
lettre_utilisé = []
mot_caché = ""
vie = 10
bool = True


clear()

#choix entre mot tapé par utilisateur et mot aléatoire
while bool:
    try: #empeche l'utilisateur de mettre autre chose que un nombre
        i = int(input("voulez vous entrer le mot vous même , ou utiliser un mot aleatoire ?\nTaper 1 ou 2\n(1) entrer mot\n(2) utiliser liste.\n"))
    except ValueError:
        clear()
        print("la valeur saisie n'est pas valide, entrez un nombre")
        
        continue
    

    
    #choix entre mot tapé par utilisateur et mot aléatoire
    if i == 1:
        mot = input("entrer le mot : ")
        mot = mot.lower()
        bool = False
    elif i == 2:
        # choisit un mot aleatoire de la liste 'mot_liste'
        mot = mot_liste[randint(0, len(mot_liste)-1)]
        bool = False
    else:
        #empeche l'utilisateur de mettre autre chose que 1 ou 2
        clear()
        print("la valeur saisie n'est pas valide, entrer soit 1 soit 2")
    
        
#met le nombre de "_" correspondant au lettres du mot dans mot_caché
for n in range(len(mot)):
    mot_caché = mot_caché + "_"

#convertir mot et mot_caché en liste de lettre
mot = split(mot)
mot_caché = split(mot_caché)



clear()
#boucle principale jeu
while vie != 0:
    bool = True
    while bool:
        bool = False
        print(ascii_switch(vie))
        print("vie restante: {0}".format(vie))
        print("lettre utilisé: {0}".format(" , ".join(lettre_utilisé)))
        print("mot caché : {0}".format("".join(mot_caché)))
        lettre = input("entrer lettre a chercher : ")
        lettre = lettre.lower()

        clear()

        if len(lettre_utilisé) != 0: #regarde si la longeur de lettre n'est pas égal a zero et si 
            for i in range(len(lettre_utilisé)):
            # demande de choisir une autre lettre si la lettre est deja utilisé
                if lettre == lettre_utilisé[i] or len(lettre) > 1:
                    
                    print("la lettre est déja utilisé ou la saisie fait plus d'un caractère, recommencer")
                    bool = True
                    break
        elif len(lettre) > 1:         
            bool = True
            print("la lettre fait plus d'un caractere, réessayer")            

            
    #chercher si lettre est dans le mot
    
    trouvé = False
    for i in range(len(mot)):

        if lettre == mot[i]:
                mot_caché[i] = mot[i]
                trouvé = True

#regarder si on doit enlever une vie ou pas
    if trouvé == False:
        vie -= 1

#regarder si le joueur a gagné le jeu
    lettre_utilisé.append(lettre)
    bool = True
    for i in range(len(mot_caché)):  # regarde si tout les lettre de mot_caché ont été révélé
        if mot_caché[i] == "_":
            bool = False
    if bool == True:  # si toutes lettre de mot_caché sont découvert alors fait gagné
        clear()
        input("bien joué tu as gagné\nle mot était {0}".format(("".join(mot))))
        exit()
        

#si vie = 0 met message de perdant
clear()
print(ascii_switch(vie))
print("vous avez perdu\nle mot était {0}".format(("".join(mot))))

