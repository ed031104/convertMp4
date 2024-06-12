import src.models.convertVideo as convertVideo

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

def convert_many_videos(carpeta_entrada, carpeta_salida):
    videos = convertVideo.obtener_videos(carpeta_entrada)
    if videos:
        try:
            convertVideo.convertir_many_mp4(videos, carpeta_salida)
            return "Videos converted successfully"
        except Exception as e:
            return f"Error during conversion: {e}"
    else:
        return "No se encontraron videos en la carpeta seleccionada."
    