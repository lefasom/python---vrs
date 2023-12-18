import pandas as pd

def convertir_csv_a_excel(ruta_csv, ruta_excel):
    # Lee el archivo CSV
    df = pd.read_csv(ruta_csv)

    # Convierte y guarda como archivo de Excel
    df.to_excel(ruta_excel, index=False)

# Ejemplo de uso
ruta_csv = 'archivos\\datos.csv'
ruta_excel = 'archivos\\resultado.xlsx'

convertir_csv_a_excel(ruta_csv, ruta_excel)
