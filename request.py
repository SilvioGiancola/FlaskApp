import requests
import json

x = requests.post('http://localhost:5000/api/predict', 
                data=open("image.jpg", 'rb').read(),  
                headers={"content-type": "image/jpeg"})

print(x.text)
