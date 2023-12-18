import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos\\bigotes.csv")
print(df)
# creando el grafico
sns.boxplot(x="categoria", y="valor", data=df)
# mostrando el grafico
plt.show()
