import pygame
from pygame.locals import *
import os
import player_class
from player_class import Player
import tile_class
from tile_class import Tile

import map_setup
from map_setup import *


my_absolute_dirpath = os.path.abspath(os.path.dirname(__file__))


pygame.init()


screen = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))


start_theme = "Decision.mp3"
spiel_theme = "Caketown 1.mp3"
gestorben_theme = "Iwan Gabovitch - Dark Ambience Loop.mp3"
gewonnen_theme = "TownTheme.mp3"

pygame.font.init()
title_font = pygame.font.Font(None, 120)
subtitle_font = pygame.font.Font(None, 30)
	

SPIEL_ZUSTAND = "start" # Start, Spiel, Gestorben, Gewonnen
PLAY_CHANNEL_1 = 1 #background_music



def title_druck(title, subtitle):
	screen.fill((0, 0, 0))
	text0 = title_font.render(title, True, white)
	text1 = subtitle_font.render(subtitle, True, white)
	screen.blit(pygame.transform.scale(text0, text0.get_size()), \
	(screen_width/2-text0.get_size()[0]/2,screen_height/2-text0.get_size()[1]/2-80))
	screen.blit(pygame.transform.scale(text1, text1.get_size()), \
	(screen_width/2-text1.get_size()[0]/2,screen_height/2-text1.get_size()[1]/2))

def spiele_zustand_musik(theme_musik):
	#PLAY_CHANNEL_1 = 1
	if pygame.mixer.Channel(PLAY_CHANNEL_1).get_busy() == False:
		musik = pygame.mixer.Sound(my_absolute_dirpath + '/music/'+theme_musik)
		pygame.mixer.Channel(PLAY_CHANNEL_1).play(musik, -1)
	 

running = True
while running:

	if SPIEL_ZUSTAND == "start":
		spiele_zustand_musik(start_theme)
		title_druck(SPIEL_ZUSTAND,"Druck leertaste fur nachst zustand")
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:	
				running = False
				
			if event.type == pygame.KEYDOWN:
				if event.key == K_SPACE:
					SPIEL_ZUSTAND = 'spiel'
					create_map()

					pygame.mixer.Channel(PLAY_CHANNEL_1).fadeout(1000)
		
					player = Player((233, 10, 100), 50,50)
					player_group = pygame.sprite.GroupSingle()
					player_group.add(player)
	
	elif SPIEL_ZUSTAND == "spiel":
		
		pygame.time.delay(20)
		#spiele_zustand_musik(spiel_theme)
		
		for event in pygame.event.get():
		
			if event.type == pygame.QUIT:	
				running = False
			
		keys = pygame.key.get_pressed()
			
			
		if keys[pygame.K_DOWN]:
			player.state = (0,2)
		elif keys[pygame.K_UP]:
			player.state = (0,-2)
		elif keys[pygame.K_LEFT]:
			player.state = (-2,0)
		elif keys[pygame.K_RIGHT]:
			player.state = (2,0)
		else:
			player.state = (0,0)
		
				
		player.rect.x += player.state[0]
		player.rect.y += player.state[1]
		
		if pygame.sprite.spritecollideany(player, lava_tile_group):
			player.rect.x -= player.state[0]
			player.rect.y -= player.state[1]
		
		
		moon = pygame.sprite.spritecollideany(player, moon_tile_group)
		if moon:
			moon.rect.x += player.state[0]
			moon.rect.y += player.state[1]
			
			if pygame.sprite.spritecollideany(moon, lava_tile_group):
			
				player.rect.x -= player.state[0]
				player.rect.y -= player.state[1]
				moon.rect.x -= player.state[0]
				moon.rect.y -= player.state[1]
				
			if pygame.sprite.spritecollide(moon, \
			ziel_tile_group, \
			False, \
			pygame.sprite.collide_circle_ratio(0.5)):
				#moon.kill()
				create_end_tile(3,0)
			
		if pygame.sprite.spritecollide(player,\
		end_tile_group,\
		False,\
		pygame.sprite.collide_circle_ratio(0.5)):
			SPIEL_ZUSTAND = 'gewonnen'
			
		screen.fill((0, 0, 0))
		s_breit = 0
		s_hohe = 0
		

		for tile in all_tile_group:
			pygame.draw.rect(screen, tile.colour, tile.rect)
		
		
			
		#screen.blit(pygame.transform.scale(player.image, (TILESIZE,TILESIZE)), (player.rect.x,player.rect.y))
		pygame.draw.rect(screen, (10,100,10), player.rect)
		
	elif SPIEL_ZUSTAND == "gestorben":
		spiele_zustand_musik(gestorben_theme)
		title_druck(SPIEL_ZUSTAND,"Druck leertaste fur nachst zustand")
		for event in pygame.event.get():
			if event.type == pygame.QUIT:	
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == K_SPACE:
					SPIEL_ZUSTAND = 'start'
					pygame.mixer.Channel(PLAY_CHANNEL_1).fadeout(10)
		
	elif SPIEL_ZUSTAND == "gewonnen":
		#spiele_zustand_musik(gewonnen_theme)
		title_druck(SPIEL_ZUSTAND,"Druck leertaste fur nachst zustand")
		for event in pygame.event.get():
			if event.type == pygame.QUIT:	
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == K_SPACE:
					SPIEL_ZUSTAND = 'start'
					pygame.mixer.Channel(PLAY_CHANNEL_1).fadeout(10)
		
	
	pygame.display.update()

