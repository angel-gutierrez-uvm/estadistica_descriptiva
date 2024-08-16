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

# Filtrar las columnas de interés ahora con datos numéricos
filtered_data_converted_hours = data_sample_new[['Edad', 'Horas de televisión', 'Horas de Lectura', 'Horas dedicadas a alguna otra actividad']].apply(pd.to_numeric, errors='coerce')

# Calcular estadísticas descriptivas para las columnas numéricas seleccionadas
mean_values_converted_hours = filtered_data_converted_hours.mean()
range_values_converted_hours = filtered_data_converted_hours.max() - filtered_data_converted_hours.min()
variance_values_converted_hours = filtered_data_converted_hours.var()
std_dev_values_converted_hours = filtered_data_converted_hours.std()

# Organizar los resultados en un DataFrame
summary_statistics_converted_hours = pd.DataFrame({
    'Media': mean_values_converted_hours,
    'Rango': range_values_converted_hours,
    'Varianza': variance_values_converted_hours,
    'Desviación Típica': std_dev_values_converted_hours
})

# Mostrar el DataFrame resultante
print(summary_statistics_converted_hours)