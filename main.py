import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.getenv("API_KEY")
account_sid = "AC306577c25c5d090a86fee6db88bd6e93"
auth_token = os.getenv("AUTH_TOKEN")

weather_params = {
    "lat": 5.532819,
    "lon": -0.423424,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body ="It's going to rain today. Remember to bring an ☔",
        from_="+15673444535",
        to="+233 54 071 8497",
    )

    print(message.status)

