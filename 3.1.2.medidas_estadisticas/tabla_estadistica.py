#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

DATOS = pd.read_csv("armamex.csv")
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
    val_intervalo = 25
    x = (min(piezas)**2)//2 + max(piezas) / val_intervalo
    aux_1, aux_2 = min(piezas), min(piezas) + x
    aux_dict = {}
    for i in range(val_intervalo):
        aux_dict[i] = [aux_1, aux_2]
        aux_1 = aux_2
        aux_2 = aux_2 + x

    print(aux_dict)

get_column_No_piezas()