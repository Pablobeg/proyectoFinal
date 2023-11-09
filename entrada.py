import uuid
import tkinter as tk
import qrcode
from PIL import Image, ImageTk
import sqlite3

def ingreso(entradaN, entradaMa, entradaCarr):
    # Obtener datos de los campos de entrada
    nombre = entradaN
    matricula = entradaMa
    carrera = entradaCarr
    
    # Generar clave de alumno usando la función generadorQr
    clave_alumno = generadorQr()
    
    conn = sqlite3.connect('universidad.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO alumno (clave_alumno, nombre_alumno, matricula, carrera) VALUES (?, ?, ?, ?)",
                     (clave_alumno, nombre, matricula, carrera))
    conn.commit()
    conn.close()
    
    return clave_alumno

def generadorQr():
    # Generar un UUID
    uid = uuid.uuid4()

    # Convertir el UUID a string
    uid_str = str(uid)
    
    # Devolver el código QR (en string) generado a partir del UUID
    return uid_str
