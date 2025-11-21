import pandas as pd

def percentiles(archivo,columna):
    try:
        df = pd.read_csv(archivo)
        if columna not in df.columns:
            print("Error al procesar la columna")
            return None
        p25 = df[columna].quantile(0.25)
        p50 = df[columna].quantile(0.50)
        p75 = df[columna].quantile(0.75)
        p90 = df[columna].quantile(0.90)

        return round(p25, 2), round(p50, 2), round(p75, 2)

    except:
        j=print("Error no existe la columna")
        return j




def promedios(n, c):
    try:

        df = pd.read_csv(n)

        if c not in df.columns:
            print("No existe la columna")
            return None
        
        prom = df[c].mean()
        return prom
    
    except FileNotFoundError:
        print("No existe el archivo")

import pandas as pd
import numpy as np


def desviacion(nombre_archivo, nombre_columna):
    try:
        try:
            df = pd.read_csv(nombre_archivo, encoding='utf-8')
        except:
            df = pd.read_csv(nombre_archivo, encoding='latin-1')
        df.columns = df.columns.str.strip()
        if nombre_columna not in df.columns:
            coldis = list(df.columns)
            return f'No existe la columna: {nombre_columna}. Columnas disponibles: {coldis}'
        desv_std = df[nombre_columna].std()
        
        return desv_std
        
    except Exception as e:
        return f'Error: {str(e)}'