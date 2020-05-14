# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 01:48:52 2020

@author: Developed
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('eda_data.csv')

# Traer solo las columnas adecuadas.
df.columns[['Ratings', 'Size', 'Type of ownership', 'Industry', 'Sector', 'Revenue', 'num_comp', 'hourly', 'employer_provided', 'job_state', 'some_state','age', 'python_yn', 'spark', 'R_yn', 'job_simp', 'seniority']]


# Traer datos ficticios
# Modelado de prueba
# Metodo Regresiòn lineal
# Metodo Regresion de laso
# Metodo aleatorio
# Afinar modelos GribsearchCV
# prueba de ensamblaje

