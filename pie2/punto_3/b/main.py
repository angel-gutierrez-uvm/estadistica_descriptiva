import pandas as pd

# Cargar el archivo Excel original
file_path_original = '../../U4_Datos_PIE2.xlsx'
data_original = pd.read_excel(file_path_original)

# Cargar la muestra generada
file_path_sample = '../../muestra_aleatoria_76.xlsx'
data_sample = pd.read_excel(file_path_sample)

# Calcular el tamaño de la población y el tamaño de la muestra
population_size = len(data_original)
sample_size = len(data_sample)

# Calcular la proporción de la muestra respecto a la población en porcentaje
sample_proportion_percentage = (sample_size / population_size) * 100

# Mostrar la proporción en porcentaje
print(f"La proporción de la población que representa el tamaño de la muestra es: {sample_proportion_percentage:.2f}%")