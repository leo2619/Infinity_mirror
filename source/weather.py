import requests
from location import location

def get_weather():
    
    '''

    Returns
    -------
    icon           : String     DESCRIPTION : clear-day, lear-night, partly-cloudy-day, 
                                              partly-cloudy-night, cloudy, fog, wind, rain, 
                                              sleet, snow, hail, thunderstorm, null

    temperature    : String     DESCRIPTION : Air temperature in °C at timestamp, 2 m above the ground
    wind_direction : String     DESCRIPTION : Mean wind direction during previous 30 minutes, 10 m above the ground
    wind_speed     : String     DESCRIPTION : Mean wind speed in km/h during previous previous 30 minutes, 10 m above the ground
    '''
    
    cordinates = location.get_coordinates()
    
    lat, lon = cordinates
    lat = str(lat)
    lon = str(lon)
    
    r_weather = requests.get('https://api.brightsky.dev/current_weather?lat=' + lat + '&lon=' + lon + '&units=dwd')
    
    icon =  r_weather.json()['weather']['icon']
    temperature = r_weather.json()['weather']['temperature']
    wind_speed = r_weather.json()['weather']['wind_speed_30']
    wind_direction_degrees = int(r_weather.json()['weather']['wind_gust_direction_30'])
    
    if 345 <= wind_direction_degrees and wind_direction_degrees <= 15:
        wind_direction = 'Nord'
    elif 15 < wind_direction_degrees and wind_direction_degrees <= 75:
        wind_direction = 'Nord-Ost'
    elif 75 < wind_direction_degrees and wind_direction_degrees <= 115:
        wind_direction = 'Ost'
    elif 115 < wind_direction_degrees and wind_direction_degrees <= 165:
        wind_direction = 'Sued-Ost'
    elif 165 < wind_direction_degrees and wind_direction_degrees <= 195:
        wind_direction = 'Sued'
    elif 195 < wind_direction_degrees and wind_direction_degrees <= 255:
        wind_direction = 'Sued-West'
    elif 255 < wind_direction_degrees and wind_direction_degrees <= 285:
        wind_direction = 'West'
    elif 285 < wind_direction_degrees and wind_direction_degrees < 345:
        wind_direction = 'Nord-West'
    else:
        print('error')
    
    print(wind_direction)
    return icon, temperature, wind_direction, wind_speed
    
