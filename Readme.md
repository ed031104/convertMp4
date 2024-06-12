
## Description:

A brief description of what this project does and who it's for

This project was made in order to be able to convert any video format to mp4 with python, occupying the "moviepy" library

## Installation

First, create a virtual environment:


```bash
python -m virtualenv venv
```


Install the dependencies needed to run this project with pip

```bash
  pip install -r requirements.txt
```
## Features

- Convert a video to mp4
- Convert an entire video folder to MP4

## Demo

| Endpoint             |      función                                                                |
| ----------------- | ------------------------------------------------------------------ |
| /convert | Convert a video to mp4 |
| /convertFolder | Convert a video folder to MP4 |

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

## Tecnologys

![Logo](https://www.svgrepo.com/show/374016/python.svg)

![Logo](https://zulko.github.io/moviepy/_images/logo.png)

![Logo](https://www.svgrepo.com/show/508915/flask.svg)

## Authors

- [@Edwin Dávila](https://github.com/ed031104)

## Feedback

If you have any feedback, please reach out  edwin.noviembre.0306@gmail.com