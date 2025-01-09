import pandas as pd

ruta_csv = "peliculas_final.csv"
peliculas_df = pd.read_csv(ruta_csv)
print(peliculas_df.columns)  # Esto mostrará todos los nombres de columnas
