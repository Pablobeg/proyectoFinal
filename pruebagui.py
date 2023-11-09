import tkinter as tk
import qrcode
from PIL import Image, ImageTk
from entrada import ingreso, generadorQr
from detectorqr import detector
from busquedAlumno import buscar_usuario_por_id
import tkinter.messagebox as messagebox
import asyncio
from enviomsj import enviar_mensaje, inicio

def validador(nomb, mat, carre):
    if not mat.isdigit() and not nomb and mat is not None and not carre:
        messagebox.showerror("Error", "La matrícula debe contener solo números y ningun campo debe estar vacio")
    else:
        codigo=ingreso(nomb, mat, carre)
        return 'exitoso', codigo

def mostrar_ventana_registro():
    registro_window = tk.Toplevel(root)
    registro_window.title("Registro y Generación de QR")
    registro_window.geometry("400x300")
    label_nombre = tk.Label(registro_window, text="Nombre:")
    label_nombre.pack()
    entry_nombre = tk.Entry(registro_window)
    entry_nombre.pack()

    label_matricula = tk.Label(registro_window, text="Matrícula:")
    label_matricula.pack()
    entry_matricula = tk.Entry(registro_window)
    entry_matricula.pack()

    label_carrera = tk.Label(registro_window, text="Carrera:")
    label_carrera.pack()
    entry_carrera = tk.Entry(registro_window)
    entry_carrera.pack()
    
    def registrar_y_limpiar():
        # Llamada a la función ingreso y validación
        estado, ui=validador(entry_nombre.get(), entry_matricula.get(), entry_carrera.get())

        if estado == 'exitoso':
            # Limpiar campos de entrada después de un registro exitoso
            entry_nombre.delete(0, tk.END)
            entry_matricula.delete(0, tk.END)
            entry_carrera.delete(0, tk.END)
            # Mostrar mensaje de registro exitoso
            
            messagebox.showinfo("Éxito", "Registro exitoso")
            # Generar el código QR después de un registro exitoso
            codigo_qr = ui
            qr_image = qrcode.make(codigo_qr)
            
            ruta_guardado = "codigo_qr_generado.png"
            qr_image.save(ruta_guardado)
            # Mostrar el código QR en una ventana nueva
            top = tk.Toplevel(root)
            top.title("Código QR para entrar")

            qr_tk = ImageTk.PhotoImage(image=qr_image)
            label_qr = tk.Label(top, image=qr_tk)
            label_qr.image = qr_tk
            label_qr.pack()
        

    # Botón para registrar y generar QR con la validación de datos
    boton_registrar = tk.Button(registro_window, text="Registrar y generar QR", command=registrar_y_limpiar)
    boton_registrar.pack()
    boton_registrar.pack()

    boton_retroceso = tk.Button(registro_window, text="Volver al menú principal", command=registro_window.destroy)
    boton_retroceso.pack()



def detectar_y_mostrar_mensaje():
    # Intenta detectar el código QR
    resultado = detector()
    print('resultado del detector', resultado)
    busqueda= buscar_usuario_por_id(resultado)
    print('resultado de busqueda', busqueda)
    ventana_actual = tk._default_root
    if busqueda==None:
        messagebox.showinfo("Usuario no encontrado", "No se encontró el código QR asociado a este usuario")
    else:
        messagebox.showinfo("Acceso Permitido", "Puedes entrar")
        mensaje = (
              f"El alumno: {busqueda[1]}\n"
              f"con matricula: {busqueda[2]}\n"
              f"de la carrera: {busqueda[3]}\n"
              f"a ingresado a la escuela")

        asyncio.run(inicio(mensaje))

    for widget in ventana_actual.winfo_children():
        if isinstance(widget, tk.Toplevel) and widget.title() == "Escaneo de Código QR":
            widget.destroy()

def mostrar_ventana_escaneo():
    # Crear una ventana secundaria (Toplevel) para el escaneo del código QR
    escaneo_window = tk.Toplevel(root)
    escaneo_window.title("Escaneo de Código QR")
    escaneo_window.geometry("400x300")

    label_detectando = tk.Label(escaneo_window, text="Detectando...")
    label_detectando.pack()
    
    def ocultar_mensaje_detectando():
        for widget in escaneo_window.winfo_children():
            if isinstance(widget, tk.Label) and widget.cget('text') == "Detectando...":
                widget.destroy()

    escaneo_window.after(2000, detectar_y_mostrar_mensaje)
    escaneo_window.after(2000, ocultar_mensaje_detectando)
    # Lógica para la detección y manejo de mensaje  # Muestra el mensaje después de 2 segundos


def ocultar_ventana():
    root.withdraw()

def mostrar_ventana():
    root.deiconify()

# Crear ventana principal
root = tk.Tk()
root.title("Aplicación con GUI")
root.geometry("200x200")

# Botón para abrir ventana de registro y generación de QR
boton_registro_qr = tk.Button(root, text="Registrar alumno", command=mostrar_ventana_registro)
boton_registro_qr.pack()

# Botón para abrir ventana de escaneo de QR
boton_escanear_qr = tk.Button(root, text="Escanear QR", command=mostrar_ventana_escaneo)
boton_escanear_qr.pack()

root.mainloop()  # Bucle principal