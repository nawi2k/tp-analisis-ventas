print("Análisis de ventas")

import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("datos/Ventas.csv")

datos["ventas"] = datos["precio"] * datos["cantidad"]

suma = datos["ventas"].sum()

print("Ventas totales:", suma)

grupo = datos.groupby("producto")

suma_grupo = grupo["cantidad"].sum()

mayor = suma_grupo.idxmax()

print("Producto más vendido:", mayor)

suma_grupo.plot(kind="bar")

plt.savefig("resultados/grafico_ventas.png")

plt.title("Ventas por producto")

plt.xlabel("Productos")

plt.ylabel("Cantidad vendida")

plt.show()