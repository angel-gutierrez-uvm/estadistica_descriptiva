#
# EQUIPO 10 - ESTADISTICA DESCRIPTIVA
# ¿La edad es relevante para dedicar más tiempo a la lectura?
#

import pandas as pd

file = "../U1_Datos_PIE1.xlsx"
xls = pd.ExcelFile(file)
df = pd.read_excel(file, sheet_name="Hoja1")

# Se tiene que convertir, de lo contrario no se puede hacer calculo y arroja -> TypeError: unsupported operand type(s) for +: 'datetime.time' and 'datetime.time'
df['Horas de Lectura'] = df['Horas de Lectura'].apply(lambda x: pd.to_timedelta(str(x)))

# Se define rangos de edad
age_bins = [20, 30, 40, 50, 60, 70]
age_labels = ['20-29', '30-39', '40-49', '50-59', '60-69']

# Se crea el segmento y se agregan los bins y labels
df['Edad Grupo'] = pd.cut(df['Edad'], bins=age_bins, labels=age_labels, right=False)

# Calculamos el promedio de lectura por grupo de edades
avg_reading_time_by_age_group = df.groupby('Edad Grupo')['Horas de Lectura'].mean()

# Quitamos milisegundos para que sea mas presentable (solo horas, minutos y segundos)
avg_reading_time_by_age_group = avg_reading_time_by_age_group.apply(lambda x: str(x).split(' ')[-1].split('.')[0])

# Se crea la tabla de datos
avg_reading_time_by_age_group = avg_reading_time_by_age_group.reset_index()

# Presentamos datos
print(avg_reading_time_by_age_group)