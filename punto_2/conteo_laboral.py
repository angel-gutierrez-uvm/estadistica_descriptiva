#
# EQUIPO 10 - ESTADISTICA DESCRIPTIVA
# REALIZA UNA TABLA DE FRECUENCIAS PARA EL RUBRO SEXO, SITUACION LABORAL Y EDAD
#

import pandas as pd

file = "../U1_Datos_PIE1.xlsx"
xls = pd.ExcelFile(file)
df = pd.read_excel(file, sheet_name="Hoja1")

# Frecuencia para la situacion laboral
# Retorna el total por situacion laboral y el conteo
job_status_freq = df["Situación laboral"].value_counts().reset_index()
job_status_freq.columns = ["Situación laboral", "Frecuencia"]

# Agrego conteo total para validacion
job_status_freq = pd.concat([job_status_freq, pd.DataFrame({'Situación laboral': ['Total'], 'Frecuencia': [job_status_freq['Frecuencia'].sum()]})], ignore_index=True)

print("Situacion Laboral: ")
print(job_status_freq)