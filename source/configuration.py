import json

class settings:
    
    def __init__(self):
        
        try:
            open('setting.json', 'x')
        except:
            pass
        else:
            print('No location found, set new one')
            settings.set_location_setting()
            
    
    def set_location_setting():
        
        Country = input('Country: ')
        City = input('City: ')
        State = input('State: ')
        data = {
            'Country': Country,
            'City': City,
            'State': State
        }
        setting = open('setting.json', 'w')
        setting.write(json.dumps(data))
        setting.close


        
