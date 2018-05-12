from tkinter import *
from math import *
from random import *
import matplotlib
import matplotlib.pyplot as plt
from random import *
from Matrix import *

global ilImageDimension, lCoordJoueur, cJoueur, mMatrice, tkCanvas, mCaseCoord, lScale, lDefaultSize, iState, bCheckResult

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
    print("Menu Principal : Chargement... ")
    iState = 0
    print("Menu Principal : iState = " + str(iState))

    EnleverWidget()
    
    tkMenuLabel = Label(tkFenetre, text="Labyrinthe")
    PositionRelative(tkMenuLabel, [0.5, 0.25])

    tkMenuButtonJouer = Button(tkFenetre, text="Jouer", command=lambda:TkJeu())
    PositionRelative(tkMenuButtonJouer, [0.5, 0.45])

    tkMenuButtonCreer = Button(tkFenetre, text="Créer", command=lambda:TkEditeur())
    PositionRelative(tkMenuButtonCreer, [0.5, 0.55])

    tkMenuButtonQuitter = Button(tkFenetre, text="Quitter", command=tkFenetre.destroy)
    PositionRelative(tkMenuButtonQuitter, [0.5, 0.65])

    # Créer les widgets de l'editeur de niveau {Statut : En Developpement}

def TkEditeur():
    print("Editeur : Chargement...")

    bEstAdditif = BooleanVar()
    bEstAdditif.set(bCheckResult)
    
    print("Editeur : bEstAdditif = " + str(bEstAdditif.get()))
    print("Editeur : bCheckResult = " + str(bCheckResult))

    iState = 2
    print("Editeur : iState = " + str(iState))
    EnleverWidget()
    
    TkAfficherMatrice()

    tkEditeurButtonNouveau=Button(tkFenetre, text="Nouvelle Map")
    PositionRelative(tkEditeurButtonNouveau, [0.80, 0.10])

    TkEditeurButtonPoint = Button(tkFenetre, text="Point", command=lambda:Edition(0, bEstAdditif.get()))
    PositionRelative(TkEditeurButtonPoint, [0.80, 0.33])

    TkEditeurButtonLigne = Button(tkFenetre, text="Ligne", command=lambda:Edition(1, bEstAdditif.get()))
    PositionRelative(TkEditeurButtonLigne, [0.85, 0.33])

    TkEditeurButtonRectangle = Button(tkFenetre, text="Rectangle", command=lambda:Edition(3, bEstAdditif.get()))
    PositionRelative(TkEditeurButtonRectangle, [0.90, 0.33])

    tkEditeurCheckBox = Checkbutton(tkFenetre, text="Additif", variable=bEstAdditif)
    PositionRelative(tkEditeurCheckBox, [0.85, 0.5])

    TkEditeurButtonMenu = Button(tkFenetre, text="Retourner au menu", command=lambda:TkMenuPrincipal())
    PositionRelative(TkEditeurButtonMenu, [0.80, 0.90])

    EditeurEvent()

    # Créer les widgets de la partie jeu {Statut : En Developpement}

def TkJeu():
    print("Jeu : Chargement...")

    iState = 1

    print("Jeu : iState = " + str(iState))
    EnleverWidget()
    
    TkAfficherMatrice()
    TkJeuButtonMenu = Button(tkFenetre, text="Retourner au menu", command=lambda:TkMenuPrincipal())
    PositionRelative(TkJeuButtonMenu, [0.90, 0.90])

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

def PositionRelative(widget, coordRelative = [0.5,0.5]):
    if 0 <= coordRelative[0] <= 1 and 0 <= coordRelative[1] <= 1:
        tkFenetre.update()
        Coord = [tkFenetre.winfo_width() * coordRelative[0], tkFenetre.winfo_height() * coordRelative[1]]
        widget.place(x = Coord[0], y = Coord[1])
    else:
        print("Erreur : Les coordonnée relative de " + str(widget) + " a au moins un de ses valeurs pas compris dans l'intervalle [0,1]")
   
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
        
        print("X = " +str(tkFenetre.winfo_pointerx()-tkFenetre.winfo_rootx()) + ", Y = " + str(tkFenetre.winfo_pointery()-tkFenetre.winfo_rooty()))
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

