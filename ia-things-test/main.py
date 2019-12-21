import numpy as np
import cv2
from PIL import Image
import os
from name_changing import name_change    



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
            if numero_veces == 0:
                print("done")
                return
            else:
                numero_veces -= 1
    elif cantidad < 0:
        print("Ya ps, que intentas hacer?")
        return
    else:
        for imagen in imagenes_name:
            imag_gris = cv2.imread(imagenes_path + "/" + imagen, cv2.IMREAD_GRAYSCALE) # hace lectura de la imagen
            imag_gris = cv2.medianBlur(imag_gris, 1)
            imag_bin = cv2.adaptiveThreshold(imag_gris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
            cv2.imwrite(imagenes_binarizadas_path + "/" + imagen, imag_bin)
        print("DONE")
        return


        
def invertir(imagenes_binarizadas_path, imagenes_invertidas_path, cantidad=0):
    imagenes_binarizadas = os.listdir(imagenes_binarizadas_path)
    if cantidad > 0:
        numero_veces = cantidad
        imagen_binarizada = imagenes_binarizadas[:cantidad]
        from PIL import ImageChops 
        for i in range(cantidad):
            ima = Image.open(imagenes_binarizadas_path + "/" + imagen_binarizada[i])      
            imagen = ImageChops.invert(ima)
            imagen.save(imagenes_invertidas_path + "/" + imagen_binarizada[i])
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
        return

def segmentar(cant_imag):
    m=1
    for i in range(cant_imag):
        img=Image.open('Invertido/imagen'+str(i+1)+'.jpg')
        #img_recortada = img.crop((5,0,50,59))
        img_recortada = img.crop((15,0,35,59))#hardcodeo
       # img_recortada_1 = img.crop((45,0,90,59))
        img_recortada_1 = img.crop((35,0,65,59))
        #img_recortada_2 = img.crop((85,0,130,59))
        img_recortada_2 = img.crop((65,0,95,59))
        img_recortada_3 = img.crop((95,0,130,59))
        img_recortada_4 = img.crop((130,0,160,59))
        img_recortada.save('SEGMENTACION/imagen'+str(i+1)+'_1.jpg')
        img_recortada_1.save('SEGMENTACION/imagen'+str(i+1)+'_2.jpg')
        img_recortada_2.save('SEGMENTACION/imagen'+str(i+1)+'_3.jpg')
        img_recortada_3.save('SEGMENTACION/imagen'+str(i+1)+'_4.jpg')
        img_recortada_4.save('SEGMENTACION/imagen'+str(i+1)+'_5.jpg')
        m = m+1
 
def main():
    cant_imag = 5
    binarizar(cant_imag)
    invertir(cant_imag)
    segmentar(cant_imag)

main()
