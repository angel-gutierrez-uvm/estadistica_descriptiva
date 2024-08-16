import pandas as pd

# Cargar el archivo Excel
file_path = '../U4_Datos_PIE2.xlsx'
data = pd.read_excel(file_path)

# Seleccionar 76 registros aleatorios
random_sample = data.sample(n=76, random_state=42)

# Guardar los registros aleatorios en un nuevo archivo
output_path = '../muestra_aleatoria_76.xlsx'
random_sample.to_excel(output_path, index=False)

output_path
