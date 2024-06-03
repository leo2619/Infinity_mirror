import time
from weather import Weather
import pygame
from pygame.locals import *
from location import Location
from configuration import Settings
pygame.init()
W = Weather
L = Location()
    


# Variablen/KONSTANTEN setzen
FPS  = 400
WEISS   = ( 255, 255, 255)
spielaktiv = True

#icon
skalierung      = 0 
skalierungswert = 0.02

icon_path = pygame.image.load(W.get_icon())
bildgroessen = icon_path.get_rect()

#status text
my_font = pygame.font.SysFont('Comic Sans MS', 30)
status_text_surface = my_font.render(W.get_status(), False, (0, 0, 0))

#wind text
wind_direction, wind_speed = W.get_wind()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
wind_direction_text_surface = my_font.render(wind_direction, False, (0, 0, 0))
wind_speed_text_surface = my_font.render(wind_speed, False, (0, 0, 0))

#temperature
temp_text_surface = my_font.render(W.get_temperature(), False, (0, 0, 0))

#City
city_text_surface = my_font.render(L.get_city(), False, (0, 0, 0))

# Definieren und Öffnen eines neuen Fensters
fenster =pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Grafik skalieren")
clock = pygame.time.Clock()

# Schleife Hauptprogramm
while spielaktiv:
    start = time.time()
    end = start + 10
    while end > start:
        start = time.time()
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
        for event in pygame.event.get():
            # Beenden bei [ESC] oder [X]
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                spielaktiv = False
    
        # Spiellogik
        skalierung += skalierungswert
    
        if skalierung > 5 or skalierung < -5:
            skalierungswert = -skalierungswert
    
        # Spielfeld Hintergrund
        fenster.fill(WEISS)
    
        # Spielfeld/figuren zeichnen
        icon_groesse = pygame.transform.scale(icon_path, (350+skalierung,350+skalierung))
        fenster.blit(icon_groesse, (150, 100))
        
        # Text zeichnen
        #status
        fenster.blit(status_text_surface, (30, 20))
        #wind_direction
        fenster.blit(wind_direction_text_surface, (100, 100))
        #wind_speed
        fenster.blit(wind_speed_text_surface, (100, 150))
        #temperature
        fenster.blit(temp_text_surface, (100, 300))
        #city
        fenster.blit(city_text_surface, (150, 400))
        
        # Fenster aktualisieren
        pygame.display.flip()
        clock.tick(FPS)
    
    #Wetter daten aktualisieren
    print('aktualisieren')
    
    icon_path = pygame.image.load(W.get_icon())
   
    status_text_surface = my_font.render(W.get_status(), False, (0, 0, 0))
    
    wind_direction, wind_speed = W.get_wind()
    wind_direction_text_surface = my_font.render(wind_direction, False, (0, 0, 0))
    wind_speed_text_surface = my_font.render(wind_speed, False, (0, 0, 0))
    
    temp_text_surface = my_font.render(W.get_temperature(), False, (0, 0, 0))
   
    city_text_surface = my_font.render(L.get_city(), False, (0, 0, 0))
    
