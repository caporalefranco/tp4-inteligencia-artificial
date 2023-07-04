# Se importan las librerías de cv2 y numpy
import cv2 
import numpy as np 
  
# Se carga la imagen motor.png del directorio actual y se la almacena en la variable img
img = cv2.imread('motor.png', cv2.IMREAD_COLOR) 
# Se muestra la imagen original
cv2.imshow('Motor-Original', img)
# Se aguarda hasta que se presione una tecla en la ventana de la imagen
cv2.waitKey(0)

# Se convierte la imagen en escala de grises y se la muestra en una ventana
img_gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imshow('Motor-Escala-Grises', img_gray_scale) 
cv2.waitKey(0)

# Ahora se aplica un filtro de desenfoque para reducir el ruido en la imagen
img_blur = cv2.blur(img_gray_scale, [3,3]) 
cv2.imshow('Motor-Borrosa', img_blur )
cv2.waitKey(0)

# Se realiza la detección de círculos en una imagen utilizando la transformada de Hough circular.
# Se ajustó la sensibilidad con los parámetros (param1 y param2) para que la detección en la imagen cargada sea la adecuada
# Los parámetros de minRadius y maxRadius establecen el radio mínimo y el radio máximo de los círculos que se desean detectar.
circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 50, minRadius = 1, maxRadius = 40) 
  
# Revisar que el método haya regresado algún valor
if circles is not None: 
  
    # Convertir los parámetros el círculo a, b, y r en enteros de 16 bits
    detected_circles = np.uint16(np.around(circles)) 
  
    # Ahora si se recorren todos los círculos detectados
    for pt in detected_circles[0, :]: 
        a, b, r = pt[0], pt[1], pt[2] 
  
        # Dibujar la circunferencia
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)   
        # Dibujar un círculo pequeño alrededor del centro
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)

    # Se muestra la imagen con los circulos encontrados
    cv2.imshow("Detección de circunferencias", img) 
    cv2.waitKey(0) 
    
#Se destruyen todas las ventanas
cv2.destroyAllWindows()

