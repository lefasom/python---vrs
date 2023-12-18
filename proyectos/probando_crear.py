import pandas as pd

df = pd.read_csv("archivos\\futbol.csv")

# reemplazar datos

df["equipo"].replace("river", "independiente", inplace=True)

# eliminar filas con datos vacios
df = df.dropna()

# eliminar datos repetido
df = df.drop_duplicates()

df.to_csv("archivos\\futbol_limpio_sin_panda.csv")