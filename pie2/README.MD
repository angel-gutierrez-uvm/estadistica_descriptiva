# Punto 1
Calcula el tamaño de la muestra que se puede estudiar si se requiere tener un margen de error de 10% y un nivel de confianza de 95%. Puedes utilizar la siguiente herramienta: (https://www.corporacionaem.com/tools/calc_muestras.php)

**Recurso**: punto_1/Muestra.png

# Punto 2
*Según lo obtenido anteriormente selecciona, la muestra de manera aleatoria con la que
trabajarás (utiliza Minitab para obtener los datos de tu muestra), utiliza los datos del archivo*
U4_Datos_PIE2.xlsx

**Recurso**: punto_2/main.py
<br>

# Punto 3
*Ya que conoces el tamaño de la muestra y los datos que la conforman, determina:*

a) La probabilidad de que cada uno de los encuestados en la población sean elegidos
parte de la muestra.

**Recurso**: punto_3/a/main.py
<br>
**Resultado**:
| Rango de Edad | Proporción |
|---------------|------------|
| 51-60         | 0.315789   |
| 41-50         | 0.276316   |
| 19-30         | 0.236842   |
| 31-40         | 0.144737   |
| 61+           | 0.026316   |
| 0-18          | 0.000000   |


b) ¿Qué proporción de la población representa el tamaño de la muestra que has
obtenido?

**Recurso**: punto_3/b/main.py
<br>
**Resultado**: 21.71%

d) Calcula Media, rango, varianza y desviación típica de las variables de la muestra

**Recurso**: punto_3/d/main.py
<br>
**Resultado**:
| Edad                                     | Media     | Rango     | Varianza  | Desviación Típica |
|------------------------------------------|-----------|-----------|-----------|-------------------|
| **Edad**                                 | 41.907895 | 39.000000 | 137.684737 | 11.733914          |
| **Horas de televisión**                  | 2.134825  | 3.977500  | 1.444590  | 1.201911           |
| **Horas de Lectura**                     | 1.748001  | 3.876389  | 1.163469  | 1.078642           |
| **Horas dedicadas a alguna otra actividad** | 3.944554  | 7.991667  | 5.286202  | 2.299174           |

e) Calcula Media, rango, varianza y desviación típica de las variables de la muestra por
sexo.

**Recurso**: punto_3/e/main.py
<br>
**Resultado**:
| Sexo   | Media (Edad) | Rango (Edad) | Varianza (Edad) | Rango (Horas en otra actividad) | Varianza (Horas en otra actividad) | Desviación Típica (Horas en otra actividad) |
|--------|--------------|--------------|-----------------|---------------------------------|------------------------------------|--------------------------------------------|
| Mujer  | 41.363636     | 39           | 134.301136      | 7.991667                        | 5.086747                           | 2.255382                                   |
| Varón  | 42.325581     | 39           | 143.129568      | 7.374167                        | 5.543213                           | 2.354403                                   |

f) Calcula Media, rango, varianza y desviación típica de las variables de la muestra para
los ocupados

**Recurso**: punto_3/f/main.py
<br>
**Resultado**:
|                                           | Media     | Rango     | Varianza  | Desviación Típica |
|-------------------------------------------|-----------|-----------|-----------|-------------------|
| **Edad**                                  | 41.666667 | 39.000000 | 171.769231 | 13.106076          |
| **Horas de televisión**                   | 2.136070  | 3.918889  | 1.596437  | 1.263502           |
| **Horas de Lectura**                      | 1.879835  | 3.650556  | 1.408731  | 1.186900           |
| **Horas dedicadas a alguna otra actividad** | 3.924506  | 7.738333  | 6.651695  | 2.579088           |
