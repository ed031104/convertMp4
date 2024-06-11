from moviepy.editor import *
import os
from pathlib import Path

def seleccionar_archivo(directorio):
    archivo_seleccionado = Path(directorio)
    return archivo_seleccionado

# def seleccionar_carpeta():
#     root = tk.Tk()
#     root.withdraw()  # Ocultar la ventana principal de tkinter
#     carpeta_seleccionada = filedialog.askdirectory( title="Seleccionar carpeta")
#     return carpeta_seleccionada


# def seleccionar_destino():
#     root = tk.Tk()
#     root.withdraw()  # Ocultar la ventana principal de tkinter
#     destino_seleccionado = filedialog.asksaveasfilename(
#         title="Guardar archivo como",
#         defaultextension=".mp4",
#         filetypes=(("Archivo MP4", "*.mp4"),)
#     )
#     return destino_seleccionado

def obtener_videos(directorio):
    # Extensiones de archivos de video que deseas buscar
    extensiones_video = ['*.mp4', '*.avi', '*.mkv', '*.mov', '*.wmv', '*.flv', '*.mpeg']
    path_directorio = Path(directorio)
    videos = []
    for extension in extensiones_video:
        videos.extend(path_directorio.rglob(extension))
    return videos

def convertir_a_mp4(archivo_entrada, archivo_salida):
    try:
        input_path = 'file:' + archivo_entrada if not archivo_entrada.startswith('file:') else input_path
        clip = VideoFileClip(input_path)
        clip.write_videofile(archivo_salida, codec='libx264')
        print(f"Conversión completa: {archivo_salida}")
    except Exception as e:
        print(f"Error al convertir el archivo: {e}")

def convertir_many_mp4(archivos_entrada, carpeta_salida):
    try:
        for archivo in archivos_entrada:
            input_path = 'file:' + archivo if not archivo.startswith('file:') else input_path
           
            clip = VideoFileClip(str(input_path))
           
            nombre_salida = Path(carpeta_salida) / (archivo.stem + ".mp4")
           
            clip.write_videofile(str(nombre_salida), codec='libx264')
           
            print(f"Conversión completa: {nombre_salida}")
    except Exception as e:
        print(f"Error al convertir el archivo: {e}")


