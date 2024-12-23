# data_validation.py
from datetime import datetime
import pandas as pd

def transform_data(row):
    # Convertir cadenas de texto que son fechas a formato YYYY-MM-DD
    def transform_date(value):
        if isinstance(value, str):
            # Manejar los formatos YYYY/MM/DD o YYYYMMDD
            for fmt in ("%Y/%m/%d", "%Y%m%d"):
                try:
                    return datetime.strptime(value, fmt).strftime('%Y-%m-%d')
                except ValueError:
                    continue
        return value
    
    # Reemplazar valores vacíos por NULL
    def handle_empty(value):
        if isinstance(value, str):
            if not value or value.strip() == "":
                return None  # O el valor que desees cuando la cadena esté vacía
        return value
    
    # Eliminar espacios en blanco innecesarios y normalizar mayúsculas/minúsculas
    def clean_text(value):
        if isinstance(value, str):
            return value.strip().lower()  # Normaliza a minúsculas y quita espacios
        return value

    # Reemplazar valores no numéricos en campos numéricos
    def transform_numeric(value):
        try:
            return int(value)  # Convierte a número entero
        except (ValueError, TypeError):
            return None  # Si no se puede convertir, lo deja en NULL
    
    # Crear un diccionario transformado
    transformed_row = {}
    
    # Recorremos cada columna y la transformamos según corresponda
    for key, value in row.items():
        if key in ["FECHA DE INGRESO", "FECHA DE INGRESO A LA BANDEJA", "FECHA DE EVACUADO DEL DOCUMENTO", "FECHA LIMITE DE RESPUESTA", "FECHA DE RESPUESTA", "ECHA RESPUESTA RADICADO", "FECHA DE RESPUESTA CON COMENTARIO"]:  # Fechas
            transformed_row[key] = transform_date(value)
        else:
            transformed_row[key] = handle_empty(clean_text(value))
        
        # Si es un campo numérico, lo convertimos
        if isinstance(transformed_row[key], (int, float)):
            transformed_row[key] = transform_numeric(transformed_row[key])

    # Convertir el diccionario a una Serie, para que pandas lo entienda correctamente
    return pd.Series(transformed_row)
