"""
Taller Práctico - Módulo 1: Análisis de Datos
UNISANGIL
CODIGO que demuestra el uso básico de la librería pandas
para análisis de datos.
"""

import pandas as pd

# 1. Crear un conjunto de datos de prueba (Diccionario sobre inventario/ventas)
inventario = {
    'Producto': ['Laptop', 'Mouse', 'Monitor', 'Laptop', 'Teclado', 'Monitor', 'Mouse', 'Teclado'],
    'Categoría': ['Cómputo', 'Accesorios', 'Cómputo', 'Cómputo', 'Accesorios', 'Cómputo', 'Accesorios', 'Accesorios'],
    'Ingresos': [1200, 150, 600, 2400, 180, 450, 90, 320],
    'Tienda': ['Sucursal A', 'Sucursal A', 'Sucursal B', 'Sucursal B', 'Sucursal A', 'Sucursal A', 'Sucursal B', 'Sucursal B']
}

# 2. Convertir el diccionario en un DataFrame de Pandas
df_tienda = pd.DataFrame(inventario)

print("--- Vista General del Inventario ---")
print(df_tienda)
print("\n" + "="*40 + "\n")

# 3. Filtrar datos: Mostrar transacciones que generaron más de 500 en ingresos
altos_ingresos = df_tienda[df_tienda['Ingresos'] > 500]
print("--- Transacciones con ingresos mayores a 500 ---")
print(altos_ingresos)
print("\n" + "="*40 + "\n")

# 4. Agrupar datos: Calcular el total de ingresos recaudados por cada producto
ingresos_totales_producto = df_tienda.groupby('Producto')['Ingresos'].sum().reset_index()
print("--- Recaudación total por tipo de producto ---")
print(ingresos_totales_producto)
print("\n" + "="*40 + "\n")

# 5. Análisis estadístico rápido de los ingresos
print("--- Métricas descriptivas de los ingresos ---")
print(df_tienda['Ingresos'].describe())