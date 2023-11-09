# Lorax

A wildfire prediction API built in lieu with an IOT system.

## Pre-fire prediction endpoint
- `/` - GET

```landing page. say hi to the lorax```


- `/predict` - POST
```json
{
  "region": "string",
    "date": "string", 
    "temp": 0.00,
    "humidity": 0.00  

}
```
> Date should be in the format `YYYY-MM-DD`

### instructions
- create a .env file in the root folder and add `WEATHER_API_KEY`
- get a `WEATHER_API_KEY` from openWeatherAPI
- run `app.py`
