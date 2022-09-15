#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:42:11 2022

@author: maximiliano
"""

import pandas as pd

datos = pd.read_csv("armamex.csv")
print(datos.describe())