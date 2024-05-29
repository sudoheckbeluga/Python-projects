import requests
from datetime import datetime

userapi="fbf89c482b289ff9a119535bd913cba5"
city=str(input())
url="https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid="+userapi

api=requests.get(url)
##api_data is a dictionary from which elements are to be extracted
#print(api.json())
api_data = api.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(city.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
