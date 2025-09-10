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
cv2.destroyAllWindows() # Cerramos todas las ventanas abiertas por OpenCV
# Mostramos la imagen.

imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
# https://opencv.org/blog/color-spaces-in-opencv/

cv2.imshow("NaranjaGris", imagen_gris)
cv2.waitKey(0)
cv2.destroyAllWindows()

# quiero cambiar el tamaño a 200x200
imagen_chica = cv2.resize(imagen, (200, 200))
cv2.imshow("NaranjaChica", imagen_chica)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_line = cv2.line(imagen, (50,50), (200,50), (0,0,255), 2)
cv2.imshow("NaranjaLinea", img_line)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Quiero hacer detección de bordes con Canny
imagen_canny = cv2.Canny(imagen, 100, 200)
cv2.imshow("NaranjaCanny", imagen_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

# quiero hacer detección de bordes pero con fondo blanco y borde negro
imagen_canny_inv = cv2.bitwise_not(imagen_canny)
cv2.imshow("NaranjaCannyInv", imagen_canny_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()