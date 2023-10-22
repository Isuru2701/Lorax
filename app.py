import json
from datetime import datetime
from flask import Flask, request

import weatherAPI as api

from keras.models import load_model
import tensorflow

app = Flask(__name__)
model = load_model('MLModel/LoraxV1.1.h5')


@app.route('/')
def hello_world():  # put application's code here
    return """<h1>Lorax says hi!</h1>
    request json structure <br>
{ <br>
    "region": string, <br>
    "date": string, //YYYY-MM-DD <br>
    "temp": float, <br>
    "humidity": float  <br>  
}
<br>
<br>
Made by @Isuru2701 
<br>
check it out on github: <br>
<a href='https://github.com/Isuru2701/Quokka'>Model </a> <br>
<a href='https://github.com/Isuru2701/Lorax'>API </a>

    """


@app.route('/predict', methods=['POST'])
def predict():
    """
    request json structure
    {
        "region": string,
        "date": string, //YYYY-MM-DD
        "temp": float,
        "humidity": float
    }
    """

    req = request.get_json()
    region = req['region']
    date = req['date']
    temp = req['temp']
    humidity = req['humidity']

    wind, rain = api.makeCall(region)
    print(wind, rain)

    dayoftheweek = datetime.strptime(date, '%Y-%m-%d').weekday() + 1
    print(datetime.strptime(date, '%Y-%m-%d'))

    year, month, day = date.split('-')
    # month, day, temp, RH, wind, rain
    print(int(month), dayoftheweek, temp, humidity, wind, rain)
    data = [int(month), dayoftheweek, temp, humidity, wind, rain]
    prediction = model.predict([data])

    if prediction < 0.3:
        chance = "low"
    elif prediction < 0.75:
        chance = "moderate"
    elif prediction < 0.9:
        chance = "moderately high"
    else:
        chance = "high"

    return json.dumps({
        "prediction": str(prediction[0][0]),
        "likelihood": chance
    })


if __name__ == '__main__':
    app.run()
