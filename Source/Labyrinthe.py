from tkinter import *
from math import *
from random import *
from Matrix import *

global ilImageDimension, lCoordJoueur, cJoueur, iaMatrice, tkCanvas, lCaseCoord, scale, state, defaultSize

#---------------------------------------------------------------------------------------------------------------
#                                                Core
#---------------------------------------------------------------------------------------------------------------

    # Affiche dans tkinter la matrice niveau {Statut : En fonctionnel / à Optimiser}

def TkAfficherMatrice():    
    tkCanvas=Canvas(tkFenetre)
    tkCanvas.pack(fill=BOTH, expand=1)

    ObjetMatrice = Matrix(iaMatrice.GetSize())

    for y in range(iaMatrice.GetSize()[0]):
        for x in range(iaMatrice.GetSize()[1]):
            if iaMatrice.GetValue([x,y]) == 0:
                case = tkCanvas.create_rectangle((x * ilImageDimension[0]), (y * ilImageDimension[1]), (x * ilImageDimension[0] + ilImageDimension[0]), (y * ilImageDimension[1] + ilImageDimension[1]), fill="lightgreen")
            elif iaMatrice.GetValue([x, y]) == 1:
                case = tkCanvas.create_rectangle((x * ilImageDimension[0]), (y * ilImageDimension[1]), (x * ilImageDimension[0] + ilImageDimension[0]), (y * ilImageDimension[1] + ilImageDimension[1]), fill="black")
            ObjetMatrice.SetMatrix([x,y], case)

    cJoueur = tkCanvas.create_rectangle((lCoordJoueur[0] * ilImageDimension[0]), (lCoordJoueur[1] * ilImageDimension[1]), (lCoordJoueur[0] * ilImageDimension[0] + ilImageDimension[0]), (lCoordJoueur[1] * ilImageDimension[1] + ilImageDimension[1]), fill="turquoise")

#---------------------------------------------------------------------------------------------------------------
#                                           Interface Utilisateur
#---------------------------------------------------------------------------------------------------------------

    # Creer une fenetre {Statut : Fonctionnel}

def GUI():
    global tkFenetre

    tkFenetre = Tk()
    tkFenetre.title("Labyrinthe")
    tkFenetre.geometry(str(defaultSize[0])+"x"+str(defaultSize[1]))

    tkFenetre.bind('<Configure>', Resize) 

    TkMenuPrincipal()   

    tkFenetre.mainloop()

    # Créer les widgets du menus principale {Statut : Fonctionnel}

def TkMenuPrincipal():
    print("Menu Principale")

    state = 0
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
    print("Editeur")

    state = 2
    EnleverWidget(tkFenetre)
    
    TkAfficherMatrice()

    tkEditeurButtonNouveau=Button(tkFenetre, text="Nouvelle Map")
    PositionRelative(tkFenetre, tkEditeurButtonNouveau, [0.80, 0.10])

    TkEditeurButtonPoint = Button(tkFenetre, text="Point", command= lambda:iaMatrice.SetPoint(lCaseCoord[0]) and TkAfficherMatrice())
    PositionRelative(tkFenetre, TkEditeurButtonPoint, [0.80, 0.33])

    TkEditeurButtonLigne = Button(tkFenetre, text="Ligne", command=lambda:iaMatrice.SetLine(lCaseCoord[0], lCaseCoord[1]) and TkAfficherMatrice())
    PositionRelative(tkFenetre, TkEditeurButtonLigne, [0.85, 0.33])

    TkEditeurButtonRectangle = Button(tkFenetre, text="Rectangle", command=lambda:iaMatrice.SetRectangle(lCaseCoord[0], lCaseCoord[1]) and TkAfficherMatrice())
    PositionRelative(tkFenetre, TkEditeurButtonRectangle, [0.90, 0.33])

    TkEditeurButtonMenu = Button(tkFenetre, text="Retourner au menu", command=lambda:TkMenuPrincipal())
    PositionRelative(tkFenetre, TkEditeurButtonMenu, [0.875, 0.90])

    EditeurEvent()

    # Créer les widgets de la partie jeu {Statut : En Developpement}

