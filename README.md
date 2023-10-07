[![Connect with me on LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=LinkedIn&style=flat-square)](https://www.linkedin.com/in/omar-alsaabi-32675b193/)


# 🌦️ ArabWeatherTask: Where Data Meets Weather Magic 🌦️
Welcome to ArabWeatherTask, a delightful journey into the world of data and weather! 🚀

### Prject Overview:
ArabWeatherTask is more than just a project; it's an adventure in data science and meteorology. We've blended the power of Tabular and Image data to bring you insights into weather like never befor

# How to Get Started:
1. Get the Code:
- Clone the repo to your local machine:
```
git clone https://github.com/Omaralsaabi/ArabWeatherTask.git
```
2. Set Up Your Environment:
- Enter the repo directory:
```
cd ArabWeatherTask
```
- Create a virtual environment: 
```
python3 -m venv venv
```
- Activate the virtual environment:
```
source venv/bin/activate
```
- Install the requirements 
```
pip install -r requirements.txt
```

### Tabular Model
1. Explore the Data:
- Enter the data directory:
```
cd WeatherTabular
```
- Dive into the training notebook `train.ipynb` and the prediction notebook `predict.ipynb`.

### Image Model 
1. Visualize Weather:
- Enter the image directory:
```
cd WeatherCV
```
- Immerse yourself in the CNN training notebook `CVWeather-CNN.ipynb` and the ResNet training notebook `CVWeather-ResNet-Finetuned.ipynb`.
- Ready for some real magic? Run the server:
```
python3 manage.py runserver
```
- Open your browser and journey to `http://localhost:8000/predict`. Upload an image and let the weather predictions begin!

## Docker Magic:
Want to make things even simpler? We've got you covered!

1. Dockerize Your Experience:
- Pull the docker image:
```
docker pull omaralsaabi/weathercv
```
- Launch the Docker container:
```
docker run -p 8000:8000 omaralsaabi/weathercv
```
- Explore weather insights at `http://localhost:8000/predict`.

For any questions, ideas, reach out to me at : `prof.omaralsaabi@gmail.com`.