def Edition(arg, args):
    print("args = " + str(args))

    bCheckResult = args
    print("CheckResult " + str(bCheckResult))

    if arg == 0:
        mMatrice.SetPoint(mCaseCoord[0], args)
        TkEditeur()
    elif arg == 1:
        mMatrice.SetLine(mCaseCoord[0], mCaseCoord[1], args)
        TkEditeur()
    else:
        mMatrice.SetRectangle(mCaseCoord[0], mCaseCoord[1], args)
        TkEditeur()

#---------------------------------------------------------------------------------------------------------------
#                                           Le Laboratoire
#---------------------------------------------------------------------------------------------------------------

# Generation de niveau aleatoirement {Statut : En Developpemnt}

def RandomLevelGeneration():
    ## Generation matrice de base
    # Dimensions
    xmax = 30
    ymax = 30

    # matrice initiale
    laby=[]                       
    for i in range (ymax):
        laby.append([1]*xmax)
    #print(laby)
    
    # Coins fixes
    laby[0][0]=-1
    laby[xmax-1][0]=-1
    laby[0][ymax-1]=-1
    laby[xmax-1][ymax-1]=-1
    #laby[2][1]=0

    # Dessiner la matrice
    #print(laby)
    plt.imshow(laby, cmap='gray', interpolation='None')
    plt.show()

    ## Preparation de bot
    # Choix des premières coordonnées de bot
    #xini=round(xmax/2)
    xini=0
    yini=round(ymax/2)

    laby[xini][yini]=0

    xbot=xini
    ybot=yini

    # Archive des déplacements
    bot = []
    bot.append([xini,yini])
    #print(bot)

    # Passage
    continu=1
    step=0
    while continu==1 and step<(xmax*ymax)*10:
        step=step+1
        print(step)
    
        # choix de pas
        #al=randint(1,10)
    
        p1 = 25
        p2 = 25
        p3 = 25
        p4 = 100-p1-p2-p3
    
        al=random()*100
        ybotsave=ybot
        xbotsave=xbot
    
        if al<p1:
            #gauche
            if ybot>1:
                ybot=ybot-1
        elif al<(p1+p2):
            #bas
            xbot=xbot+1
        elif al<p1+p2+p3:
            #droite
            ybot=ybot+1
        else:
            #haut
            if xbot>1:
                xbot=xbot-1
    
        #eviter grandes salles
        if (xbot<xmax-1) and (ybot<ymax-1):
            if (laby[xbot+1][ybot]+laby[xbot][ybot+1]+laby[xbot+1][ybot+1]==0): 
                laby[xbot][ybot]=-1
    
    
        if (xbot>0) and (ybot<ymax-1):
            if (laby[xbot-1][ybot]+laby[xbot][ybot+1]+laby[xbot-1][ybot+1]==0):
                laby[xbot][ybot]=-1
        
        if (xbot<xmax-1)and(ybot>0):
            if(laby[xbot+1][ybot]+laby[xbot][ybot-1]+laby[xbot+1][ybot-1]==0):
                laby[xbot][ybot]=-1
            
        if (xbot>0)and(ybot>0):
            if (laby[xbot-1][ybot]+laby[xbot][ybot-1]+laby[xbot-1][ybot-1]==0):
                laby[xbot][ybot]=-1
    
        if laby[xbot][ybot]==-1:
            ybot=ybotsave
            xbot=xbotsave
        
        bot.append([xbot,ybot])
        print(xbot)
    
        # Creer passage
        laby[xbot][ybot]=0
    

        # Condition arret
        if (xbot==xmax-1) or (ybot==ymax-1) or (ybot==0):# or (xbot==0):
            continu=0
    laby[xbot][ybot]=3
    plt.imshow(laby, cmap='gray', interpolation='None')
    plt.show()
    print(bot)

    #Initialisation de la liste
    bot=[]

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

bCheckResult = True 

lDefaultSize = [720, 450]
lTailleMatrice = [30, 30]
lCoordJoueur=[0,0, 1]   #[0] coord X, [1] coord Y, [2] Orientation (0 = Up, 1 = Right, 2 = Down, 3 = Left)

mCaseCoord = [[0,0], [0,0]]
lScale = [1.0,1.0]
iState = 0

ilImageDimension = [15, 15]

mMatrice = Matrix(lTailleMatrice)
mMatrice.DebugDisplay()

GUI()