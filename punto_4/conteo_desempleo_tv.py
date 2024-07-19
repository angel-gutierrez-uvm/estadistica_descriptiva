#
# EQUIPO 10 - ESTADISTICA DESCRIPTIVA
# De los encuestados ¿quiénes ven más televisión los hombres o las mujeres desempleados?
#

import pandas as pd

file = "../U1_Datos_PIE1.xlsx"
xls = pd.ExcelFile(file)
df = pd.read_excel(file, sheet_name="Hoja1")

# Se tiene que convertir, de lo contrario no se puede hacer calculo y arroja -> TypeError: unsupported operand type(s) for +: 'datetime.time' and 'datetime.time'
df["Horas de televisión"] = df["Horas de televisión"].apply(lambda x: pd.to_timedelta(str(x)))

# Agregamos los filtros solo para obtener los desempleados por sexo
men = df[(df["Sexo"] == "Varón") & (df["Situación laboral"] == "Desempleado")]
women = df[(df["Sexo"] == "Mujer") & (df["Situación laboral"] == "Desempleado")]

# Sacamos promedio por sexo
avg_tv_men = men["Horas de televisión"].mean()
avg_tv_women = women["Horas de televisión"].mean()

# Quitamos milisegundos para que sea mas presentable (solo horas, minutos y segundos)
avg_tv_men = str(avg_tv_men).split(' ')[-1].split('.')[0]
avg_tv_women = str(avg_tv_women).split(' ')[-1].split('.')[0]

comparison = pd.DataFrame({
    "Sexo": ["Varón", "Mujer"],
    "Horas de TV": [avg_tv_men, avg_tv_women]
})

# Mostramos datos
print(comparison)