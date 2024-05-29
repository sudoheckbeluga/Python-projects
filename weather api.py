import requests
from datetime import datetime

userapi="fbf89c482b289ff9a119535bd913cba5"
city=str(input())
url="https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid="+userapi

api=requests.get(url)
##data is a dictionary from which elements are to be extracted
#print(api.json())
data = api.json()

temp_city = ((data['main']['temp']) - 273.15)
weather_desc = data['weather'][0]['description']
hmdt = data['main']['humidity']
wind_spd = data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(city.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Temperature is: {:.2f} deg C".format(temp_city))
print ("Weather desc  :",weather_desc)
print ("Humidity      :",hmdt, '%')
print ("Wind speed    :",wind_spd ,'kmph')
