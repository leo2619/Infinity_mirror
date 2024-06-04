import requests
from location import Location


class Weather:
    
    
    def get_request():
        
        L = Location
        coordinates = L.get_coordinates()
        
     
        lat, lon = coordinates
        lat = str(lat)
        lon = str(lon)
        
        r = requests.get('https://api.brightsky.dev/current_weather?lat='
                         + lat + '&lon=' + lon + '&units=dwd')
        return r
        
    def get_wind():
              
        
        r_weather = Weather.get_request()
    
    
        wind_speed = r_weather.json()['weather']['wind_speed_30']
        wind_direction_degrees = int(r_weather.json()['weather']['wind_gust_direction_30'])
        
        #wind direction 
        if 345 <= wind_direction_degrees and wind_direction_degrees <= 15:
            wind_direction = 'Nord'
        elif 15 < wind_direction_degrees and wind_direction_degrees <= 75:
            wind_direction = 'Nord-Ost'
        elif 75 < wind_direction_degrees and wind_direction_degrees <= 115:
            wind_direction = 'Ost'
        elif 115 < wind_direction_degrees and wind_direction_degrees <= 165:
            wind_direction = 'Süd-Ost'
        elif 165 < wind_direction_degrees and wind_direction_degrees <= 195:
            wind_direction = 'Süd'
        elif 195 < wind_direction_degrees and wind_direction_degrees <= 255:
            wind_direction = 'Süd-West'
        elif 255 < wind_direction_degrees and wind_direction_degrees <= 285:
            wind_direction = 'West'
        elif 285 < wind_direction_degrees and wind_direction_degrees < 345:
            wind_direction = 'Nord-West'
        else:
            print('error')
            
        return str(wind_direction) + '-Wind', str(wind_speed) + 'km/h'
    
    def get_temperature():
        
        r_weather = Weather.get_request()
        temperature = r_weather.json()['weather']['temperature']
    
        return str(temperature) + '°C'
    
    def get_icon():
        
        r_weather = Weather.get_request()
        icon =  r_weather.json()['weather']['icon']
    
        #icon path 
        if icon == 'sleet' or icon == 'snow':
            icon_path = 'weather_icons/snow.png'
        else:
            icon_path = f'weather_icons/{icon}.png'
       
        return icon_path

    def get_status():
        r_weather = Weather.get_request()
        status =  r_weather.json()['weather']['icon']
        
        return status


