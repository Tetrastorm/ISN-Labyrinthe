from tkinter import *
from math import *

#---------------------------------------------------------------------------------------------------------------
#                                                Core
#---------------------------------------------------------------------------------------------------------------

    # Fonction de creation de la Matrice de la taille souhaite {Statut : Fonctionnel}

def InitMatrice(TailleMatrice):
    Matrice = [[0], [0]]
    
    for y in range(TailleMatrice[1]):
        Matrice.append([0])
        for x in range(TailleMatrice[0]):
            Matrice[y].append(0)

    return Matrice

    # Affiche dans tkinter la matrice niveau {Statut : En Developpement}

def TkAfficherMatriceEditeur(tkFenetre, iaMatrice):
    imgMur = PhotoImage(file="MurTexture.gif")
    imgJoueur = PhotoImage(file="PlayerTexture.gif")
    imgSol = PhotoImage(file="NavTexture.gif")

    ilImageDimension = [25, 25]

    tkCanvas = Canvas(tkFenetre)

    AfficherMatrice(iaMatrice, 10)

    for y in range(10):
        for x in range(10):
            print("Affichage : " + str(x) + ", " + str(y))
            print(iaMatrice[x][y])

            if iaMatrice[x][y] == 0:
                img = tkCanvas.create_image(x * (ilImageDimension[0]/2) + 12.5, y * (ilImageDimension[1]/2) + 12.5, image=imgSol)
            elif iaMatrice[x][y] == 1:
                img = tkCanvas.create_image(x * (ilImageDimension[0]/2) + 12.5, y * (ilImageDimension[1]/2) + 12.5, image=imgMur)

#---------------------------------------------------------------------------------------------------------------
#                                           Interface Utilisateur
#---------------------------------------------------------------------------------------------------------------

    # Creer une fenetre {Statut : Fonctionnel}

def GUI(iaMatrice):
    tkFenetre = Tk()
    tkFenetre.title("Labyrinth")
    tkFenetre.geometry("1280x720")
    
    TkMenuPrincipale(tkFenetre, iaMatrice)    

    tkFenetre.mainloop()
        

    # Créer les widgets du menus principale {Statut : Fonctionnel}

def TkMenuPrincipale(tkFenetre, iaMatrice):
    tkMenuLabel = Label(tkFenetre, text="Labyrinth")
    PositionRelative(tkFenetre, tkMenuLabel, [0.5, 0.25])

    tkMenuButtonJouer = Button(tkFenetre, text="Jouer", command=lambda:TkJeu(tkFenetre, iaMatrice))
    PositionRelative(tkFenetre, tkMenuButtonJouer, [0.5, 0.5])

    tkMenuButtonCreer = Button(tkFenetre, text="Créer", command=lambda:TkEditeur(tkFenetre))
    PositionRelative(tkFenetre, tkMenuButtonCreer, [0.5, 0.625])

    tkMenuButtonQuitter = Button(tkFenetre, text="Quitter", command=tkFenetre.destroy)
    PositionRelative(tkFenetre, tkMenuButtonQuitter, [0.5, 0.75])

    # Créer les widgets de l'editeur de niveau {Statut : En Developpement}

def TkEditeur(tkFenetre):
    tkEditeurButtonNouveau=Button(tkFenetre, text="Nouvelle Map")
    PositionRelative(tkFenetre, tkEditeurButtonNouveau, [0.80, 0.10])

    # Créer les widgets de la partie jeu {Statut : En Developpement}

def TkJeu(tkFenetre, iaMatrice):
    TkAfficherMatriceEditeur(tkFenetre, iaMatrice)

#---------------------------------------------------------------------------------------------------------------
#                                                 Gameplay
#---------------------------------------------------------------------------------------------------------------

    # Gère les déplacemnts du joueur {Statut : En Developpement}

def Deplacement(event, fenetre, coordJoueur, Matrix): 
    fichierimage=Photoimage(file="Image JPEG")                     # Attention les canvas Tkinter prennent par defaut que le gif, si on prend des jpg il faut passer par le lib PIP
    if fenetre.bind("<Up>,haut"):
        if matrice[coordJoueur[0], coordJoueur[1]+1] == 0:
            imgi=can.create_image(coordJoueur[0],coordJoueur[1])
            coordJoueur[coordJoueur[0],coordJoueur[1]+1]
            
    elif fenetre.bind("<Down>,bas"):
        if matrice[coordJoueur[0], coordJoueur[1]-1]==0:
            imgi=can.create_image(coordJoueur[0],coordJoueur[1])
            coordJoueur[coordJoueur[0],coordJoueur[1]-1]
            
    elif fenetre.bind("<Left>,gauche"):
        if matrice[coordJoueur[0]-1, coordJoueur[1]]==0:
            imgi=can.create_image(coordJoueur[0],coordJoueur[1])
            coordJoueur[coordJoueur[[0] -1, coordJoueur[1]]]
            
    elif fenetre.bind("<Right>,droite"):
        if matrice[coordJoueur[0]+1, coordJoueur[1]] == 0:
            imgi=can.create_image(coordJoueur[0],coordJoueur[1])
            coordJoueur[coordJoueur[[0] +1, coordJoueur[1]]]

