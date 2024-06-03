import json

class Settings:
    
    def __init__(self):
        
        try:
            open('setting.json', 'x')
        except:
            try:
                with open('setting.json') as json_file:
                    data = json.load(json_file)
                len(data) == 3
            except:
                pass
            else:
                print('No location data found, set new one')
                Settings.set_location_setting()
        
        else:
            print('No location found, set new one')
            Settings.set_location_setting()
      
    
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

