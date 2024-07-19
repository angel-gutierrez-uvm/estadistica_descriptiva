#
# EQUIPO 10 - ESTADISTICA DESCRIPTIVA
# Realiza una tabla de frecuencias para el rubro sexo, situación laboral y edad.
#


import pandas as pd

file = "../U1_Datos_PIE1.xlsx"
xls = pd.ExcelFile(file)
df = pd.read_excel(file, sheet_name="Hoja1")

# Frecuencia para el Sexo
# Retorna el total por sexo y el conteo
gender_freq = df["Sexo"].value_counts().reset_index()
gender_freq.columns = ["Sexo", "Frecuencia"]

# Agrego el total por si acaso
gender_frequency = pd.concat([gender_freq, pd.DataFrame({'Sexo': ['Total'], 'Frecuencia': [gender_freq['Frecuencia'].sum()]})], ignore_index=True)

print("Sexo")
print(gender_frequency)