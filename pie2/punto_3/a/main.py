import pandas as pd

# Cargar la muestra generada
file_path_sample = '../../muestra_aleatoria_76.xlsx'
data_sample = pd.read_excel(file_path_sample)

# Definir los rangos de edad
bins = [0, 18, 30, 40, 50, 60, 100]
labels = ['0-18', '19-30', '31-40', '41-50', '51-60', '61+']

# Crear una nueva columna con los rangos de edad
data_sample['Rango de Edad'] = pd.cut(data_sample['Edad'], bins=bins, labels=labels, right=False)

# Contar la cantidad de registros por cada rango de edad
age_range_counts = data_sample['Rango de Edad'].value_counts()

# Calcular la proporción de la muestra en cada rango de edad
proportion_by_age_range = age_range_counts / len(data_sample)

# Mostrar la proporción por rango de edad en un formato más limpio
print("Proporción de la muestra por rango de edad:")
print(f"{'Rango de Edad':<10} {'Proporción':>12}")
print("-" * 25)
for age_range, proportion in proportion_by_age_range.items():
    print(f"{age_range:<10} {proportion:.6f}")