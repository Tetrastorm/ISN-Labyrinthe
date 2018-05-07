from tkinter import *
from math import *
from random import *
from Matrix import *

#---------------------------------------------------------------------------------------------------------------
#                                                Core
#---------------------------------------------------------------------------------------------------------------

    # Affiche dans tkinter la matrice niveau {Statut : En fonctionnel / à Optimiser}

def TkAfficherMatriceEditeur():    
    tkCanvas=Canvas(tkFenetre)
    tkCanvas.pack(fill=BOTH, expand=1)

    for y in range(ilTailleMatrice[1]):
        for x in range(ilTailleMatrice[1]):
            if iaMatrice[x][y] == 0:
                case = tkCanvas.create_rectangle((x * ilImageDimension[0]), (y * ilImageDimension[1]), (x * ilImageDimension[0] + ilImageDimension[0]), (y * ilImageDimension[1] + ilImageDimension[1]), fill="lightgreen")
            elif iaMatrice[x][y] == 1:
                case = tkCanvas.create_rectangle((x * ilImageDimension[0]), (y * ilImageDimension[1]), (x * ilImageDimension[0] + ilImageDimension[0]), (y * ilImageDimension[1] + ilImageDimension[1]), fill="black")
    
    cJoueur = tkCanvas.create_rectangle((ilCoordJoueur[0] * ilImageDimension[0]), (ilCoordJoueur[1] * ilImageDimension[1]), (ilCoordJoueur[0] * ilImageDimension[0] + ilImageDimension[0]), (ilCoordJoueur[1] * ilImageDimension[1] + ilImageDimension[1]), fill="turquoise")

#---------------------------------------------------------------------------------------------------------------
#                                           Interface Utilisateur
#---------------------------------------------------------------------------------------------------------------

    # Creer une fenetre {Statut : Fonctionnel}

def GUI():
    global tkFenetre
    tkFenetre = Tk()
    tkFenetre.title("Labyrinthe")
    tkFenetre.geometry("720x450")

    TkMenuPrincipale()    

    tkFenetre.mainloop()
        

    # Créer les widgets du menus principale {Statut : Fonctionnel}

def TkMenuPrincipale():
    EnleverWidget(tkFenetre)
    
    tkMenuLabel = Label(tkFenetre, text="Labyrinthe")
    PositionRelative(tkFenetre, tkMenuLabel, [0.5, 0.25])

    tkMenuButtonJouer = Button(tkFenetre, text="Jouer", command=lambda:TkJeu())
    PositionRelative(tkFenetre, tkMenuButtonJouer, [0.5, 0.45])

    tkMenuButtonCreer = Button(tkFenetre, text="Créer", command=lambda:TkEditeur())
    PositionRelative(tkFenetre, tkMenuButtonCreer, [0.5, 0.55])

    tkMenuButtonQuitter = Button(tkFenetre, text="Quitter", command=tkFenetre.destroy)
    PositionRelative(tkFenetre, tkMenuButtonQuitter, [0.5, 0.65])

    # Créer les widgets de l'editeur de niveau {Statut : En Developpement}

def TkEditeur():
    EnleverWidget(tkFenetre)
    
    TkAfficherMatriceEditeur()

    tkEditeurButtonNouveau=Button(tkFenetre, text="Nouvelle Map")
    PositionRelative(tkFenetre, tkEditeurButtonNouveau, [0.80, 0.10])

    TkEditeurButtonPoint = Button(tkFenetre, text="Point", command=lambda:Selection(0))
    PositionRelative(tkFenetre, TkEditeurButtonPoint, [0.80, 0.33])

    TkEditeurButtonLigne = Button(tkFenetre, text="Ligne", command = lambda:Selection(1))
    PositionRelative(tkFenetre, TkEditeurButtonLigne, [0.85, 0.33])

    TkEditeurButtonRectangle = Button(tkFenetre, text="Rectangle", command=lambda:Selection(2))
    PositionRelative(tkFenetre, TkEditeurButtonRectangle, [0.90, 0.33])

    TkEditeurButtonMenu = Button(tkFenetre, text="Retourner au menu", command=lambda:TkMenuPrincipale())
    PositionRelative(tkFenetre, TkEditeurButtonMenu, [0.875, 0.90])

    # Créer les widgets de la partie jeu {Statut : En Developpement}

