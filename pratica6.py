from picamera import PiCamera, Color
from time import sleep
from requests import get
import json
from pprint import pprint

## COLETA DE DADOS API
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/966583'

weather = get(url).json()['items']

temp = weather[0].get('ambient_temp')
hum = weather[0].get('humidity')

print("Temperatura ambiente: " + str(temp) + "ºC" + "\nUmidade: " + str(hum) + "%")

# Configuração da câmera
camera = PiCamera()
camera.rotation = 180
camera.framerate = 15

# Ambiente de visualização
camera.start_preview()

# Configuração da label de texto
camera.annotate_background = Color('white')
camera.annotate_foreground = Color('black')
camera.annotate_text = "Temperatura ambiente: " + str(temp) + "\nUmidade: " + str(hum) 
camera.annotate_text_size = 50

sleep(7)
#Captura de foto
camera.capture('/home/sel/SEL0337/Pratica_6/weather1.jpg')
#Captura de video
camera.start_recording('/home/sel/SEL0337/Pratica_6/weather1.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()