def TkJeu():
    state = 1
    EnleverWidget(tkFenetre)
    
    TkAfficherMatrice()
    TkJeuButtonMenu = Button(tkFenetre, text="Retourner au menu", command=lambda:TkMenuPrincipal())
    PositionRelative(tkFenetre, TkJeuButtonMenu, [0.90, 0.90])

#---------------------------------------------------------------------------------------------------------------
#                                                Editeur
#---------------------------------------------------------------------------------------------------------------

def EditeurEvent():
    tkFenetre.bind('<Button-1>', GetCase)

#---------------------------------------------------------------------------------------------------------------
#                                                 Jeu
#---------------------------------------------------------------------------------------------------------------

    # Gère les déplacemnts du joueur {Statut : En Developpement}

def Deplacement(event): 
    if tkFenetre.bind("<Up>,haut"):
        if iaMatrice[coordJoueur[0], coordJoueur[1]+1] == 0:
            lCoordJoueur[lCoordJoueur[0], lCoordJoueur[1]+1]
            
    elif tkFenetre.bind("<Down>,bas"):
        if iaMatrice[coordJoueur[0], coordJoueur[1]-1]==0:
            lCoordJoueur[lCoordJoueur[0], lCoordJoueur[1]-1]
            
    elif tkFenetre.bind("<Left>,gauche"):
        if iaMatrice[lCoordJoueur[0]-1, lCoordJoueur[1]]==0:
            lCoordJoueur[lCoordJoueur[[0] -1, lCoordJoueur[1]]]
            
    elif tkFenetre.bind("<Right>,droite"):
        if iaMatrice[lCoordJoueur[0]+1, lCoordJoueur[1]] == 0:
            lCoordJoueur[lCoordJoueur[[0] +1, lCoordJoueur[1]]]

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

def GetCase(event):
    lCaseCoord[1][0] = lCaseCoord[0][0]
    lCaseCoord[1][1] = lCaseCoord[0][1]
    lCaseCoord[0][0]= int((tkFenetre.winfo_pointerx()*scale[0])/(2*ilImageDimension[0])) 
    lCaseCoord[0][1]= int((tkFenetre.winfo_pointery()*scale[1])/(2*ilImageDimension[1]))

    print(str(lCaseCoord))

def Resize(event):
    print("Configure")

    tempScale = [0,0]
    if defaultSize[0] != 0 and defaultSize[1] != 0:
       tempScale[0] = tkFenetre.winfo_width()/defaultSize[0]
       tempScale[1] = tkFenetre.winfo_height()/defaultSize[1]

    print("state : " + str(state))
    print("TempScale : " + str(tempScale))
    print("scale : " + str(scale))

    if tempScale != scale:
        # infinite loop hazard
        if state == 0:
            TkMenuPrincipal()
        elif state == 1:
            TkJeu()
        else:
            TkEditeur()

        scale = tempScale

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

defaultSize = [720, 450]
lTailleMatrice = [30, 30]
lCoordJoueur=[0,0, 1]   #[0] coord X, [1] coord Y, [2] Orientation (0 = Up, 1 = Right, 2 = Down, 3 = Left)

lCaseCoord = [[0,0], [0,0]]
scale = [1.0,1.0]
state = 0

ilImageDimension = [15, 15]

    # Variable de Test

lCoord = [0,0]

lCoordA = [2,2]
lCoordB = [2,5]

lCoordC = [4,1]
lCoordD = [8,1]

lCoordE = [5,8]
lCoordF = [9,3]

    # Fonction en cours de test

iaMatrice = Matrix(lTailleMatrice)

iaMatrice.SetPoint(lCoord)

iaMatrice.SetLine(lCoordA, lCoordB)
iaMatrice.SetLine(lCoordC, lCoordD)

iaMatrice.SetRectangle(lCoordE, lCoordF)

iaMatrice.DebugDisplay()

GUI()