#Same Convolution by Jose Miguel Luna Vega

import numpy as np
import cv2
import matplotlib.pyplot as plt
 
#Funcion para hacer una same convolucion  
def convolution(image, kernel, strides, average = False):
    
    #Dejar una imagen en 2 dimensiones si es necesario
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #Obtener las columnas y filas de image y el kernel
    image_row, image_col = image.shape
    kernel_row, kernel_col = kernel.shape
    
    #Calcular el pad necesario 
    pad_height = int((kernel_row - 1) / 2)
    pad_width = int((kernel_col - 1) / 2)
 
    #Convertir la imagen original a una con padding
    padded_image = np.zeros((image_row + (2 * pad_height), image_col + (2 * pad_width)))
    padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = image

    #Calcular el tamaño de la matriz resultante
    output_row = int(( (image_row-kernel_row+2*pad_height)/strides) + 1)
    output_col = int(( (image_col-kernel_col+2*pad_width)/strides) + 1)
    output = np.zeros((output_row,output_col))
 
    #Hacer el procesos de convolucion
    for row in range(output_row):
        for col in range(output_col):
            output[row, col] = np.sum(kernel * padded_image[row:row + kernel_row, col:col + kernel_col])
            if average:
                output[row, col] /= kernel.shape[0] * kernel.shape[1]
 
    return output

#Variables para caso de prueba
strides = 1
matrix = np.matrix(' 1,2,3,4,5,6 ; 7,8, 9, 10, 11,12 ; 0, 0, 1,16,17,18 ; 0, 1, 0, 7,23,24 ; 1, 7, 6, 5, 4,3')
filter = np.matrix(' 1,1,1 ; 0,0,0 ; 2,10,3 ')

#Demostracion de caso de prueba
print(convolution(matrix,filter,strides))
plt.imshow(convolution(matrix,filter,strides), cmap='gray')
plt.title("Output Image using {}X{} Kernel".format(filter.shape[0], filter.shape[1]))
plt.show()
 
