# ArabWatherTask
This is a simple demosntration of training a Tabular and Image data related to weather. 

## How to run the code
1. Clone the repo to your local machine using `git clone https://github.com/Omaralsaabi/ArabWatherTask.git`
2. Enter the repo directory using `cd ArabWatherTask`
3. Create a virtual environment using `python3 -m venv venv`
4. Activate the virtual environment using `source venv/bin/activate`
5. Install the requirements using `pip install -r requirements.txt`

### Tabular Model
1. Enter the tabular directory using `cd WeatherTabular`
2. Have a look at the training notebook `train.ipynb` and the prediction notebook `predict.ipynb`

### Image Model 
1. Enter the image directory using `cd WeatherCV`
2. Have a look at the CNN training notebook `CVWeather-CNN.ipynb` and the ResNet training notebook `CVWeather-ResNet-Finetuned.ipynb`
3. Run the server using `python3 manage.py runserver`
4. Open the browser and go to `http://localhost:8000/predict`
5. Upload an image and click on predict

## How to run the code using Docker image
1. Pull the docker image using `docker pull docker pull omaralsaabi/weathercv`
2. Run the docker image using `docker run -p 8000:8000 omaralsaabi/weathercv`
3. Open the browser and go to `http://localhost:8000/predict`

For any questions, please contact me at: `prof.omaralsaabi@gmail.com`