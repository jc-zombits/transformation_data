import pandas as pd
from data_validation import transform_data
from db import insert_data

# Cargar el archivo Excel
def load_data(file_path):
    df = pd.read_excel(file_path, engine='openpyxl')  # Asegúrate de usar 'openpyxl' para archivos .xlsx
    return df  # Devuelve un DataFrame directamente

# Función para formatear cada fila según el formato requerido
def format_row(row):
    """
    Formatea una fila del DataFrame en el formato requerido.
    Cada valor es envuelto en comillas simples y la fila completa en paréntesis.
    Si el valor es NaN, lo reemplaza por una cadena vacía.
    """
    formatted_values = [
        f"'{value}'" if isinstance(value, str) else str(value) if pd.notna(value) else "''"
        for value in row
    ]
    return f"({','.join(formatted_values)}),"


# Función principal para procesar y guardar el archivo transformado
def process_and_save(file_path):
    """
    Procesa el archivo Excel, transforma los datos y guarda en un archivo CSV
    con el formato personalizado.
    """
    # Cargar el archivo Excel
    df = load_data(file_path)

    # Aplicar la transformación a todo el DataFrame
    df_transformed = df.apply(transform_data, axis=1)  # Transformar cada fila del DataFrame

    # Crear el archivo de salida en formato CSV
    output_file = 'pqrs_transformed.csv'

    with open(output_file, 'w', encoding='utf-8-sig') as file:
        # Escribir los encabezados (en comillas simples)
        headers = ','.join([f"'{col}'" for col in df_transformed.columns])
        file.write(f"{headers}\n")

        # Formatear y escribir cada fila
        for _, row in df_transformed.iterrows():
            formatted_row = format_row(row)
            file.write(f"{formatted_row}\n")
    
    print(f"Archivo transformado guardado como: {output_file}")

# Código para ejecutar el programa
if __name__ == "__main__":
    file_path = './PQRS.xlsx'  # Cambia a la ruta de tu archivo de Excel
    process_and_save(file_path)
