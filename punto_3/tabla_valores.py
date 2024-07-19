#
# EQUIPO 10 - ESTADISTICA DESCRIPTIVA
# Genera una tabla agrupando valores (realiza 5 grupos de edad) para que puedas generar a partir de ella un histograma.
#

import pandas as pd

file = "../U1_Datos_PIE1.xlsx"
xls = pd.ExcelFile(file)
df = pd.read_excel(file, sheet_name="Hoja1")

# Se define rangos de edad
age_bins = [20, 30, 40, 50, 60, 70]

# Se agregan los labels para cada rango
age_labels = ["20-29", "30-39", "40-49", "50-59", "60-69"]

# Se crea el segmento y se agregan los bins y labels
df["Edad Grupo"] = pd.cut(df["Edad"], bins=age_bins, labels=age_labels, right=False)

# Se hace el conteo y ordenado de datos (menor a mayor)
age_group_freq = df["Edad Grupo"].value_counts().sort_index().reset_index()

# Se agrega las columnas
age_group_freq.columns = ["Edad Grupo", "Frecuencia"]

# Se presenta la tabla
print(age_group_freq)