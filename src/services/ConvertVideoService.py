import models.convertVideo as convertVideo

def convert_video(directorio, destino):
    if directorio:
        if destino:
            try:
                convertVideo.convertir_a_mp4(directorio, destino)
                return "Video converted successfully"
            except Exception as e:
                return f"Error during conversion: {e}"
        else:
            return "No output file or directory selected."
    else:
        return "No input directory selected."

def convert_many_videos(directorio, destino):
    videos = convertVideo.obtener_videos(directorio)
    if videos:
        print("Videos encontrados:")
        for video in videos:
            print(video)
            if destino:
                ruta_Destino = convertVideo.seleccionar_archivo(destino)
                convertVideo.convertir_many_mp4(videos, ruta_Destino)
            else:
                return"No se seleccionó ninguna carpeta de salida."
    else:
        return "No se encontraron videos en la carpeta seleccionada."
    