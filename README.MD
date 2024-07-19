# Punto 2
## Realiza una tabla de frecuencias para el rubro sexo, situación laboral y edad.

### Sexo - Codigo: punto2/conteo_sexo.py
| Sexo  | Frecuencia |
|-------|------------|
| Varón | 183        |
| Mujer | 167        |
| Total | 350        |

### Situacion Laboral - Codigo punto2/conteo_laboral.py
| Situación laboral | Frecuencia |
|-------------------|------------|
| Ocupado           | 127        |
| Desempleado       | 116        |
| Inactivo          | 107        |
| Total             | 350        |

### Edad - Codigo punto2/conteo_edad.py
| Edad | Frecuencia |
|------|------------|
| 45   | 17         |
| 38   | 14         |
| 52   | 13         |
| 57   | 13         |
| 34   | 13         |
| 49   | 13         |
| 21   | 12         |
| 40   | 11         |
| 47   | 11         |
| 55   | 11         |
| 43   | 10         |
| 46   | 10         |
| 36   | 10         |
| 23   | 10         |
| 31   | 10         |
| 26   | 10         |
| 53   | 10         |
| 24   | 9          |
| 27   | 9          |
| 41   | 9          |
| 59   | 9          |
| 37   | 9          |
| 50   | 8          |
| 28   | 8          |
| 25   | 8          |
| 29   | 7          |
| 60   | 7          |
| 48   | 7          |
| 51   | 7          |
| 35   | 6          |
| 58   | 6          |
| 32   | 5          |
| 30   | 5          |
| 42   | 5          |
| 44   | 5          |
| 56   | 5          |
| 33   | 4          |
| 54   | 4          |
| 20   | 4          |
| 39   | 3          |
| 22   | 3          |
| Total | 350       |

# Punto 3
## Genera una tabla agrupando valores (realiza 5 grupos de edad) para que puedas generar a partir de ella un histograma. - Codigo: punto3/tabla_valores.py

| Edad Grupo | Frecuencia |
|------------|------------|
| 20-29      | 80         |
| 30-39      | 79         |
| 40-49      | 98         |
| 50-59      | 86         |
| 60-69      | 7          |


# Punto 4
## Con base en lo realizado anteriormente contesta las siguientes preguntas:

a. **¿Cuál es el tamaño de la muestra?** 350 encuestados

b. **¿Se aplicó la encuesta a más hombres o mujeres?** Tomando en cuenta los datos del punto 2, especificamente el codigo *conteo_sexo.py*, la frecuencia indica que fueron los hombres con 183 encuestados

c. **¿Cuál es el tiempo promedio que los hombres dedican a la lectura? ¿y las mujeres?** Los hombres, con 1 hora, 53 minutos y 46 segundos - Codigo: punto4/conteo_sexo_lectura.py

| Sexo  | Promedio Horas de Lectura |
|-------|----------------------------|
| Varón | 01:53:46                   |
| Mujer | 01:51:27                   |

d. **De los encuestados ¿quiénes ven más televisión los hombres o las mujeres desempleados?** Los hombres, con 1 hora, 58 minutos y 29 segundos - Codigo: punto4/conteo_desempleo_tv.py

| Sexo  | Horas de TV |
|-------|-------------|
| Varón | 01:58:29    |
| Mujer | 02:17:31    |

e. **¿La edad es relevante para dedicar más tiempo a la lectura?** Si, utilizando el codigo punto4/conteo_edad_lectura.py se puede apreciar que el rango de edad para dedicar mas tiempo a la lectura va de los 20 a los 29 años.

| Edad Grupo | Horas de Lectura |
|------------|------------------|
| 20-29      | 02:02:18         |
| 30-39      | 01:45:50         |
| 40-49      | 01:51:33         |
| 50-59      | 01:50:41         |
| 60-69      | 01:59:23         |