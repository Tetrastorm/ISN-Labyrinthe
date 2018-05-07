class Matrix(object):
    
    global iaMatrix, lSize

    def __init__(self, lSizeMatrix, bIsAdditif):
        self.lSize = lSizeMatrix

        if isAdditif:
            fValue = 1
        else: 
            fValue = 0

        self.iaMatrix = [[fValue], [fValue]]
    
        for y in range(self.lSize[1]):
            self.iaMatrix.append([fValue])
            for x in range(lSize[0]):
                self.iaMatrix[y].append(fValue)

    def GetMatrix(self):
        return self.iaMatrix

    def SetMatrix(self, iValue, lCoord):
        if lCoord[0] >= 0  and lCoord <= self.lSize[0] and lCoord[1] >= 0   and lCoord <= self.lSize[1]:
            self.iaMatrix[Coord[1]][Coord[0]] = iValue

    def DebugDisplay(self):
        for i in range(lSize[1]):
            print(str(self.iaMatrix[i]))