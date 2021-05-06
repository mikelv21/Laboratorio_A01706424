#Convolution Simple by Jose Miguel Luna Vega

#Libreria para mostrar la matriz resultante
import matplotlib.pyplot as plt

#Declaracion para dos ejemplos de convolucion
matrix=[ [1,2,3,4,5,6],
          [7,8, 9, 10, 11,12],
          [0, 0, 1,16,17,18],
          [0, 1, 0, 7,23,24],
          [1, 7, 6, 5, 4,3] ]
 
filter=[ [1,1,1],
          [0,0,0],
          [2,10,3] ]

matrix2=[ [10,4,50,30,20],
         [80,0, 0, 0, 6],
         [0, 0, 1,16,17],
         [0, 1, 0, 7,23],
         [1, 0, 6, 0, 4] ]

filter2=[ [1,0,1],
         [0,0,0],
         [1,0,3] ]

#Funcion auxiliar para los calculos aritmeticos de la convolucion
def conv_helper (mat, fil):
    res = int()
    for i in range(len(fil)):
        for j in range(len(fil[1])):
            res += mat[i][j]*fil[i][j]
    return res

#Funcion auxiliar para encontrar la matriz a operar dentro de la imagen
def create_matrix (matrix, col, fil,a,b):
    aux=[]
    for i in range (fil):
        fila=[]
        for j in range (col):
            fila.append(matrix[i+a][j+b])
        aux.append(fila)
    return (aux)

#Ejercicio de convolucion
def convolution (mat, kernel, padding, strides):
    res = []
    a = 0
    b = 0
    for i in range ( int(( (len(mat)-len(kernel)+2*padding)/strides) + 1) ):
        filaAux = []
        for j in range ( int(( (len(mat[1])-len(kernel[1])+2*padding)/strides) + 1) ):           
            aux = create_matrix(mat, len(kernel), len(kernel[1]),a,b)        
            filaAux.append(conv_helper(aux,kernel))
            b+=1
        b=0
        a+=1
        if(a==len(filter)):
            a=0
        res.append(filaAux)    
    return res

padding = 0
strides = 1

#Impresion de las matrices resultantes
print(convolution(matrix,filter, padding, strides))
print(convolution(matrix2,filter2, padding, strides))
plt.imshow(convolution(matrix,filter, padding, strides), cmap='gray')
plt.title("Output Image using {}X{} Kernel".format(len(filter), len(filter[1])))
plt.show()
plt.imshow(convolution(matrix2,filter2, padding, strides), cmap='gray')
plt.title("Output Image 2 using {}X{} Kernel".format(len(filter2), len(filter2[1])))
plt.show() 