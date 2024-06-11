from moviepy.editor import *
import os
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de tkinter

    archivo_seleccionado = filedialog.askopenfilename(
        title="Seleccionar archivo",
        filetypes=(("Archivos de videos", "*.mp4" ), ("Todos los archivos", "*.*"))
    )
    return archivo_seleccionado

def seleccionar_carpeta():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de tkinter
    carpeta_seleccionada = filedialog.askdirectory( title="Seleccionar carpeta")
    return carpeta_seleccionada


def seleccionar_destino():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de tkinter
    destino_seleccionado = filedialog.asksaveasfilename(
        title="Guardar archivo como",
        defaultextension=".mp4",
        filetypes=(("Archivo MP4", "*.mp4"),)
    )
    return destino_seleccionado

def obtener_videos(directorio):
    # Extensiones de archivos de video que deseas buscar
    extensiones_video = ['*.mp4', '*.avi', '*.mkv', '*.mov', '*.wmv', '*.flv', '*.mpeg']
    # Crear un objeto Path para el directorio
    path_directorio = Path(directorio)
    # Crear una lista para almacenar los videos encontrados
    videos = []
    for extension in extensiones_video:
        # Utilizar rglob para buscar archivos con la extensión específica recursivamente
        videos.extend(path_directorio.rglob(extension))
    return videos

def convertir_a_mp4(archivo_entrada, archivo_salida):
    try:
        clip = VideoFileClip(archivo_entrada)
        clip.write_videofile(archivo_salida, codec='libx264')
        print(f"Conversión completa: {archivo_salida}")
    except Exception as e:
        print(f"Error al convertir el archivo: {e}")

def convertir_many_mp4(archivos_entrada, carpeta_salida):
    try:
        for archivo in archivos_entrada:
            clip = VideoFileClip(str(archivo))
            nombre_salida = Path(carpeta_salida) / (archivo.stem + ".mp4")
            clip.write_videofile(str(nombre_salida), codec='libx264')
            print(f"Conversión completa: {nombre_salida}")
    except Exception as e:
        print(f"Error al convertir el archivo: {e}")


