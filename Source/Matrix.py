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
        self.mChange = [[0,0],[0.0]]

        for y in range(self.lSize[1]):
            self.iaMatrix.append([fValue])
            for x in range(self.lSize[0]):
                self.iaMatrix[y].append(fValue)
    
    # Setter/Getter function

    def GetMatrix(self):
        return self.iaMatrix

    def GetValue(self, Coord):
        return self.iaMatrix[Coord[0]][Coord[1]]

    def GetValue(self, lCoord):
        if 0 <= lCoord[0] < self.lSize[0] and 0 <= lCoord[1] < self.lSize[1]:
            return self.iaMatrix[lCoord[0]][lCoord[1]]
        else:
            print("Error : Coordinate is out range of matrix size")

    def GetSize(self):
        return self.lSize

    def SetValue(self, lCoord, iValue):
        if 0 <= lCoord[0] < self.lSize[0] and 0 <= lCoord[1] < self.lSize[1]:
            self.iaMatrix[lCoord[0]][lCoord[1]] = iValue
        else:
            print("Error : Coordinate is out range of matrix size")
    
    def SetMatrix(self, iValue):
        for y in range(self.lSize[1]):
            for x in range(self.lSize[0]):
                self.SetValue([x,y], iValue)
    
    def Switch(self, a, b):
        for y in range(self.lSize[1]):
            for x in range(self.lSize[0]):
                if self.iaMatrix[x][y] == a:
                    self.iaMatrix[x][y] = b

    # Debug Function

    def DebugDisplay(self):
        for i in range(self.lSize[1]):
            print(str(self.iaMatrix[i]))

    # Save/Load System

    def SavingMatrix(self):
        return 0

    # Edition tools

    def SetLine(self, lCoordA, lCoordB, iValue = 0):        
        lTempCoord = [0,0]

        if lCoordA[0] == lCoordB[0]:
            lTempCoord[0] = lCoordA[0]

            if lCoordA[1] > lCoordB[1]:
                for i in range(lCoordB[1], (lCoordA[1] + 1)):
                    lTempCoord[1] = i
                    self.SetValue(lTempCoord, iValue)
            else:
                for i in range(lCoordA[1], (lCoordB[1] + 1)):
                    lTempCoord[1] = i
                    self.SetValue(lTempCoord, iValue)

        elif lCoordA[1] == lCoordB[1]:
            lTempCoord[1] = lCoordA[1]

            if lCoordA[0] > lCoordB[0]:
                for i in range(lCoordB[0], (lCoordA[0] + 1)):
                    lTempCoord[0] = i
                    self.SetValue(lTempCoord, iValue)
            else:
                for i in range(lCoordA[0], (lCoordB[0] + 1)):
                    lTempCoord[0] = i
                    self.SetValue(lTempCoord, iValue)
        else:
            print("Erreur : La Ligne n'est pas verticale ou horizontale")

    def SetRectangle(self, lCoordA, lCoordB, iValue = 0):
        lTempCoord = [lCoordA[0], lCoordB[1]]
        self.SetLine(lCoordA, lTempCoord, iValue)
        self.SetLine(lCoordB, lTempCoord, iValue)

        lTempCoord = [lCoordB[0], lCoordA[1]]     
        self.SetLine(lCoordA, lTempCoord, iValue)
        self.SetLine(lTempCoord, lCoordB, iValue)