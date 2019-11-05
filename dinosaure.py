import pygame
from pygame.locals import *

class Dino():

	def __init__(self, y):
		self.perso = pygame.image.load("dino.png").convert_alpha() 
		self.perso = pygame.transform.smoothscale(perso,(fond.get_width()//5,fond.get_height()//5))
		self.y = y
		self.saut = False
		self.perso_x=50
		self.perso_y=680
		
	def sauter(self):
		if self.saut == True:
			return True



pygame.init()

#ouverture de la fenêtre pygame.

fenetre = pygame.display.set_mode((0, 0))

fond = pygame.image.load("foret1.jpg").convert()
fond = pygame.transform.smoothscale(fond,(fond.get_width()//4,fond.get_height()//4)) 
fenetre = pygame.display.set_mode(fond.get_size(),RESIZABLE)

fenetre.blit(fond,(0,0))

perso = pygame.image.load("dino.png").convert_alpha() 
perso = pygame.transform.smoothscale(perso,(fond.get_width()//5,fond.get_height()//5))
perso_x=50
perso_y=680

fenetre.blit(perso, (perso_x,perso_y))



continuer=1
while continuer:

	pygame.time.Clock().tick(30)


	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0

		elif event.type == KEYDOWN:
			if event.key == K_SPACE:
				continuer=1	


	pygame.display.flip()

pygame.display.quit()