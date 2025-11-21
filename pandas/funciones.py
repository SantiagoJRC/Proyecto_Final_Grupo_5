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