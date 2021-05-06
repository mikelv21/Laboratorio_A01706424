#Padding by Jose Miguel Luna Vega

#Libreria para manejar matrices
import numpy as np

#Funcion para hacer el padding recibiendo una matriz y un kernel 
def padding(mat, kernel):
    row_k, col_k = kernel.shape
    row_m, col_m = mat.shape

    pad_height = int((row_k - 1) / 2)
    pad_width = int((row_k - 1) / 2)
    
    matP = np.zeros((row_m+pad_height*2,col_m+pad_width*2))
    matP[pad_height:matP.shape[0]-pad_height, pad_width:matP.shape[1]-pad_width] = mat
    return matP

#Ejemplo de prueba 
kernel = np.matrix(' 1,1,1 ; 0,0,0 ; 2,10,3 ')
originalMatrix = np.matrix('1,1,1; 0,0,0 ; 2,10,3')
matrixPadded = padding(originalMatrix,kernel)
print(matrixPadded)
