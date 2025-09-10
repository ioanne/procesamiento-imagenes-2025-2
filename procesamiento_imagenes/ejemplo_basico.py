# opencv
# Pueden buscarlo en pypi.org (googleando "pypi opencv")

import cv2

imagen = cv2.imread("imagenes/naranja.jpg")

# podemos usar dir para ver los atributos y metodos de un objeto
# dir(imagen) # El dir no funciona solo para el objeto principal, sino para cualquier cosa.
# dir(imagen.diagonal) # diagonal es un atributo de imagen

# Tambien podemos ver la ayuda de un objeto
# help(imagen)

cv2.imshow("Naranja", imagen)
cv2.waitKey(0)
# Mostramos la imagen.

imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
# https://opencv.org/blog/color-spaces-in-opencv/

cv2.imshow("NaranjaGris", imagen_gris)
cv2.waitKey(0)
