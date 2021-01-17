import pygame
from pygame.locals import *

class Tile(pygame.sprite.Sprite):

	def __init__(self, colour, width, height, x, y):
	
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)
		
		# Create an image of the block, and fill it with a color.
		# This could also be an image loaded from the disk.	
		self.image = pygame.Surface([width, height])
		self.image.fill(colour)
		self.colour = colour
		# Fetch the rectangle object that has the dimensions of the image
		# Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x
		self.state = (0,0)
		