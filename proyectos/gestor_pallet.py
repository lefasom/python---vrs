import matplotlib.pyplot as plt

# Tamaño del plano y tamaño de los cuadrados en centímetros
base = 100
cuadrado_lado = 1

# Número de cuadrados en un lado del plano
num_cuadrados_lado = base // cuadrado_lado

# Crear una matriz para representar el plano
plano = [[0] * num_cuadrados_lado for _ in range(num_cuadrados_lado)]


# Función para agregar una caja en el plano
def agregar_caja(x, y, ancho, alto):
    for i in range(x, x + ancho):
        for j in range(y, y + alto):
            if i < num_cuadrados_lado and j < num_cuadrados_lado:
                plano[i][j] = 1


# Agregar cajas al plano (ejemplo)
# agregar_caja(0, 0, 10, 10)
agregar_caja(0, 10, 10, 10)

# agregar_caja(10, 10, 3, 8)
# agregar_caja(30, 70, 6, 4)

# Crear la representación gráfica del plano
plt.imshow(plano, cmap="Blues", origin="lower", extent=[0, base, 0, base])
plt.colorbar(label="Sección ocupada")
plt.xlabel("Longitud (cm)")
plt.ylabel("Ancho (cm)")
plt.title("Plano con cajas")
plt.grid(True, linewidth=0.5, color="gray", linestyle="--")

# Mostrar el plano
plt.show()
