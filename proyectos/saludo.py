# from funciones.calculo_edad import calculo_edad

# archivo_a_abrir = "archivos/notas.txt"
# with open(archivo_a_abrir, encoding="UTF-8") as archivo:
#     contenido = archivo.read()
#     print(contenido)
# naci = input("en que año naciste ?")
# print("tu edad es de :", calculo_edad(naci))

# archivo_a_abrir = "archivos/notas.txt"
# with open(archivo_a_abrir, encoding="UTF-8") as archivo:
#     contenido = archivo.read()
#     print(contenido)
    
archivo_a_abrir = "archivos/notas.txt"

    
    
def escribir():
    nota = input("escribe :")
    with open(archivo_a_abrir,"a", encoding="UTF-8") as archivo:
        archivo.writelines([f"{nota}\n"])

    pregunta()

def pregunta():
    resp = input("¿Quieres escribir? ")
    if resp == "si":
        escribir()
    elif resp == "no":
        print("Hasta la próxima")

pregunta()

