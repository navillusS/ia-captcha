import os 
from PIL import Image



def segment(imagenes_invertidas_path, imagenes_segmentadas_path ,cantidad = 0):
    if not ('a' in os.listdir(imagenes_segmentadas_path)):
        abc = 'abcdefghijklmnopqrstuvwxyz0123456789'
        for letter in abc:
            os.makedirs(imagenes_segmentadas_path + '\\' + letter, 0o777)

    cantidad_segmentos = 5
    list_img_inv = os.listdir(imagenes_invertidas_path)
    if cantidad > 0:
        nro_veces = cantidad
        imagen = list_img_inv[:cantidad]
        for i in range(cantidad):
            imagen = imagen[i]
            img=Image.open(imagenes_invertidas_path + '/' + imagen)
            first = imagen[0]
            second = imagen[1]
            third =  imagen[2]
            fourth = imagen[3]
            fifth = imagen[4]

            img_recortada_0 = img.crop((15,0,35,59))#hardcodeo
            img_recortada_0.save(imagenes_segmentadas_path + '/' + first +'/' + first + imagen[5:])    

            img_recortada_1 = img.crop((35,0,65,59))
            img_recortada_1.save(imagenes_segmentadas_path + '/' + second +'/' + second + imagen[5:])    

            img_recortada_2 = img.crop((65,0,95,59))
            img_recortada_2.save(imagenes_segmentadas_path + '/' + third + '/'  + third + imagen[5:])    

            img_recortada_3 = img.crop((95,0,130,59))
            img_recortada_3.save(imagenes_segmentadas_path + '/' + fourth + '/' + fourth  + imagen[5:])    

            img_recortada_4 = img.crop((130,0,160,59))
            img_recortada_4.save(imagenes_segmentadas_path + '/' + fifth +'/'  + fifth + imagen[5:])    
            if nro_veces == 0:
                print("DONE")
                return
            else:
                nro_veces -= 1
    elif cantidad < 0:
        print("Crei que lo habiamos superado")
        return
    else:
        for imagen in list_img_inv:
            img=Image.open(imagenes_invertidas_path + '/' + imagen)
            first = imagen[0]
            second = imagen[1]
            third =  imagen[2]
            fourth = imagen[3]
            fifth = imagen[4]

            img_recortada_0 = img.crop((15,0,35,59))#hardcodeo
            img_recortada_0.save(imagenes_segmentadas_path + '/' + first +'/' + first + imagen[5:])    

            img_recortada_1 = img.crop((35,0,65,59))
            img_recortada_1.save(imagenes_segmentadas_path + '/' + second +'/' + second + imagen[5:])    

            img_recortada_2 = img.crop((65,0,95,59))
            img_recortada_2.save(imagenes_segmentadas_path + '/' + third + '/'  + third + imagen[5:])    

            img_recortada_3 = img.crop((95,0,130,59))
            img_recortada_3.save(imagenes_segmentadas_path + '/' + fourth + '/' + fourth  + imagen[5:])    

            img_recortada_4 = img.crop((130,0,160,59))
            img_recortada_4.save(imagenes_segmentadas_path + '/' + fifth +'/'  + fifth + imagen[5:])    
        print("DONE")
        return


def main():
    segment('C:\\Users\\tantrix\\Documents\\Pythonize\\ia-things\\ia-things-test\\invertir', 'C:\\Users\\tantrix\\Documents\\Pythonize\\ia-things\\ia-things-test\\segmentar')


if __name__ == "__main__":
    main()
