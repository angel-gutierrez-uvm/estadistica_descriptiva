import pandas as pd

# Cargar el nuevo archivo proporcionado
file_path_new_sample = '../../muestra_aleatoria_76.xlsx'
data_sample_new = pd.read_excel(file_path_new_sample)

# Función para convertir el formato de tiempo (hh:mm:ss) a horas
def time_to_hours(time_str):
    if pd.isna(time_str):
        return None
    h, m, s = map(int, time_str.split(':'))
    return h + m / 60 + s / 3600

# Aplicar la conversión a las columnas de interés
data_sample_new['Horas de televisión'] = data_sample_new['Horas de televisión'].apply(time_to_hours)
data_sample_new['Horas de Lectura'] = data_sample_new['Horas de Lectura'].apply(time_to_hours)
data_sample_new['Horas dedicadas a alguna otra actividad'] = data_sample_new['Horas dedicadas a alguna otra actividad'].apply(time_to_hours)

# Filtrar las columnas de interés y agrupar por 'Sexo'
grouped_data = data_sample_new.groupby('Sexo')[['Edad', 'Horas de televisión', 'Horas de Lectura', 'Horas dedicadas a alguna otra actividad']]

# Calcular las estadísticas por grupo (por sexo)
summary_statistics_by_sex = grouped_data.agg([
    ('Media', 'mean'),
    ('Rango', lambda x: x.max() - x.min()),
    ('Varianza', 'var'),
    ('Desviación Típica', 'std')
])

# Aplanar el MultiIndex en las columnas para facilitar el acceso y mejorar la legibilidad
summary_statistics_by_sex.columns = [f'{stat} ({col})' for col, stat in summary_statistics_by_sex.columns]

# Reemplazar los nombres de las columnas para que sean más legibles
summary_statistics_by_sex.columns = summary_statistics_by_sex.columns.str.replace('Edad', 'Edad')
summary_statistics_by_sex.columns = summary_statistics_by_sex.columns.str.replace('Horas de televisión', 'Horas de TV')
summary_statistics_by_sex.columns = summary_statistics_by_sex.columns.str.replace('Horas de Lectura', 'Horas de Lectura')
summary_statistics_by_sex.columns = summary_statistics_by_sex.columns.str.replace('Horas dedicadas a alguna otra actividad', 'Horas en otra actividad')

print(summary_statistics_by_sex)