#Libreria para manejar matrices
import numpy as np

#Funcion para hacer el padding recibiendo una matriz y el valor 
def padding(mat, p):
    row, col = mat.shape
    matP = np.zeros((row+p*2,col+p*2))
    matP[p:matP.shape[0]-p, p:matP.shape[1]-p] = mat
    return matP

#Ejemplo de prueba con padding = 1 
p = 1
originalMatrix = np.matrix('1,1,1; 0,0,0 ; 2,10,3')
matrixPadded = padding(originalMatrix,p)
print(matrixPadded)
