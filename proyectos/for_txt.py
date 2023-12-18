apellidos = ["sombra","vargas","huaman","herrera"]
nombres = ["leonardo","lucas","michael","ignacio"]


with open("archivos/nombre_y_apellido.txt","w") as arch:
    arch.writelines("nombres y apellidos: \n")
    [arch.writelines(f'nombre: {n} \n apellido: {a} \n----------------\n') for n,a in zip(nombres,apellidos)]