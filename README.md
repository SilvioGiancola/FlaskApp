# Flask

Create the conda environment `conda env create -f env.yml`

Run the server with `python flask_app.py`

Request a prediction with `python request.py`

The request will post the image `image.jpg` on the server `/api/predict`.
The server will read that image and save a copy in `image_received.jpg`.
