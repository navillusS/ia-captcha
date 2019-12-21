import cv2
from PIL import Image
import os


def binarizar(imagenes_path, imagenes_binarizadas_path, cantidad=0):
    imagenes_name = os.listdir(imagenes_path)
    if cantidad > 0:
        numero_veces = cantidad
        imagen = imagenes_name[:cantidad]
        for i in range(cantidad):
            imag_gris = cv2.imread(imagenes_path + "/" + imagen[i], cv2.IMREAD_GRAYSCALE) # hace lectura de la imagen
            imag_gris = cv2.medianBlur(imag_gris, 1)
            imag_bin = cv2.adaptiveThreshold(imag_gris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
            cv2.imwrite(imagenes_binarizadas_path + "/" + imagen[i], imag_bin)
            print(imagenes_binarizadas_path + "\\"+ imagen[i])
            if numero_veces != 0:
                numero_veces -= 1
            else:
                return 

    elif cantidad < 0:
        print("Ya ps, que intentas hacer?")
        return
    else:
        for imagen in imagenes_name:
            imag_gris = cv2.imread(imagenes_path + "/" + imagen, cv2.IMREAD_GRAYSCALE) # hace lectura de la imagen
            imag_gris = cv2.medianBlur(imag_gris, 1)
            imag_bin = cv2.adaptiveThreshold(imag_gris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
            cv2.imwrite(imagenes_binarizadas_path + "/" + imagen, imag_bin)
            print(imagenes_binarizadas_path + "\\"+ imagen)
        print("DONE")
        return


        
def invertir(imagenes_binarizadas_path, imagenes_invertidas_path, cantidad=0):
    imagenes_binarizadas = os.listdir(imagenes_binarizadas_path)
    if cantidad > 0:
        from PIL import ImageChops 
        numero_veces = cantidad
        imagen_binarizada = imagenes_binarizadas[:cantidad]
        for i in range(cantidad):
            ima = Image.open(imagenes_binarizadas_path + "/" + imagen_binarizada[i])
            imagen = ImageChops.invert(ima)
            imagen.save(imagenes_invertidas_path + "/" + imagen_binarizada[i])
            print(imagenes_invertidas_path + "\\" + imagen_binarizada[i])
            if numero_veces == 0:
                print("done")
                return
            else:
                numero_veces -= 1 
    elif cantidad< 0:
        print("Otra vez?")
        return
    else:
        from PIL import ImageChops 
        for imagen_binarazada in imagenes_binarizadas:
            ima = Image.open(imagenes_binarizadas_path + "/" + imagen_binarazada)      
            imagen = ImageChops.invert(ima)
            imagen.save(imagenes_invertidas_path + "/" + imagen_binarazada)
            print(imagenes_invertidas_path + "\\" + imagen_binarazada)
        print("DONE")
        return

binarizar('C:\\Users\\tantrix\\Documents\\Pythonize\\ia-things\\ia-things-test\\imgs', 'C:\\Users\\tantrix\\Documents\\Pythonize\\ia-things\\ia-things-test\\binarizar')
invertir('C:\\Users\\tantrix\\Documents\\Pythonize\\ia-things\\ia-things-test\\binarizar', 'C:\\Users\\tantrix\\Documents\\Pythonize\\ia-things\\ia-things-test\\invertir')

