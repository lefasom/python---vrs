import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# pongo colores por que por defecto son todos azul


df = pd.read_csv("archivos\\ganancias.csv")
total_de_ingresos = df["ingresos"].sum()

print(f"el total de ingresos es $ {total_de_ingresos} USD")
# creando el grafico
sns.barplot(x="fuente", y="ingresos", data=df, hue=df["fuente"])
# mostrando el grafico
plt.show()
