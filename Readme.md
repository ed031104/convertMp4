## API para convertir cualquier tipo de video a MP4


## About Me:

A brief description of what this project does and who it's for

Este proyecto se hizo con el fin de poder convertir cualquier formato de video a mp4 con python, ocupando la librería  "moviepy"

## Installation

Instala las dependencias necesarias para ejecutar este proyecto con pip

```bash
  pip install -r requirements.txt
```
## Features

- Convertir un video a mp4
- convertir toda una carpeta de videos a mp4

## Demo

| Endpoint             |      función                                                                |
| ----------------- | ------------------------------------------------------------------ |
| /convert | convierte un video a mp4 |
| /convertFolder | convierte una carpeta de videos a mp4 |

* endpoint /convertFolder

```python
#Código hecho en python

import requests

url = "http://127.0.0.1:5000/convertFolder" 
data = {
  #Cambia las rutas según donde se encuentre el video a convertir

  #Aquí cambias la dirección donde se encuentre la carpeta con los videos
    "directorio": "C:\\Users\\edwin\\Desktop\\go avanzado concurrencia sin convertir",

# Aquí pones la dirección donde quieres que se guarden los videos
    "destino": "C:\\Users\\edwin\\Desktop\\prueba"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Conversión exitosa:", response.json())
else:
    print("Error al convertir:", response.status_code, response.text)
```

* endpoint /convert

```python
#Código hecho en python

import requests

url = "http://127.0.0.1:5000/convert" 
data = {
  #Cambia las rutas según donde se encuentre el video a convertir
  
    #Aquí cambias la dirección donde se encuentre la carpeta con el video a convertir
    "directorio": "C:\\Users\\edwin\\Desktop\\go avanzado concurrencia sin convertir",

    #Aquí pones la dirección en donde se guardará el video, al final se le agrega el nombre nuveo con la extensión mp4
    "destino": "C:\\Users\\edwin\\Desktop\\prueba\\video_convert.mp4"
}
response = requests.post(url, json=data)

if response.status_code == 200:
    print("Conversión exitosa:", response.json())
else:
    print("Error al convertir:", response.status_code, response.text)
```

## Tecnologys

![Logo](https://www.svgrepo.com/show/374016/python.svg)

![Logo](https://zulko.github.io/moviepy/_images/logo.png)

![Logo](https://www.svgrepo.com/show/508915/flask.svg)

## Authors

- [@Edwin Dávila](https://github.com/ed031104)
