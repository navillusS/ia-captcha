import numpy as np
import cv2 as cv
from PIL import Image
import os
from matplotlib import pyplot as plt


# def segment(imagenes_invertidas_path, imagenes_segmentadas_path ,cantidad = 0):
#     # cantidad_segmentos = 5
#     return 



# im = cv.imread('C:\\Users\\tantrix\\Documents\\Pythonize\\ia-things\\ia-things-test\\invertir\\imagen0.jpg')
im = cv.imread('C:\\Users\\tantrix\\Documents\\Pythonize\\ia-things\\ia-things-test\\invertir\\imagen0.jpg')
print(im.shape)


white_pixels = []
cont_white_pixels = [0] * 200 
densidad_white_pixels = [0] * 200
threshold = (250,250,250)
for x in range(200):
    for y in range(60):
        b = im.item(y,x,0)
        g = im.item(y,x,1)
        r = im.item(y,x,2)
        pixel = tuple([r,g,b])
        if pixel > threshold:
            cont_white_pixels[x] += 1
            white_pixels.append(pixel)


for index, cont in enumerate(cont_white_pixels):
    densidad_white_pixels[index] = cont/200

    
print(densidad_white_pixels)
print(max(densidad_white_pixels), min(densidad_white_pixels), sum(densidad_white_pixels)/len(densidad_white_pixels))


def get_front_neigh(vector, point, neightbors=5):
    i = 1 
    while i<neightbors:
        yield vector[point+i]
        i += 1

def check_front_neigh(generator_pointer, value_point, operation):
    value_list = [x for x in generator_pointer]
    value = operation(value_list)
    if operation = min:
        if value_point < value:
            
    if operation = max:











    if value_point < value:
        es_menor = True
    else:
        es_mayor = False
    


            
        
        





cuts = 6
neightbors = 10
cuts_x_cordinate = []
max_den = 0
min_den = 0
first_up = True

for x_cord, densi in enumerate(densidad_white_pixels):
    if min_den < densi:
        check_neigh()










    
    



            
cv.imshow('imagen', im)
cv.waitKey(0)
# for i in im:
#     for y in i:
#         print(y)
# imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
# ret, thresh = cv.threshold(imgray, 127, 255, 0)
# contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# im2 = cv.drawContours(im,  contours[0], 0, (0,255,0), 3)
# for cnt in contours[1:30]:
#     im2 = cv.drawContours(im2,  [cnt], 0, (0,255,0), 3)

# plt.imshow(im2)
# plt.show()