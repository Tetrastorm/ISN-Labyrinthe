import pickle

class Matrix(object):

    # Constructor

    def __init__(self, lSizeMatrix, bIsAdditive = False):
        self.lSize = lSizeMatrix

        if bIsAdditive:
            fValue = 1
        else: 
            fValue = 0

        self.iaMatrix = [[fValue], [fValue]]
    
        for y in range(self.lSize[1]):
            self.iaMatrix.append([fValue])
            for x in range(self.lSize[0]):
                self.iaMatrix[y].append(fValue)
    
    # Setter/Getter function

    def GetMatrix(self):
        return self.iaMatrix

    def GetSize(self):
        return self.lSize

    def SetMatrix(self, iValue, lCoord):
        if lCoord[0] >= 0 and lCoord[0] <= self.lSize[0] and lCoord[1] >= 0 and lCoord[1] <= self.lSize[1]:
            self.iaMatrix[Coord[1]][Coord[0]] = iValue
        else:
            print("Error : Coordinate is out range of matrix size")
    
    # Debug Function

    def DebugDisplay(self):
        for i in range(lSize[1]):
            print(str(self.iaMatrix[i]))

    # Save/Load System

    def SavingMatrix(self):
        return 0

    # Edition tools

    def SetPoint(self, lCoord, bIsAdditive = True):
        if bIsAdditive:
            self.SetMatrix(lCoord, 1)
        else:
            self.SetMatrix(lCoord, 0)

    def SetLine(self, lCoordA, lCoordB, bIsAddive = True):        
        if lCoordA[0] == lCoordB[0]:
            lTempCoord[0] = lCoordA[0]

            if lCoordA[1] > lCoordB[1]:
                for i in range(lCoordB[1], (lCoordA[1] + 1)):
                    lTempCoord[1] = i
                    self.SetPoint(lTempCoord, bIsAdditive)
            else:
                for i in range(lCoordA[1], (lCoordB[1] + 1)):
                    lTempCoord[1] = i
                    self.SetPoint(lTempCoord, bIsAdditive)

        elif lCoordA[1] == lCoordB[1]:
            lTempCoord[1] = lCoordA[1]

            if lCoordA[0] > lCoordB[0]:
                for i in range(lCoordB[0], (lCoordA[0] + 1)):
                    lTempCoord[0] = i
                    self.SetPoint(lTempCoord, bIsAdditive)
            else:
                for i in range(lCoordA[0], (lCoordB[0] + 1)):
                    lTempCoord[0] = i
                    self.SetPoint(lTempCoord, bIsAdditive)
        else:
            print("Erreur : La Ligne n'est pas verticale ou horizontale")

    def SetRectangle(self, lCoordA, lCoordB, bIsAdditive = True):
        lTempCoord = [lCoordA[0], lCoordB[1]]
        self.SetLine(lCoordA, lTempCoord, bIsAdditive)
        self.SetLine(lCoordB, lTempCoord, bIsAdditive)

        lTempCoord = [lCoordB[0], lCoordA[1]]     
        self.SetLine(lCoordA, lTempCoord, bIsAdditive)
        self.SetLine(lTempCoord, lCoordB, bIsAdditive)