def TkJeu():
    EnleverWidget(tkFenetre)
    TkAfficherMatriceEditeur()
    TkJeuButtonMenu = Button(tkFenetre, text="Retourner au menu", command=lambda:TkMenuPrincipale())
    PositionRelative(tkFenetre, TkJeuButtonMenu, [0.90, 0.90])

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

    # Permet de placer un Widget en relatif {Statut : Fonctionnel}

def PositionRelative(fenetre, widget, coordRelative = [0.5,0.5]):
    fenetre.update()
    Coord = [fenetre.winfo_width() * coordRelative[0], fenetre.winfo_height() * coordRelative[1]]

    widget.place(x = Coord[0], y = Coord[1])

   # Permet de supprimer tout le widget de la fenetre {Statut : Fonctionnel}

def EnleverWidget(tkFenetre):
    lWidget =tkFenetre.winfo_children()

    for item in lWidget:
        item.destroy()
    #Permet de selectionner un ase de la matrice dans l'éditeur Tkinter

def Selection(Type = 0):
    CoordA = [0, 0]
    CoordB = [0, 0]

    CoordA = tkFenetre.bind('<Button 1>', GetMouseCoord)
    print("Mouse : x = " + str(CoordA[0]) + " y = " + str(CoordB[1]))
    
    if Type == 0:    
        Point(CoordA)
    else:
        CoordB = tkFenetre.bind('<Button 1>', GetMouseCoord)
        print("Mouse : x = " + str(CoordB[0]) + " y = " + str(CoordB[1]))

        if Type == 1:
            Ligne(CoordA, CoordB)
        else:
            Rectangle(CoordA, CoordB)

def GetMouseCoord(event):
    MouseCoord[0]=tkFenetre.winfo_pointerx()
    MouseCoord[1]=tkFenetre.winfo_pointery()
    
    return MouseCoord

#---------------------------------------------------------------------------------------------------------------
#                                           Le Laboratoire
#---------------------------------------------------------------------------------------------------------------

# Generation de niveau aleatoirement {Statut : En Developpemnt}

def RandomLevelGeneration():
    x = int(input("Largeur:  "))  
    y = int(input("Hauteur:  "))       
    labyrinthe = generer(x, y)                 
 
    listelignes = []                           
    while len(labyrinthe) != 0:                 
        ligne = []                              
        for i in range (0,x):
            ligne.append(labyrinthe[0])         
            labyrinthe.pop(0)
        listeLignes.append(ligne)
    print(listelignes)                

def Generer(x, y):
    base= []                          
    for i in range(0, x * y):               
        rand = randint(0, 2)
        if rand==0:
            valeurcase=1
        else:
            valeurcase=0
        base.append(valeurcase)              
    return base

def AI_Perception(ActorInfo, OtherActorInfo, Range = 5):    
    if sqrt((OtherActorInfo[0] - ActorInfo[0])^2, (OtherActorInfo[1] - ActorInfo[1])^2) <= Range:
        ActorDistance = sqrt((ActorInfo[0])^2, (ActorInfo[1])^2)
        OtherActorDistance = sqrt((OtherActorInfo[0])^2, (OtherActorInfo[1] - 0)^2)

        if ActorInfo[2] == 0:   #x = 0, y = -1
            return 0
        elif ActorInfo[2] == 1: #x = 1, y = 0
            return 0
        elif ActorInfo[2] == 2: #x = 0, y = 1
            return 0
        else:                   #x = -1, y = 0
            return 0

#---------------------------------------------------------------------------------------------------------------
#                                             Programme principale
#---------------------------------------------------------------------------------------------------------------

global ilImageDimension, ilTailleMatrice, ilCoordJoueur, cJoueur, iaMatrice, tkCanvas, MouseCoord

ilTailleMatrice = [30, 30]
ilCoordJoueur=[0,0, 1]          #[0] coord X, [1] coord Y, [2] Orientation (0 = Up, 1 = Right, 2 = Down, 3 = Left)

ilImageDimension = [15, 15]

    # Variable de Test

ilCoord = [0,0]

ilCoordA = [2,2]
ilCoordB = [2,5]

ilCoordC = [4,1]
ilCoordD = [8,1]

ilCoordE = [5,8]
ilCoordF = [9,3]

    # Fonction en cours de test

iaMatrice = Matrix(ilTailleMatrice)

iaMatrice.SetPoint(ilCoord)

iaMatrice.SetLine(ilCoordA, ilCoordB)
iaMatrice.SetLine(ilCoordC, ilCoordD)

iaMatrice.SetRectangle(ilCoordE, ilCoordF)

iaMatrice.DebugDisplay()

GUI()