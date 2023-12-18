import csv

with open("archivos\\datos.csv","r",encoding="UTF-8") as archivo:
    print(csv.reader(archivo))
    for row in archivo:
        print(row)