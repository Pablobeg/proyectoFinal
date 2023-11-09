import sqlite3

def buscar_usuario_por_id(usuario_id):
    # Establece la conexión a la base de datos
    conexion = sqlite3.connect('universidad.db')
    
    # Crea un cursor para ejecutar comandos SQL
    cursor = conexion.cursor()
    
    # Consulta SQL para buscar un usuario por su ID
    consulta = f"SELECT * FROM alumno WHERE clave_alumno= '{usuario_id}'"
    
    # Ejecuta la consulta
    cursor.execute(consulta)
       # Obtiene el resultado de la consulta
    resultado = cursor.fetchone()
    
    # Cierra la conexión a la base de datos
    conexion.close()
    
    # Devuelve el resultado
    return resultado


