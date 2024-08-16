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

# Filtrar los datos para seleccionar solo los "Ocupados"
ocupados_data = data_sample_new[data_sample_new['Situación laboral'] == 'Ocupado']

# Filtrar las columnas de interés
filtered_data_ocupados = ocupados_data[['Edad', 'Horas de televisión', 'Horas de Lectura', 'Horas dedicadas a alguna otra actividad']]

# Calcular las estadísticas descriptivas para los ocupados
mean_values_ocupados = filtered_data_ocupados.mean()
range_values_ocupados = filtered_data_ocupados.max() - filtered_data_ocupados.min()
variance_values_ocupados = filtered_data_ocupados.var()
std_dev_values_ocupados = filtered_data_ocupados.std()

# Organizar los resultados en un DataFrame
summary_statistics_ocupados = pd.DataFrame({
    'Media': mean_values_ocupados,
    'Rango': range_values_ocupados,
    'Varianza': variance_values_ocupados,
    'Desviación Típica': std_dev_values_ocupados
})

# Mostrar el DataFrame resultante
print(summary_statistics_ocupados)