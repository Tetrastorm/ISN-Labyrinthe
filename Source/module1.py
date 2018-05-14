import pickle
import Matrix

test = Matrix.Matrix([30,30])

file = open('Picle test','w')
pickle.Pickler(file, 0).dump(test)