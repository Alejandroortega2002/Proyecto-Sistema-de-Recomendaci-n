import pandas as pd
import pandas as pd

def eliminar_datos_filas(archivo_csv):
    # Leer el archivo CSV
    df = pd.read_csv(archivo_csv)

    # Eliminar los datos de las filas (mantener las columnas)
    df.loc[:, :] = None  # Establecer todos los valores de las filas a None (vacío)

    # Guardar el DataFrame actualizado en el archivo CSV
    df.to_csv(archivo_csv, index=False)
    print("Todos los datos dentro de las filas han sido eliminados.")

# Llamar a la función para eliminar los datos en el archivo 'usuarios.csv'
archivo_csv = 'usuarios.csv'
eliminar_datos_filas(archivo_csv)
