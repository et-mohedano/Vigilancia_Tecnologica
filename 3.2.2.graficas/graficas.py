#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:42:04 2022

@author: maximiliano
"""

import pandas as pd
import matplotlib.pyplot as plt
import operator

colors  = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#ffffb6','#ffd1df','#017a79','#ceb301','#516572','#e17701','#d5869d','#82cbb2']
colors2 = ['#017a79','#ceb301','#516572','#e17701','#d5869d','#82cbb2','#cf524e','#cb0162','#cb6843','#ffb2d0','#e50000','#c65102']
colors3 = ['#cf524e','#cb0162','#cb6843','#ffb2d0','#e50000','#c65102','#ff9999','#66b3ff','#99ff99','#ffcc99','#ffffb6','#ffd1df']
color='#feffca'
color2='#ceb301'
color3='#e50000'
color4='#516572'

def listaPalabrasDicFrec(words):
    words_found = {}
    for word in words:
        if word not in words_found:
            words_found[word] = 1
        else:
            words_found[word] += 1
    wors_found_sort = dict(
        sorted(words_found.items(), key=operator.itemgetter(1), reverse=True)
    )
    return wors_found_sort
 
datos = pd.read_csv("armamex.csv")
df=pd.DataFrame(datos)
aux1 = df['Pais_origen_empresa']
df_fixed = listaPalabrasDicFrec(aux1)
df_fixed["otros"] = 0
for key in list(df_fixed):
    if df_fixed[key] < 170:
        df_fixed["otros"] += df_fixed[key]
        del df_fixed[key]

plt.pie(df_fixed.values(), labels=df_fixed.keys(), autopct='%1.1f%%', colors=colors2, textprops=dict(color='black'), labeldistance=None) 
plt.legend(bbox_to_anchor=(1.5, .5), loc='center right')
plt.title('Principales países proveedores de armas a México', fontweight='bold' , loc='left')
plt.show()

aux1 = df['Marca']
df_fixed = listaPalabrasDicFrec(aux1)
df_fixed["otros"] = 0
for key in list(df_fixed):
    if df_fixed[key] < 280:
        df_fixed["otros"] += df_fixed[key]
        del df_fixed[key]
        
plt.pie(df_fixed.values(), labels=df_fixed.keys(), autopct='%1.1f%%', colors=colors, textprops=dict(color='black'), labeldistance=None) 
plt.legend(bbox_to_anchor=(1.5, .5), loc='center right')
plt.title('Principales marcas de armas adquiridas en México', fontweight='bold' , loc='left')
plt.show()

aux1 = df['Tipo']
df_fixed = listaPalabrasDicFrec(aux1)
df_fixed["otros"] = 0
for key in list(df_fixed):
    if df_fixed[key] < 280:
        df_fixed["otros"] += df_fixed[key]
        del df_fixed[key]
        
plt.pie(df_fixed.values(), labels=df_fixed.keys(), autopct='%1.1f%%', colors=colors3, textprops=dict(color='black'), labeldistance=None) 
plt.legend(bbox_to_anchor=(1.5, .5), loc='center right')
plt.title('Tipo de armas adquiridas en México', fontweight='bold' , loc='center')
plt.show()

df.plot.scatter(x="Estado", color=color2, y="Pais_origen_empresa", alpha=0.1)
plt.title("Países proveedores de armas por estado", fontweight='bold')
plt.xticks(rotation=90, ha='right')
plt.xlabel("Estado de la República Mexicana")
plt.ylabel("País proveedor")
plt.show()

df.plot.scatter(x="Estado",color=color3, y="Tipo", alpha=0.1)
plt.title("Tipos de arma adquiridos por estado de la República Mexicana", fontweight='bold')
plt.xticks(rotation=90, ha='right')
plt.xlabel("Estado de la República Mexicana")
plt.ylabel("Tipo de arma")
plt.show()

df.plot.scatter(x="Estado", y="Ano",color=color4, alpha=0.01)
plt.title("Frecuencia de adquisición de armas por año", fontweight='bold')
plt.xticks(rotation=90, ha='right')
plt.xlabel("Estado de la República Mexicana")
plt.ylabel("Año de adquisición")
plt.show()