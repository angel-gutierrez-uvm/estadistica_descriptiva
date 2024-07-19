#
# EQUIPO 10 - ESTADISTICA DESCRIPTIVA
# ¿Cuál es el tiempo promedio que los hombres dedican a la lectura? ¿y las mujeres?
#

import pandas as pd

file = "../U1_Datos_PIE1.xlsx"
xls = pd.ExcelFile(file)
df = pd.read_excel(file, sheet_name="Hoja1")

# Se tiene que convertir, de lo contrario no se puede hacer calculo y arroja -> TypeError: unsupported operand type(s) for +: 'datetime.time' and 'datetime.time'
df['Horas de Lectura'] = df['Horas de Lectura'].apply(lambda x: pd.to_timedelta(str(x)))

# Agregamos los filtros por sexo
men = df[df['Sexo'] == 'Varón']
women = df[df['Sexo'] == 'Mujer']

# Sacamos promedio
avg_reading_men = men['Horas de Lectura'].mean()
avg_reading_women = women['Horas de Lectura'].mean()

# Quitamos milisegundos para que sea mas presentable (solo horas, minutos y segundos)
average_reading_men_str = str(avg_reading_men).split(' ')[-1].split('.')[0]
average_reading_women_str = str(avg_reading_women).split(' ')[-1].split('.')[0]

reading_comparison = pd.DataFrame({
    'Sexo': ['Varón', 'Mujer'],
    'Promedio Horas de Lectura': [average_reading_men_str, average_reading_women_str]
})

# Presentamos datos
print(reading_comparison)