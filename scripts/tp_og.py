# ==============================================================================
# PROYECTO: Módulo Automatizado de Análisis de Ventas (E-commerce)
# ROL: Data Engineer / Backend Developer (Nahuel Sandoval)
# TAREA JIRA ASOCIADA: NAHUE2004-5 y NAHUE2004-6
# ==============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import os  # Librería nativa para el manejo dinámico de rutas del sistema

print("Iniciando análisis automatizado de ventas comerciales...")

# 1. Resolución dinámica de rutas para asegurar reproducibilidad absoluta
# Detecta la ubicación del script actual y retrocede a la raíz del proyecto
ruta_script = os.path.dirname(os.path.abspath(__file__))
ruta_raiz_proyecto = os.path.dirname(ruta_script)

# Define los caminos correctos hacia los archivos estructurados
ruta_csv = os.path.join(ruta_raiz_proyecto, "datos", "Ventas.csv")
ruta_grafico = os.path.join(ruta_raiz_proyecto, "resultados", "grafico_ventas.png")

# 2. Carga segura del Dataset mediante el manejo de excepciones
try:
    datos = pd.read_csv(ruta_csv)
    print(f"Dataset cargado exitosamente desde: {ruta_csv}")
except FileNotFoundError:
    print(f"Error crítico: No se encontró el archivo Ventas.csv en la ruta calculada: {ruta_csv}")
    print("Verifique que el archivo CSV se encuentre dentro de la carpeta /datos.")
    exit()  # Detiene la ejecución de forma limpia para evitar NameError

# 3. Procesamiento de datos y cálculo de métricas de negocio (Métrico: Facturación Total)
# Se genera una nueva serie calculada multiplicando precio unitario por cantidad de unidades
datos["ventas"] = datos["precio"] * datos["cantidad"]
suma = datos["ventas"].sum()
print("Ventas totales calculadas: $", suma)

# 4. Lógica de agrupación para identificar demanda (Métrico: Producto más vendido)
# Se agrupa por el identificador del producto y se suma el volumen total de unidades
grupo = datos.groupby("producto")
suma_grupo = group_suma = grupo["cantidad"].sum()
mayor = suma_grupo.idxmax()
print("Producto con mayor demanda identificado (ID):", mayor)

# 5. Generación de Reporte Visual e Integración de Metadatos
# Se inicializa y configura el lienzo del gráfico antes de la exportación
plt.figure(figsize=(10, 6))
suma_grupo.plot(kind="bar", color="skyblue", edgecolor="black")

# Definición de etiquetas organizacionales para el reporte gerencial
plt.title("Volumen de Ventas Totales por Producto Comercial", fontsize=14, fontweight="bold")
plt.xlabel("Identificador de Producto", fontsize=12)
plt.ylabel("Cantidad de Unidades Vendidas", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# 6. Exportación automatizada del entregable a la carpeta de resultados
plt.tight_layout()
plt.savefig(ruta_grafico, dpi=300)
print(f"Reporte visual exportado correctamente en: {ruta_grafico}")

# 7. Despliegue en el entorno virtual / local
plt.show()