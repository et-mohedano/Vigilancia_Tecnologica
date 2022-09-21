#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

DATOS = pd.read_csv("Armas_Policias_Mexico_clean.csv")
print(DATOS.columns)

def get_column_Estado():
    """"""
    global DATOS
    piezas = DATOS['Estado']
    observacion = list(set(piezas))
    observacion.sort()
    frecuencia_absoluta = {i:len([value for value in piezas if i == value]) for i in observacion}
    frecuencia_relativa = {val:(frecuencia_absoluta[val]*100)/len(piezas) for val in frecuencia_absoluta}
    moda = {i for i in frecuencia_absoluta if frecuencia_absoluta[i]==max(frecuencia_absoluta.values())}
    data = pd.DataFrame({'Estado':list(observacion), 'Frecuencia_absoluta': frecuencia_absoluta.values(), 'Frecuencia_relativa': frecuencia_relativa.values()})
    
    print(data)
    print('\nModa: ', moda)


def get_column_Pais_origen_empresa():
    """"""
    global DATOS
    piezas = DATOS['Pais_origen_empresa']
    observacion = list(set(piezas))
    observacion.remove('n.a.')
    frecuencia_absoluta = {i:len([value for value in piezas if i == value]) for i in observacion}
    frecuencia_relativa = {val:(frecuencia_absoluta[val]*100)/len(piezas) for val in frecuencia_absoluta}
    moda = {i for i in frecuencia_absoluta if frecuencia_absoluta[i]==max(frecuencia_absoluta.values())}
    data = pd.DataFrame({'País':list(observacion), 'Frecuencia_absoluta': frecuencia_absoluta.values(), 'Frecuencia_relativa': frecuencia_relativa.values()})
    
    print(data)
    print('\nModa: ', moda)


def get_column_Calibre():
    """"""
    global DATOS
    piezas = DATOS['Calibre']
    observacion = list(set(piezas))
    frecuencia_absoluta = {i:len([value for value in piezas if i == value]) for i in observacion}
    frecuencia_relativa = {val:(frecuencia_absoluta[val]*100)/len(piezas) for val in frecuencia_absoluta}
    moda = {i for i in frecuencia_absoluta if frecuencia_absoluta[i]==max(frecuencia_absoluta.values())}
    data = pd.DataFrame({'Calibre':list(observacion), 'Frecuencia_absoluta': frecuencia_absoluta.values(), 'Frecuencia_relativa': frecuencia_relativa.values()})
    
    print(data)
    print('\nModa: ', moda)


def get_column_Tipo():
    """"""
    global DATOS
    piezas = DATOS['Tipo']
    observacion = list(set(piezas))
    frecuencia_absoluta = {i:len([value for value in piezas if i == value]) for i in observacion}
    frecuencia_relativa = {val:(frecuencia_absoluta[val]*100)/len(piezas) for val in frecuencia_absoluta}
    moda = {i for i in frecuencia_absoluta if frecuencia_absoluta[i]==max(frecuencia_absoluta.values())}
    data = pd.DataFrame({'Tipo':list(observacion), 'Frecuencia_absoluta': frecuencia_absoluta.values(), 'Frecuencia_relativa': frecuencia_relativa.values()})
    
    print(data)
    print('\nModa: ', moda)


def get_column_Marca():
    """"""
    global DATOS
    piezas = DATOS['Marca']
    observacion = list(set(piezas))
    observacion.sort(); observacion.remove('n.a.')
    frecuencia_absoluta = {i:len([value for value in piezas if i == value]) for i in observacion}
    frecuencia_relativa = {val:(frecuencia_absoluta[val]*100)/len(piezas) for val in frecuencia_absoluta}
    moda = {i for i in frecuencia_absoluta if frecuencia_absoluta[i]==max(frecuencia_absoluta.values())}
    data = pd.DataFrame({'Marca':list(observacion), 'Frecuencia_absoluta': frecuencia_absoluta.values(), 'Frecuencia_relativa': frecuencia_relativa.values()})
    
    print(data)
    print('\nModa: ', moda)


def get_column_No_piezas():
    """Working ..."""
    global DATOS
    piezas = DATOS['No_piezas']
    value = piezas;value.dropna(inplace=True)
    val_intervalo = 25
    x = (min(piezas)**2)//2 + max(piezas) / val_intervalo
    aux_1, aux_2 = min(piezas), min(piezas) + x
    aux_dict = []
    for i in range(val_intervalo):
        aux_dict.append([aux_1, aux_2])
        aux_1 = aux_2
        aux_2 = aux_2 + x
    frecuencia_absoluta = {int((val[0] + val[1])/2): len([i for i in piezas if val[1] > i >= val[0]]) for val in aux_dict}
    frecuencia_relativa = {val: (frecuencia_absoluta[val]*100)/len(piezas) for val in frecuencia_absoluta}
    moda = {i for i in frecuencia_absoluta if frecuencia_absoluta[i]==max(frecuencia_absoluta.values())}
    media = sum(value) / len(piezas)

    data = pd.DataFrame({'Rango':aux_dict, 'Frecuencia_absoluta': frecuencia_absoluta.values(), 'Frecuencia_relativa': frecuencia_relativa.values()})
    
    print(data)
    print('\nModa: ', moda)
    print('Media: ', media)


def get_column_Costo_Pesos_Mex():
    """Working ..."""
    global DATOS
    piezas = DATOS['Costo_Pesos_Mex']
    piezas.dropna(inplace=True)
    clean_piezas = list(map(lambda x : int(str(x).replace(',','')),piezas))
    val_intervalo = 25
    x = min(clean_piezas) + max(clean_piezas) / val_intervalo
    
    aux_1, aux_2 = min(clean_piezas), min(clean_piezas) + x
    aux_dict = []
    for i in range(val_intervalo):
        aux_dict.append([aux_1, aux_2])
        aux_1 = aux_2
        aux_2 = aux_2 + x
    frecuencia_absoluta = {int((val[0] + val[1])/2): len([i for i in clean_piezas if val[1] > i >= val[0]]) for val in aux_dict}
    frecuencia_relativa = {val: (frecuencia_absoluta[val]*100)/len(clean_piezas) for val in frecuencia_absoluta}
    moda = {i for i in frecuencia_absoluta if frecuencia_absoluta[i]==max(frecuencia_absoluta.values())}
    media = sum(clean_piezas) / len(clean_piezas)

    data = pd.DataFrame({'Rango':aux_dict, 'Frecuencia_absoluta': frecuencia_absoluta.values(), 'Frecuencia_relativa': frecuencia_relativa.values()})
    
    print(data)
    print('\nModa: ', moda)
    print('Media: ', media)

get_column_Costo_Pesos_Mex()