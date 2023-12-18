archivo_a_abrir = "archivos/notas.txt"
with open(archivo_a_abrir, encoding="UTF-8") as archivo:
    contenido = archivo.read()
    print(contenido)
    
    
    
def escribir():
    pregunta()

def pregunta():
    resp = input("¿Quieres escribir? ")
    if resp == "si":
        escribir()
    elif resp == "no":
        print("Hasta la próxima")

pregunta()
