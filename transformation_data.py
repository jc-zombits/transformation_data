import pandas as pd
from datetime import datetime

def transformar_datos(input_file: str, output_file: str):
    # Leer el archivo Excel
    df = pd.read_excel(input_file, engine='openpyxl')

    # Normalizar las fechas (si existen en el DataFrame)
    fecha_columns = [
        'FECHA DE INGRESO', 
        'FECHA DE INGRESO A LA BANDEJA', 
        'FECHA DE EVACUADO DEL DOCUMENTO',
        'FECHA LIMITE DE RESPUESTA',
        'FECHA DE RESPUESTA',
        'FECHA RESPUESTA RADICADO',
        'FECHA DE RESPUESTA CON COMENTARIO'
    ]

    for col in fecha_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')  # Mantener el tipo de fecha
            # Si prefieres convertirla a texto: df[col] = df[col].dt.strftime('%Y-%m-%d')

    # Normalizar las columnas numéricas (convertir las columnas numéricas de texto a números si es necesario)
    numeric_columns = [
        'AÑO', 'RADICADO', 'DIAS', 'AMPLIACION DE TERMINOS', 'TOTAL DÍAS', 'DIAS CALENDARIO',
        'DIAS HABILES', 'AÑO RESPUESTA', 'CANTIDAD RESPUESTAS ASOCIADAS'
    ]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')  # Convertir texto a números, si es necesario

    # Las columnas de texto las mantenemos como están, pero podemos asegurarnos de que no haya valores nulos
    text_columns = [
        'MES', 'DIAS SEMANA', 'SECRETARÍA', 'TEMA', 'CLASE DE SOLICITUD', 'SOLICITANTE', 
        'INFORMACIÓN ADICIONAL DEL SOLICITANTE', 'NOMBRE DEL SOLICITANTE', 'DIRIGIDO A', 
        'NOMBRE DEL SERVIDOR O DEPENDENCIA', 'ULTIMO USUARIO EN RUTA', 'ULTIMO ESTADO EN RUTA', 
        'FORMATO', 'MES LIMITE DE RESPUESTA', 'MES REAL RESPUESTA', 'OBSERVACIÓN', 'ESTADO',
        'OPORTUNIDAD', 'CANAL', 'USUARIO RADICADOR SOLICITUD', 'IDENTIFICACIÓN CIUDADANO', 
        'NOMBRE CIUDADANO', 'TELEFONO', 'PENDIENTE', 'VENCIDOS', 'A TIEMPO', 'OPORTUNO', 'NO OPORTUNO'
    ]

    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].fillna('')  # Llenar valores nulos con cadena vacía

    # Guardar el archivo transformado
    df.to_excel(output_file, index=False)
    
    print(f"Archivo Excel transformado guardado en: {output_file}")
