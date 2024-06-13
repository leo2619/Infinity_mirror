import time
import pygame
from pygame.locals import *
import DisplayLib

pygame.init()
W = DisplayLib.Weather()
L = DisplayLib.Location()    

# Variablen/KONSTANTEN setzen

WEISS = (255, 255, 255)
spielaktiv = True

# icon
skalierung = 0 
skalierungswert = 0.02

icon_path = pygame.image.load(W.get_icon())
bildgroessen = icon_path.get_rect()

# status text
my_font = pygame.font.SysFont('Comic Sans MS', 30)
status_text_surface = my_font.render(W.get_status(), False, (0, 0, 0))

# wind text
wind_direction, wind_speed = W.get_wind()
wind_direction_text_surface = my_font.render(wind_direction, False, (0, 0, 0))
wind_speed_text_surface = my_font.render(wind_speed, False, (0, 0, 0))

# temperature
temp_text_surface = my_font.render(W.get_temperature(), False, (0, 0, 0))

# city
city_text_surface = my_font.render(L.get_city(), False, (0, 0, 0))

# logo
my_start = pygame.font.SysFont('Comic Sans MS', 80)
logo_text_surface = my_start.render('Infinity Spiegel', False, (0, 0, 0))

# Initial background color (black)
color = [0, 0, 0]
# Set the increment value for brightness increase
increment = 1
max_brightness = 255
# Control the speed of brightness increase
delay = 0.001

# Definieren und Öffnen eines neuen Fensters
fenster = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Grafik skalieren")
clock = pygame.time.Clock()

# Schleife Hauptprogramm
while spielaktiv:
    start = time.time()
    end = start + 600
        
    
    while time.time() < end and spielaktiv:
        # Spiellogik
        skalierung += skalierungswert
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        if skalierung > 5 or skalierung < -5:
            skalierungswert = -skalierungswert
        
        if color[0] < max_brightness:
            color = [min(c + increment, max_brightness) for c in color]
        # Spielfeld Hintergrund
        fenster.fill(color)
            
        if start + 4.5 > time.time():
            
            FPS = 60
            fenster.blit(logo_text_surface, (150, 400))
        
        if start + 4.5 < time.time():
            
            FPS = 400
        
            
            # Spielfeld/figuren zeichnen
            icon_groesse = pygame.transform.scale(icon_path, (350 + int(skalierung), 350 + int(skalierung)))
            fenster.blit(icon_groesse, (150, 100))
            
            # Text zeichnen
            # status
            fenster.blit(status_text_surface, (30, 20))
            # wind_direction
            fenster.blit(wind_direction_text_surface, (100, 100))
            # wind_speed
            fenster.blit(wind_speed_text_surface, (100, 150))
            # temperature
            fenster.blit(temp_text_surface, (100, 300))
            # city
            fenster.blit(city_text_surface, (150, 400))
        
        # Fenster aktualisieren
        pygame.display.flip()
        clock.tick(FPS)
    

    # Wetterdaten aktualisieren    
    icon_path = pygame.image.load(W.get_icon())
    status_text_surface = my_font.render(W.get_status(), False, (0, 0, 0))
    wind_direction, wind_speed = W.get_wind()
    wind_direction_text_surface = my_font.render(wind_direction, False, (0, 0, 0))
    wind_speed_text_surface = my_font.render(wind_speed, False, (0, 0, 0))
    temp_text_surface = my_font.render(W.get_temperature(), False, (0, 0, 0))
    city_text_surface = my_font.render(L.get_city(), False, (0, 0, 0))

