import json
import requests
from country_codes import country_codes_list

class Settings:
    
    def __init__(self, username):
                
        self.user = username
        self.setting_file = 'setting_' + self.user + '.json'
        
        try:
            open(self.setting_file, 'x')
        except:
            try:
                with open(self.setting_file) as json_file:
                    data = json.load(json_file)
                len(data) == 3
            except:
                print('No or wrong locationdata found, set new one')
                self.set_location_setting()
        
        else:
            print('No location found, set new one')
            self.set_location_setting()
      
    
    def set_location_setting(self):
        
        country = input('Country: ')
        city = input('City: ')
        state = input('State: ')
        
        data = {
            'Country': country,
            'City': city,
            'State': state
        }
        setting = open(self.setting_file, 'w')
        setting.write(json.dumps(data))
        setting.close
    
class Location(Settings):
    
    def __init__(self, username):
        super().__init__(username)
    
        
    def get_request(self):
        
        location_setting = eval(open(self.setting_file, 'r').read())
        country = location_setting['Country']
        city = location_setting['City']
        state = location_setting['State']
        
        for i in country_codes_list:
            if i['name'] == country:
                country_code = i['code']
                   
        self.r_location = requests.get('http://api.openweathermap.org/geo/1.0/direct?q='
                                  + city + ','+ state + ',' + country_code + 
                                  '&limit=5&appid=2fb76b8383ba35703d287350c62e568b')
            

    def get_coordinates(self):
        
        self.get_request()   
        lat = self.r_location.json()[0]['lat']
        lon = self.r_location.json()[0]['lon']
        
        return lat, lon

    def get_city(self):
        
        self.get_request()
        return self.r_location.json()[0]['name']

class Weather:
    
    def __init__(self, Location):
        
        self.Location = Location
        
        try:
            self.get_request()
        except:
            raise SystemError('No connection')
    
    def get_request(self):
        
        coordinates = self.Location.get_coordinates()
        
    
        lat, lon = coordinates
        lat = str(lat)
        lon = str(lon)
        
        self.r_weather = requests.get('https://api.brightsky.dev/current_weather?lat='
                         + lat + '&lon=' + lon + '&units=dwd')
        
    def get_wind(self):
              
        
        self.get_request()
    
    
        wind_speed = self.r_weather.json()['weather']['wind_speed_30']
        wind_direction_degrees = int(self.r_weather.json()['weather']['wind_gust_direction_30'])
        
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
    
    def get_temperature(self):
        
        self.get_request()
        
        temperature = self.r_weather.json()['weather']['temperature']
    
        return str(temperature) + '°C'
    
    def get_icon(self):
        
        self.get_request()
        
        icon = self.r_weather.json()['weather']['icon']
    
        #icon path 
        if icon == 'sleet' or icon == 'snow':
            icon_path = 'weather_icons/snow.png'
        else:
            icon_path = f'weather_icons/{icon}.png'
       
        return icon_path

    def get_status(self):
        self.get_request()
        
        status =  self.r_weather.json()['weather']['icon']
        
        return status
    
