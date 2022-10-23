import os
import requests
import json
import subprocess

url = "https://eardetect-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/94f0562c-8359-4b28-87b8-8a38bc88994d/classify/iterations/Iteration9/image"
headers = { 'content-type':'application/octet-stream','Prediction-Key':'98f87e1c0e2f4c1abc64cdad3f8c79d7' }

def classify_ear():

    r = requests.post( url, data=open("../../../Downloads/imagen.jpg", "rb"), headers=headers )
    os.remove("../../../Downloads/imagen.jpg")

    response = json.loads(r.content)['predictions']
    ear_data = float(response[0]['probability']) if response[0]['tagName'] == 'Ear' else float(response[1]['probability'])
    not_ear_data = float(response[0]['probability']) if response[0]['tagName'] != 'Ear' else float(response[1]['probability'])

    if ear_data > not_ear_data and ear_data > 0.75:
        return (1, 1)
    else:
        return (0, 0)
