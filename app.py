import json
from datetime import datetime
from flask import Flask, request

import weatherAPI as api

from keras.models import load_model
import tensorflow

app = Flask(__name__)
model = load_model('MLModel/LoraxV1.0.h5')


@app.route('/')
def hello_world():  # put application's code here
    return 'Lorax says hi'


"""
request json structure
{
    "region": string,
    "date": string, //YYYY-MM-DD
    "temp": float,
    "humidity": float    
}
"""


@app.route('/predict', methods=['POST'])
def predict():
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
    #month, day, temp, RH, wind, rain
    print(int(month), dayoftheweek, temp, humidity, wind, rain)
    data = [int(month), dayoftheweek, temp, humidity, wind, rain]
    prediction = model.predict([data])

    if prediction <0.3:
        chance = "low"
    elif prediction < 0.75:
        chance = "moderate"
    else:
        chance = "high"

    return json.dumps({
        "prediction" : str(prediction[0][0]),
        "likelihood": chance
    })





if __name__ == '__main__':
    app.run()
