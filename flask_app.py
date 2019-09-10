from flask import Flask, request, jsonify

import numpy as np
import cv2

app = Flask(__name__)

@app.route("/") # main webpage
def home():
    return "Hello world!"


@app.route("/api/predict", methods=['POST'])
def predict():
    headers = request.headers
    print(headers)

    if (headers["content-type"] == "image/jpeg"):
        data = request.data
        
        nparr = np.frombuffer(data,np.uint8)

        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        cv2.imwrite("image_received.jpg", img)

        # Do any prediction here
        # prediction = DeepLearningModel(img)
        
        prediction = [[0,10,10,20],[30,20,10,10],]

        return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
    