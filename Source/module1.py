import matplotlib
import matplotlib.pyplot as plt
from random import *

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

