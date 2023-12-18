import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos\\dispersion.csv")
print(df)
# creando el grafico
sns.scatterplot(x="tiempo", y="dinero", data=df)
# mostrando el grafico
plt.show()
