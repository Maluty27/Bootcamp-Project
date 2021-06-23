from datetime import datetime

import requests

f = open("Weather Data.txt","a")
api_key = 'de1cd0f89fd64a0cf6b4e1cf513b98e1'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

# create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
f.write("City : "+str(location)+"\n")
f.write("Temperature : "+str(temp_city)+"\n")
f.write("Weather Desc : "+str(weather_desc)+"\n")
f.write("Humidity : "+str(hmdt)+"\n")
f.write("Wind Speed : "+str(wind_spd)+"\n\n")

print("-------------------------------------------------------------")
print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc  :", weather_desc)
print("Current Humidity      :", hmdt, '%')
print("Current wind speed    :", wind_spd, 'kmph')
