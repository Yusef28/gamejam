import pygame
from pygame.locals import *
import tile_class
from tile_class import Tile

pygame.init()
screen_width, screen_height = (500,500)
screen = pygame.display.set_mode((500, 500))


green = (40,255,30)
brown = (40,60,90)
red =  (155,20,30)
yellow = (0,155,155)
white = (255,255,255)
blue = (0,0,255)
orange = (255,255,0)

grass = 0
dirt = 1
lava = 2
end = 3
moon = 4
ziel = 5

colours = {
    grass: green,
    dirt: brown,
    lava: red,
	end:white,
	moon:blue,
	ziel:orange
    }

tilemap = [
        [grass,dirt,lava,dirt,lava],
        [dirt,lava,dirt,dirt,dirt],
        [lava,ziel,dirt,dirt,lava],
        [lava, grass,dirt,dirt,grass],
        [dirt,dirt,dirt,dirt,grass]

        ]

		
TILESIZE = 100
MAPWIDTH =  5
MAPHEIGHT = 5


grass_tile_group = pygame.sprite.Group()
dirt_tile_group = pygame.sprite.Group()
lava_tile_group = pygame.sprite.Group()
end_tile_group = pygame.sprite.Group()
moon_tile_group = pygame.sprite.Group()
ziel_tile_group = pygame.sprite.Group()
all_tile_group = pygame.sprite.Group()

def create_moon_tile(x,y):
	tile_sprite = Tile(colours[moon], TILESIZE, TILESIZE, x*TILESIZE, y*TILESIZE)
	moon_tile_group.add(tile_sprite)	
	all_tile_group.add(tile_sprite)
	

def create_end_tile(x,y):
	tile_sprite = Tile(colours[end], TILESIZE, TILESIZE, x*TILESIZE, y*TILESIZE)
	end_tile_group.add(tile_sprite)	
	all_tile_group.add(tile_sprite)
	
def create_map():

	grass_tile_group.empty()
	dirt_tile_group.empty()
	lava_tile_group.empty()
	end_tile_group.empty()
	moon_tile_group.empty()
	ziel_tile_group.empty()
	all_tile_group.empty()

	for i, row in enumerate(tilemap):
		for j, tile in enumerate(row):

			if tile == 2:
				tile_sprite = Tile(colours[tile], TILESIZE,TILESIZE, j*TILESIZE, i*TILESIZE)
				lava_tile_group.add(tile_sprite)
			elif tile == 3:
				tile_sprite = Tile(colours[tile], TILESIZE,TILESIZE, j*TILESIZE, i*TILESIZE)
				end_tile_group.add(tile_sprite)
			elif tile == 5:
				tile_sprite = Tile(colours[tile], TILESIZE,TILESIZE, j*TILESIZE, i*TILESIZE)
				ziel_tile_group.add(tile_sprite)	
			else:
				tile_sprite = Tile(colours[tile], TILESIZE,TILESIZE, j*TILESIZE, i*TILESIZE)
			all_tile_group.add(tile_sprite)

	create_moon_tile(3,3)