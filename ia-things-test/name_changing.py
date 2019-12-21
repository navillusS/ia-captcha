import os
import csv


def name_change(etiquetado_path, imagenes_path, etiquetado_field_number, imagen_field_number):

"""Para usar esto se debe enviar un archivo csv con la misma cantidad de lineas y ordenado de la forma en la que salga al listar los archivos 
 donde esten las imagenes. Tambien tienes que mandar el campo en donde esta el etiquetado y el numero."""

    os.chdir(imagenes_path)
    with open(etiquetado_path) as file:
        csv_reader = csv.reader(file, delimiter=',')
        imgs = os.listdir()
        imgs_tags = [list(img_tag) for img_tag in zip(imgs, csv_reader)]
        for row in imgs_tags:
            print("Cambiando el nombre " + row[0] + " por " +  row[1][etiquetado_field_number] + "_" + row[1][imagen_field_number]+ ".jpg")
            print(os.rename(row[0],row[1][etiquetado_field_number] + "_" + row[1][imagen_field_number]+ ".jpg"))


def main():
    name_change(etiquetado_path='C:\\Users\\tantrix\\Documents\\Pythonize\\ia-things\\etiquetado.csv', imagenes_path='C:\\Users\\tantrix\\Documents\\Pythonize\\ia-things\\imgs', 2, 5)

if __name__ == "__main__":
    main()