#---------------------------------------------------------------------------------------------------------------
#                                                 Outils
#---------------------------------------------------------------------------------------------------------------

    # Affiche la matrice dans la console (outil de Debbuging) {Statut : Fonctionnel}

def AfficherMatrice(Matrice, YMax = 0):
    for i in range(YMax):
        print(Matrice[(YMax - 1) - i])

    # Creer un Point dans la matrice {Statut : Fonctionnel}

def Point(Matrice, Coord, EstAdditif = True):
    if EstAdditif:
        Matrice[Coord[1]][Coord[0]] = 1
    else:
        Matrice[Coord[1]][Coord[0]] = 0

    # Creer une ligne dans la matris {Statut : Fonctionnel}

def Ligne(Matrice, CoordA, CoordB, EstAdditif = True):
    TempCoord = [0,0]

    if CoordA[0] == CoordB[0]:
        TempCoord[0] = CoordA[0]

        if CoordA[1] > CoordB[1]:
            for i in range(CoordB[1], (CoordA[1] + 1)):
                TempCoord[1] = i
                Point(Matrice, TempCoord, EstAdditif)
        else:
            for i in range(CoordA[1], (CoordB[1] + 1)):
                TempCoord[1] = i
                Point(Matrice, TempCoord, EstAdditif)

    elif CoordA[1] == CoordB[1]:
        TempCoord[1] = CoordA[1]

        if CoordA[0] > CoordB[0]:
            for i in range(CoordB[0], (CoordA[0] + 1)):
                TempCoord[0] = i
                Point(Matrice, TempCoord, EstAdditif)
        else:
            for i in range(CoordA[0], (CoordB[0] + 1)):
                TempCoord[0] = i
                Point(Matrice, TempCoord, EstAdditif)
    else:
        print("Erreur : La Ligne n'est pas verticale ou horizontale")

    # Creer un Reactangle {Statut : Fonctionnel}
    
def Rectangle(Matrice, CoordA, CoordB, EstAdditif = True):
    TempCoord = [0,0]

    TempCoord = [CoordA[0], CoordB[1]]
    Ligne(Matrice, CoordA, TempCoord, EstAdditif)
    Ligne(Matrice, CoordB, TempCoord, EstAdditif)

    TempCoord = [CoordB[0], CoordA[1]]
    Ligne(Matrice, CoordA, TempCoord, EstAdditif)
    Ligne(Matrice, TempCoord, CoordB, EstAdditif)

    # Permet de placer un Widget en relatif {Statut : Fonctionnel}

def PositionRelative(fenetre, widget, coordRelative = [0.5,0.5]):
    fenetre.update()
    Coord = [fenetre.winfo_width() * coordRelative[0], fenetre.winfo_height() * coordRelative[1]]

    widget.place(x = Coord[0], y = Coord[1])

#---------------------------------------------------------------------------------------------------------------
#                                           Prototype de Technologie (cadeau alyona)
#---------------------------------------------------------------------------------------------------------------

# Generation de niveau aleatoirement {Statut : En Developpemnt}

def RandomLevelGeneration():                  # J'ai remis le code de la fonction Test()
    for i in range(x):
        for j in range(y):
            iop=randint(1,10)
            if iop==1:
                matrice[i][j]=1
            else:
                matrice[i][j]=0

#---------------------------------------------------------------------------------------------------------------
#                                             Programme principale
#---------------------------------------------------------------------------------------------------------------

ilTailleMatrice = [10,10]
ilCoordJoueur=[0,0]

    # Variable de Test

ilCoord = [0,0]

ilCoordA = [2,2]
ilCoordB = [2,5]

ilCoordC = [4,1]
ilCoordD = [8,1]

ilCoordE = [5,8]
ilCoordF = [9,3]

    # Fonction en cours de test

iaMatrice = InitMatrice(ilTailleMatrice)

Point(iaMatrice, ilCoord)

Ligne(iaMatrice, ilCoordA, ilCoordB)
Ligne(iaMatrice, ilCoordC, ilCoordD)

Rectangle(iaMatrice, ilCoordE, ilCoordF)

AfficherMatrice(iaMatrice, ilTailleMatrice[1])

GUI(iaMatrice)
