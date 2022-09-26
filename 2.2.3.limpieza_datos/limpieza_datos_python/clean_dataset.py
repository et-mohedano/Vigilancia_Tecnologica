# Cargar liberias
# Libreria para manipular dataframes
import pandas as pd
#Libreria para graficar
import matplotlib.pyplot as plt
# Libreria para control de alertas
import warnings
# Libreria para indices en diccionarios
import operator
# Libreria de utilidades para fechas
import calendar
# Evitar warmings
warnings.filterwarnings('ignore')

# Leer Dataframe
dataset=pd.read_csv("Armas_Policias_Mexico.csv")
# Mostrar dataframe
print(dataset)
# Mostrar columnas de dataframe
print(dataset.head)
# Mostrar info de dataframe
dataset.info()
# Mostrar cantidad de nulos del dataframe
dataset.isnull().sum()
# Seleccionar dimensiones
dataset1=dataset[['Estado','Fecha','Mes','Ano','Marca','Pais_origen_empresa','No_piezas','Costo_Pesos_Mex','Calibre','Tipo']]
# Mostrar nuevo dataframe
print(dataset1)
# Mostrar cantidad de nulos del nuevo dataframe
dataset1.isnull().sum()
# Eliminar registros nulos del dataframe
dataset1.dropna()
# Mostrar cantidad de nulos del dataframe
dataset1.isnull().sum().sum()
# Mostrar información descriptiva del dataframe
dataset1.describe()
# Capturar nulos en lista
null_columns=dataset1.columns[dataset1.isnull().any()]
# Mostrar nulos enlistados en el dataframe nuevo
print(dataset1[null_columns].isnull().sum())
# Limpiar nulos de segundo dataframe
dataset2=dataset1.dropna(how='any')
# Mostrar información descriptiva del segundo dataframe
dataset2.describe()
# Mostrar cantidad de nulos del segundo dataframe
dataset2.isnull().sum().sum()
# Mostrar segundo dataframe
print(dataset2)
# Crear dataframe con correlaciones
dataset2_corr=dataset2.corr()
# Mostrar correlaciones
print(dataset2_corr)
# Definir función para cambiar numero por nombre de mes
def castMes(diccionario):
    # Definir diccionario auxiliar
    dict_aux = {}
    # Recorrer llaves del diccionario (las llaves son los numeros de los meses)
    for clave in diccionario:
        # Agregar al diccionario auxiliar el valor del nombre del mes según el número
        dict_aux[calendar.month_abbr[int(clave)]] = diccionario[clave]
    # Retornar diccionario arreglado
    return dict_aux
# Definir función para contar registros en un diccionario según sus categorías
def dictMesesCostos(registros, columna):
    # C}Definir dccionario de meses
    meses = {}
    # Recorrer registros de categorias 
    for indice, mes in enumerate(registros):
        # Cambiar valores con comas por enteros
        dataset2[columna][indice] = int(dataset2[columna][indice].replace(',', ''))
        # Agregar meses al diccionario con su valor correspondiente
        if mes not in meses:
            meses[mes] = dataset2[columna][indice]
        # Sumar al valor del mes la siguiente cantidad
        else:
            meses[mes] += dataset2[columna][indice]
    # Ordenar registros según el mes
    mes_ordenados = dict(
        sorted(meses.items(), key=operator.itemgetter(0), reverse=False)
    )
    # Castear el número a nombre del mes
    mes_ordenados = castMes(mes_ordenados)
    # Retornar diccionario
    return mes_ordenados
# Arreglar indices del dataframe (Después de correciones)
dataset2=dataset2.reset_index(drop=True)
# Obtener el diccionario de meses y costos
df_fixed = dictMesesCostos(registros=dataset2["Mes"], columna="Costo_Pesos_Mex")
# MOstrar diccionario de meses y costos
print(df_fixed)
# Definir gráfica de barras
plt.bar(range(len(df_fixed)), list(df_fixed.values()), tick_label=list(df_fixed.keys()))
# Agregar titulo
plt.title("Costos de armas por mes")
# Label para X
plt.xlabel("Meses")
# Label para Y
plt.ylabel("Costos")
# Mostrar gráfica
plt.show()