import sqlite3
import qrcode
import uuid

# Generar un UUID
codigo_alumno = uuid.uuid4()

# Conectar a la base de datos
conn = sqlite3.connect('universidad.db')
cursor = conn.cursor()

# Generar un UUID para el alumno
clave_alumno1= str(uuid.uuid4())

# Insertar un registro con el UUID como identificador del alumno
nombre_alumno = "lalo garza"
matricula1 = 20
carrera ="ing computacion"
cursor.execute("INSERT INTO alumno (clave_alumno, nombre_alumno, matricula, carrera) VALUES (?, ?, ?,?)", (clave_alumno1, nombre_alumno, matricula1, carrera))

# Guardar los cambios
conn.commit()

# Cerrar la conexión
conn.close()



def generar_qr(texto):
    # Crear objeto QRCode
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    
    # Agregar datos al QRCode
    qr.add_data(texto)
    qr.make(fit=True)

    # Crear imagen QR
    imagen_qr = qr.make_image(fill_color="black", back_color="white")

    # Guardar la imagen
    nombre_archivo = f"codigo_qr_{texto}.png"
    imagen_qr.save(nombre_archivo)

    print(f"Se ha generado el código QR en el archivo: {nombre_archivo}")

# Ejemplo de uso
texto_de_entrada = "c4c4ad14-f49b-4420-945a-74a32b9d448d"
generar_qr(texto_de_entrada)
