#
# EQUIPO 10 - ESTADISTICA DESCRIPTIVA
# Realiza una tabla de frecuencias para el rubro sexo, situación laboral y edad.
#

import pandas as pd

file = "../U1_Datos_PIE1.xlsx"
xls = pd.ExcelFile(file)
df = pd.read_excel(file, sheet_name="Hoja1")

age_freq = df["Edad"].value_counts().reset_index()
age_freq.columns = ["Edad", "Frecuencia"]
age_freq = pd.concat([age_freq, pd.DataFrame({'Edad': ['Total'], 'Frecuencia': [age_freq['Frecuencia'].sum()]})], ignore_index=True)

print("Edad: ")
print(age_freq)