import psycopg2
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD
import pandas as pd

def connect_db():
    """Conectar a la base de datos PostgreSQL."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print(f"Error: {e}")
        return None

def insert_data(table_name, data):
    """
    Inserta datos en la base de datos a partir de un DataFrame de Pandas.

    :param table_name: Nombre de la tabla en la base de datos.
    :param data: DataFrame con los datos a insertar.
    """
    conn = connect_db()
    if conn is None:
        print("No se pudo conectar a la base de datos")
        return

    try:
        cursor = conn.cursor()
        
        # Convertir DataFrame a formato adecuado para la inserción
        for i, row in data.iterrows():
            columns = ", ".join(data.columns)
            values = ", ".join(f"'{v}'" if v is not None else "NULL" for v in row.values)
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
            
            cursor.execute(query)
        
        conn.commit()
        print(f"Datos insertados en {table_name}")
    
    except Exception as e:
        print(f"Error al insertar datos: {e}")
    finally:
        conn.close()

def test_connection():
    """Probar la conexión a la base de datos."""
    conn = connect_db()
    if conn:
        print("Conexión exitosa a la base de datos")
        conn.close()
    else:
        print("No se pudo conectar a la base de datos")

if __name__ == "__main__":
    test_connection()
