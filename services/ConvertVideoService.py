import models.convertVideo as convertVideo 
from tkinter import filedialog

def convert_video(directorio):
    if directorio:
        archivo_salida = convertVideo.seleccionar_destino()
        if archivo_salida:
            try:
                convertVideo.convertir_a_mp4(directorio, archivo_salida)
                return "Video converted successfully"
            except Exception as e:
                return f"Error during conversion: {e}"
        else:
            return "No output file or directory selected."
    else:
        return "No input directory selected."

def convert_many_videos(directorio):
    videos = convertVideo.obtener_videos(directorio)
    if videos:
        print("Videos encontrados:")
        for video in videos:
            print(video)
            carpeta_salida = convertVideo.seleccionar_carpeta()
            if carpeta_salida:
                convertVideo.convertir_many_mp4(videos, carpeta_salida)
            else:
                print("No se seleccionó ninguna carpeta de salida.")
    else:
        print("No se encontraron videos en la carpeta seleccionada.")
    