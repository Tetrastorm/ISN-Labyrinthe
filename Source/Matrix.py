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

    def SetMatrix(self, iValue, Coord):
        return 0

    def DebugDisplay(self):
        for i in range(lSize[1]):
            print(str(self.iaMatrix[i]))