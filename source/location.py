import requests
from country_codes import country_codes_list

class location:
    
    
    def __init__(self, Country, City, State):
        
        '''
        Parameters
        ----------
        country : TYPE == String
        city    : TYPE == String
        state   : TYPE == String     DESCRIPTION : Bundesland 
       
        '''
        
        self.country = Country
        self.city = City
        self.state = State
        

    def get_coordinates(self):
        '''
        Returns
        -------
        TYPE == float      DESCRIPTION : lat
        TYPE == float      DESCRIPTION : lon
    
        '''
    
        
        for i in country_codes_list:
            if i['name'] == self.country:
                country_code = i['code']
                
        
        r_location = requests.get('http://api.openweathermap.org/geo/1.0/direct?q='
                                  + self.city + ','+ self.state + ',' + country_code + '&limit=5&appid=2fb76b8383ba35703d287350c62e568b')
        
        return r_location.json()[0]['lat'], r_location.json()[0]['lon']

