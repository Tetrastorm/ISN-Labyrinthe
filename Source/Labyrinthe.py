from tkinter import *
from math import *
from random import *
from Matrix import *

#---------------------------------------------------------------------------------------------------------------
#                                                Core
#---------------------------------------------------------------------------------------------------------------

    # Affiche dans tkinter la matrice niveau {Statut : En fonctionnel / à Optimiser}

def TkAfficherMatrice():
    tkCanvas=Canvas(tkFenetre)
    tkCanvas.pack(fill=BOTH, expand=1)

    for y in range(mMatrice.GetSize()[0]):
        for x in range(mMatrice.GetSize()[1]):
            if mMatrice.GetValue([x,y]) == 0:
                case = tkCanvas.create_rectangle((x * (ilImageDimension[0]*lScale[0])), (y * (ilImageDimension[1]*lScale[1])), (x * (ilImageDimension[0]*lScale[0]) + (ilImageDimension[0]*lScale[0])), (y * (ilImageDimension[1]*lScale[1]) + (ilImageDimension[1]*lScale[1])), fill="lightgreen")
            elif mMatrice.GetValue([x, y]) == 1:
                case = tkCanvas.create_rectangle((x * (ilImageDimension[0]*lScale[0])), (y * (ilImageDimension[1]*lScale[1])), (x * (ilImageDimension[0]*lScale[0]) + (ilImageDimension[0]*lScale[0])), (y * (ilImageDimension[1]*lScale[1]) + (ilImageDimension[1]*lScale[1])), fill="black")
            mObjetMatrice.SetMatrix([x,y], case)

    cJoueur = tkCanvas.create_rectangle((lCoordJoueur[0] * (ilImageDimension[0]*lScale[0])), (lCoordJoueur[1] * (ilImageDimension[1]*lScale[1])), (lCoordJoueur[0] * (ilImageDimension[0]*lScale[0]) + (ilImageDimension[0]*lScale[0])), (lCoordJoueur[1] * (ilImageDimension[1]*lScale[1]) + (ilImageDimension[1]*lScale[1])), fill="turquoise")

#---------------------------------------------------------------------------------------------------------------
#                                           Interface Utilisateur
#---------------------------------------------------------------------------------------------------------------

    # Creer une fenetre {Statut : Fonctionnel}

def GUI():
    global tkFenetre

    tkFenetre = Tk()
    tkFenetre.title("Labyrinthe")
    tkFenetre.geometry(str(lDefaultSize[0])+"x"+str(lDefaultSize[1]))

    tkFenetre.bind('<Configure>', Resize) 

    TkMenuPrincipal()   

    tkFenetre.mainloop()

    # Créer les widgets du menus principale {Statut : Fonctionnel}

def TkMenuPrincipal():
    print("Loading : Menu Principal")
    iState = 0
    print(str(iState))

    EnleverWidget()
    
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
    print("Loading : Editeur")

    iState = 2
    print(str(iState))
    EnleverWidget()
    
    TkAfficherMatrice()

    tkEditeurButtonNouveau=Button(tkFenetre, text="Nouvelle Map")
    PositionRelative(tkFenetre, tkEditeurButtonNouveau, [0.80, 0.10])

    TkEditeurButtonPoint = Button(tkFenetre, text="Point", command= lambda:Edition(0))
    PositionRelative(tkFenetre, TkEditeurButtonPoint, [0.80, 0.33])

    TkEditeurButtonLigne = Button(tkFenetre, text="Ligne", command=lambda:Edition(1))
    PositionRelative(tkFenetre, TkEditeurButtonLigne, [0.85, 0.33])

    TkEditeurButtonRectangle = Button(tkFenetre, text="Rectangle", command=lambda:Edition(3))
    PositionRelative(tkFenetre, TkEditeurButtonRectangle, [0.90, 0.33])

    TkEditeurButtonMenu = Button(tkFenetre, text="Retourner au menu", command=lambda:TkMenuPrincipal())
    PositionRelative(tkFenetre, TkEditeurButtonMenu, [0.875, 0.90])

    EditeurEvent()

    # Créer les widgets de la partie jeu {Statut : En Developpement}

