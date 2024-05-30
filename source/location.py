import requests
from country_codes import country_codes_list
import configuration

class location:
            

    def get_coordinates():
        '''
        Returns
        -------
        TYPE == float      DESCRIPTION : lat
        TYPE == float      DESCRIPTION : lon
    
        '''
        s = configuration.settings()
        
        location_setting = eval(open('setting.json', 'r').read())
        
        country = location_setting['Country']
        city = location_setting['City']
        state = location_setting['State']
        for i in country_codes_list:
            if i['name'] == country:
                country_code = i['code']
                
        
        r_location = requests.get('http://api.openweathermap.org/geo/1.0/direct?q='
                                  + city + ','+ state + ',' + country_code + '&limit=5&appid=2fb76b8383ba35703d287350c62e568b')
        
        return r_location.json()[0]['lat'], r_location.json()[0]['lon']

