
## Description:

A brief description of what this project does and who it's for

This project was made in order to be able to convert any video format to mp4 with python, occupying the "moviepy" library

## Installation

First, create a virtual environment:


```bash
python -m venv Virtual_Environment_Name
```


Then activate your virtual environment

```bash
cd Virtual_Environment_Name/Script/activate
```

Install the dependencies needed to run this project with pip

```bash
  pip install -r requirements.txt
```

## Features

- Convert a video to mp4
- Convert an entire video folder to MP4

## Demo

| Endpoint | Function | method  |
| -------- | ------- | ------- |
| /convert | Convert a video to mp4 | post |
| /convertFolder | Convert a video folder to MP4 | post|

* endpoint /convertFolder

```python
#Code made in python

import requests

url = "http://127.0.0.1:5000/convertFolder" 
data = {
  #Change the paths depending on where the video to be converted is located

  #Here you change the address where the folder with the videos is located
    "directorio": "C:\\Users\\edwin\\Desktop\\go avanzado concurrencia sin convertir",

# Here you put the address where you want the videos to be saved
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
#Code made in python

import requests

url = "http://127.0.0.1:5000/convert" 
data = {
  #Change the paths depending on where the video to be converted is located
  
    #Here you change the address where the folder with the video to be converted is located
    "directorio": "C:\\Users\\edwin\\Desktop\\go avanzado concurrencia sin convertir",

    #Here you put the address where the video will be saved, at the end the name is added to it with the mp4 extension
    "destino": "C:\\Users\\edwin\\Desktop\\prueba\\video_convert.mp4"
}
response = requests.post(url, json=data)

if response.status_code == 200:
    print("Conversión exitosa:", response.json())
else:
    print("Error al convertir:", response.status_code, response.text)
```

# Petition from Postman

- **To convert a video to mp3**

To make the request to POSTMAN we first indicate that it will be of type **POST**

Then the URL where the API is running is passed to it and we pass the endpoind "**/convert**"

![Logo](https://vlink.lol/vfm/play/imgEdwin/Captura-de-pantalla-2024-06-12-113345.png)

Now it is only passed the "directory" and "destination" parameters in a json

```json
  {
    'directorio': 'C:\\ruta\\de\\ejemplo\\nombreVideo.mp4',
    'destino': 'C:\\ruta\\de\\ejemplo\\nuevo_nombre_de_video.mp4'
  }
```
- **To convert a video folder to mp3**

To make the request to POSTMAN we first indicate that it will be of type **POST**

then the URL where the API is running is passed to it and we pass the endpoind "**/convertFolder**"

![Logo](https://vlink.lol/vfm/play/imgEdwin/Captura-de-pantalla-2024-06-12-141354.png)

Now it is only passed the "directory" and "destination" parameters in a json
```json
  {
    'directorio': 'C:\\ruta\\de\\ejemplo',
    'destino': 'C:\\ruta\\de\\ejemplo'
  }
```

## Tecnologys

![Logo](https://www.svgrepo.com/show/374016/python.svg)

![Logo](https://zulko.github.io/moviepy/_images/logo.png)

![Logo](https://www.svgrepo.com/show/508915/flask.svg)

## Authors

- [@Edwin Dávila](https://github.com/ed031104)

## Feedback

If you have any feedback, please reach out  edwin.noviembre.0306@gmail.com