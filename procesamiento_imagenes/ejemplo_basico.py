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
# cv2.imwrite("imagenes/naranja_copia.jpg", imagen)
cv2.waitKey(0)
