import pygame
from pygame.locals import *

pygame.init()
screen_width, screen_height = (500,500)
screen = pygame.display.set_mode((500, 500))
running = True

uhr = pygame.time.Clock()

class SpriteSheet:

	def __init__(self, filename):
		self.sheet = pygame.image.load(filename).convert()
		self.sprite_list = []


	def image_at(self, rectangle, colorkey = (255,255,255)):
		# Loads image from x, y, x+offset, y+offset.
		rect = pygame.Rect(rectangle)
		image = pygame.Surface(rect.size).convert()
		image.blit(self.sheet, (0, 0), rect)
		if colorkey is not None:
			if colorkey is -1:
				colorkey = image.get_at((0,0))
			image.set_colorkey(colorkey, pygame.RLEACCEL)
		return image
		
	def images_at(self, range_x, range_y):
		for dy in range(range_y):
			for dx in range(range_x):
				teil_dimentions = (52*dy, 72*dx, 52, 72)
				tile = piece_ss.image_at(teil_dimentions)
				self.sprite_list.append(tile)	
	
pygame.init()


filename = 'images/bonus1_full.png'
piece_ss = SpriteSheet(filename)
piece_ss.images_at(4,3)
#print(piece_ss.sprite_list)
#teil_dimentions = (0, 0, 52, 72)
#teil_bild = piece_ss.image_at(teil_dimentions)


gehe_links = [piece_ss.sprite_list[0+1], piece_ss.sprite_list[8+1]]
gehe_rechts = [piece_ss.sprite_list[0+2], piece_ss.sprite_list[8+2]]
gehe_unten = [piece_ss.sprite_list[0], piece_ss.sprite_list[8]]
gehe_oben = [piece_ss.sprite_list[0+3], piece_ss.sprite_list[8+3]]
halt_links = piece_ss.sprite_list[5]
halt_rechts = piece_ss.sprite_list[6]
halt_unten = piece_ss.sprite_list[4]
halt_oben = piece_ss.sprite_list[7]

schritt = 1
schritt_zeit = 0
while running:
	pygame.event.pump()
	#event = pygame.event.wait()

	for event in pygame.event.get():

		if event.type == QUIT:
			running = False
	
	screen.fill((0, 0, 0))
	
	schritt_zeit += 1
	if schritt_zeit >= 7:
		schritt_zeit = 0
		schritt = 0 if schritt else 1
		
	teil_bild = halt_unten
	teil_rect = teil_bild.get_rect()
	teil_rect.topleft = 250-26, 250-72
	screen.blit(teil_bild, teil_rect)

	pygame.display.update()
	uhr.tick(30)
	
			