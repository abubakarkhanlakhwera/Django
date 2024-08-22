from django.shortcuts import render , redirect
from .api_key import key
import json
import urllib.request as ureq
from urllib.parse import quote

def index(req):
    if req.method == 'POST':
        city = req.POST['city']
        encoded_city = quote(city)
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={encoded_city}&appid={key}'
        try:
            with ureq.urlopen(api_url) as response:
                data = json.loads(response.read())
                # Convert temperature from Kelvin to Celsius
                temperature_kelvin = data['main']['temp']
                temperature_celsius = temperature_kelvin - 273.15

                if temperature_celsius > 30:
                    
                    text_color = 'text-warning'  # reddish-yellow
                elif 25 < temperature_celsius <= 30:
                    
                    text_color = 'text-info'  # cool color
                else:
                    
                    text_color = 'text-primary'

                weather_data = {
                    'city': city,
                    'temperature': f"{temperature_celsius:.2f}°C",
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                    'text_color': text_color,
                }
        except Exception as e:
            # Handle errors or exceptions
            weather_data = {'error': str(e)}
        return render(req, 'index.html', {'weather_data': weather_data})
        
    
    else:
        return render(req, 'index.html')