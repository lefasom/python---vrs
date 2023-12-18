import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos\\gastos.csv")
print(df)
# creando el grafico
sns.lineplot(x="fecha",y="gastos", data = df)
# creando un punto 
plt.plot("1-05",5000,"o")
# mostrando el grafico
plt.show()