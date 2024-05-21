from weather import get_weather
from location import location


l1 = location('Germany', 'Aalen', 'Baden-Wuertemberg')

print(get_weather(l1))


l2 = location('Germany', 'Berlin', 'Berlin')

print(get_weather(l2))


 