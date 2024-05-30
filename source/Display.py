import time
from weather import weather
import pygame
from pygame.locals import *
pygame.init()
w = weather()



# Variablen/KONSTANTEN setzen
FPS  = 400
WEISS   = ( 255, 255, 255)
spielaktiv = True

#icon
skalierung      = 0 
skalierungswert = 0.02

icon_path = pygame.image.load("weather_icons\cloudy.png")
bildgroessen = icon_path.get_rect()

#status text
my_font = pygame.font.SysFont('Comic Sans MS', 30)
status_text_surface = my_font.render(w.get_status(), False, (0, 0, 0))

#wind text
wind_direction, wind_speed = w.get_wind()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
wind_direction_text_surface = my_font.render(wind_direction, False, (0, 0, 0))
wind_speed_text_surface = my_font.render(wind_speed, False, (0, 0, 0))

#temperature
temp_speed_text_surface = my_font.render(w.get_temperature(), False, (0, 0, 0))

# Definieren und Öffnen eines neuen Fensters
fenster =pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Grafik skalieren")
clock = pygame.time.Clock()

# Schleife Hauptprogramm
while spielaktiv:
    start = time.time()
    end = start + 600
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
        fenster.blit(temp_speed_text_surface, (100, 300))
        
        
        # Fenster aktualisieren
        pygame.display.flip()
        clock.tick(FPS)
    
    #Wetter daten aktualisieren
    icon_path = pygame.image.load(w.get_icon())
    status_text_surface = my_font.render(w.get_status(), False, (0, 0, 0))
    wind_direction, wind_speed = w.get_wind()
    temp = w.get_temperature()
    
    