def TkJeu():
    print("Loading : Jeu")

    iState = 1

    print(str(iState))
    EnleverWidget()
    
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
        if mMatrice[lCoordJoueur[0], lCoordJoueur[1]+1] == 0:
            lCoordJoueur[lCoordJoueur[0], lCoordJoueur[1]+1]
            
    elif tkFenetre.bind("<Down>,bas"):
        if mMatrice[lCoordJoueur[0], lCoordJoueur[1]-1]==0:
            lCoordJoueur[lCoordJoueur[0], lCoordJoueur[1]-1]
            
    elif tkFenetre.bind("<Left>,gauche"):
        if mMatrice[lCoordJoueur[0]-1, lCoordJoueur[1]]==0:
            lCoordJoueur[lCoordJoueur[[0] -1, lCoordJoueur[1]]]
            
    elif tkFenetre.bind("<Right>,droite"):
        if mMatrice[lCoordJoueur[0]+1, lCoordJoueur[1]] == 0:
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

def EnleverWidget():
    lWidget = tkFenetre.winfo_children()

    for item in lWidget:
        item.destroy()

def GetCase(event):
    lTempCaseCoord = [0,0]

    lTempCaseCoord[0]= int((tkFenetre.winfo_pointerx()-tkFenetre.winfo_rootx())/(ilImageDimension[0]*lScale[0])) 
    lTempCaseCoord[1]= int((tkFenetre.winfo_pointery()-tkFenetre.winfo_rooty())/(ilImageDimension[1]*lScale[1]))
    
    if lTempCaseCoord[0] < mMatrice.GetSize()[0] and lTempCaseCoord[1] < mMatrice.GetSize()[1]:
        mCaseCoord[1][0] = mCaseCoord[0][0]
        mCaseCoord[1][1] = mCaseCoord[0][1]
        mCaseCoord[0][0] = lTempCaseCoord[0] 
        mCaseCoord[0][1] = lTempCaseCoord[1]
        
        print(str(tkFenetre.winfo_pointerx()-tkFenetre.winfo_rootx()) + ", Y = " + str(tkFenetre.winfo_pointery()-tkFenetre.winfo_rooty()))
        print(str(mCaseCoord))

def Resize(event):
    lTempScale = [0,0]
    if lDefaultSize[0] != 0 and lDefaultSize[1] != 0:
       lTempScale[0] = tkFenetre.winfo_width()/lDefaultSize[0]
       lTempScale[1] = tkFenetre.winfo_height()/lDefaultSize[1]
       
       if lTempScale != lScale:
           lScale[0] = lTempScale[0]
           lScale[1] = lTempScale[1]
            
           print("Resizing")
           print("Reloading state : " + str(iState))
           print("New scale : " + str(lScale))
        
           if iState == 0:
               TkMenuPrincipal()
           elif iState == 1:
               TkJeu()
           else:
               TkEditeur()

def Edition(arg):
    if arg == 0:
        mMatrice.SetPoint(mCaseCoord[0])
        TkEditeur()
    elif arg == 1:
        mMatrice.SetLine(mCaseCoord[0], mCaseCoord[1])
        TkEditeur()
    else:
        mMatrice.SetRectangle(mCaseCoord[0], mCaseCoord[1])
        TkEditeur()

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

def TestPoint():
    mMatrice.SetPoint(mCaseCoord[0])

    for y in range(mObjetMatrice.GetSize()[1]):
        for x in range(mObjetMatrice.GetSize()[0]):
            print("Value Objet : " + str(mObjetMatrice.GetValue([x,y])))
            mObjetMatrice.DebugDisplay()
            mObjetMatrice.GetValue([x,y]).destroy()

    TkAfficherMatrice()

#---------------------------------------------------------------------------------------------------------------
#                                             Programme principale
#---------------------------------------------------------------------------------------------------------------

global ilImageDimension, lCoordJoueur, cJoueur, mMatrice, tkCanvas, mCaseCoord, lScale, iState, lDefaultSize, mObjetMatrice

lDefaultSize = [720, 450]
lTailleMatrice = [30, 30]
lCoordJoueur=[0,0, 1]   #[0] coord X, [1] coord Y, [2] Orientation (0 = Up, 1 = Right, 2 = Down, 3 = Left)

mCaseCoord = [[0,0], [0,0]]
lScale = [1.0,1.0]
iState = 0

ilImageDimension = [15, 15]

mMatrice = Matrix(lTailleMatrice)
mObjetMatrice = Matrix(mMatrice.GetSize())

mMatrice.DebugDisplay()

GUI()