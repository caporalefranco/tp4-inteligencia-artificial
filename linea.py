# Se importan las librerías de cv2 y numpy
import cv2
import numpy as np

# Se carga la imagen motor.jpg del directorio actual y se la almacena en la variable img
img = cv2.imread('motor.jpg')
# Se muestra la imagen original
cv2.imshow('Motor-Original', img)
# Se aguarda hasta que se presione una tecla en la ventana de la imagen
cv2.waitKey(0)

# Se convierte la imagen en escala de grises y se la muestra en una ventana
img_gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Motor-Escala-Grises', img_gray_scale)
cv2.waitKey(0)

# Se detectan los bordes en la imagen en escala de grises utilizando el algoritmo de detección de bordes Canny 
# y luego muestran los bordes encontrados en una ventana.

edges = cv2.Canny(img_gray_scale,50,150)
cv2.imshow('Motor - Bordes de imagen', edges)
cv2.waitKey(0)

# Se aplica la transformada de hough
lines = cv2.HoughLines(edges, 1, np.pi/180, 160)


if lines is not None:
    # Se recorren las líneas detectadas por la transformada de Hough y se dibujan las líneas en la imagen
    for line in lines:
        # Obtener los valores de rho (distacia) y de theta (ángulo)
        rho, theta = line[0]
        # Guardar el valor del cos(theta)
        a = np.cos(theta)
        # Guardar el valor del sen(theta)
        b = np.sin(theta)
        # Guardar el valor de r cos(theta)
        x0 = a*rho
        # Guardar el valor de r sen(theta), todo se está haciendo de forma paramétrica
        y0 = b*rho
        # Ahora todo se recorrerá de -1000 a 1000 pixeles
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        # Generar las líneas para montarlas en la imagen original
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1, cv2.LINE_AA)

    # Se muestra la imagen original con todas las líneas halladas
    cv2.imshow('Motor - Detección de lineas', img)
    cv2.waitKey(0)

# Se destruyen todas las ventanas
cv2.destroyAllWindows()
