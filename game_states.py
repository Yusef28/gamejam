import pygame
from pygame.locals import *

pygame.init()
screen_width, screen_height = (500,500)
screen = pygame.display.set_mode((500, 500))
pic = pygame.image.load("beispiel.png")  # You need an example picture in the same folder as this file!
running = True


TILESIZE = 100
MAPWIDTH =  5
MAPHEIGHT = 5


pygame.init()
screen = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

start_theme = "caketown 1.mp3"
spiel_theme = "Decision.mp3"
gestorben_theme = "Iwan Gabovitch - Dark Ambience Loop.mp3"
gewonnen_theme = "TownTheme.mp3"



pygame.font.init()
title_font = pygame.font.Font(None, 120)
subtitle_font = pygame.font.Font(None, 30)
	
#Start, Spiel, Gestorben, Gewonnen
SPIEL_ZUSTAND = "gewonnen"

def title_druck(title, subtitle):
	screen.fill((0, 0, 0))
	text0 = title_font.render(title, True, white)
	text1 = subtitle_font.render(subtitle, True, white)
	screen.blit(pygame.transform.scale(text0, text0.get_size()), \
	(screen_width/2-text0.get_size()[0]/2,screen_height/2-text0.get_size()[1]/2-80))
	screen.blit(pygame.transform.scale(text1, text1.get_size()), \
	(screen_width/2-text1.get_size()[0]/2,screen_height/2-text1.get_size()[1]/2))

def spiele_zustand_musik(theme_musik):
	PLAY_CHANNEL_1 = 1
	if pygame.mixer.Channel(PLAY_CHANNEL_1).get_busy() == False:
		musik = pygame.mixer.Sound('music/'+theme_musik)
		pygame.mixer.Channel(PLAY_CHANNEL_1).play(musik, -1)
	 

while running:
	pygame.event.pump()
	event = pygame.event.wait()
		
	if event.type == QUIT:
		running = False
		

	if SPIEL_ZUSTAND == "start":
		spiele_zustand_musik(start_theme)
		title_druck(SPIEL_ZUSTAND,"Druck leertaste fur nachst zustand")
		
	elif SPIEL_ZUSTAND == "spiel":
		spiele_zustand_musik(spiel_theme)
		title_druck(SPIEL_ZUSTAND,"Druck leertaste fur nachst zustand")
		
	elif SPIEL_ZUSTAND == "gestorben":
		spiele_zustand_musik(gestorben_theme)
		title_druck(SPIEL_ZUSTAND,"Druck leertaste fur nachst zustand")
		
	elif SPIEL_ZUSTAND == "gewonnen":
		spiele_zustand_musik(gewonnen_theme)
		title_druck(SPIEL_ZUSTAND,"Druck leertaste fur nachst zustand")
		
	pygame.display.update()
	
	
			