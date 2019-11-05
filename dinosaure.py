import pygame
from pygame.locals import *

class Dino():

	def __init__(self, fond):
		self.perso = pygame.image.load("dino.png").convert_alpha() 
		self.perso = pygame.transform.smoothscale(self.perso,(self.perso.get_width()//5,self.perso.get_height()//5))
		self.saut = False
		# self.perso_x = 50
		# self.perso_y = 680
		self.rectangle = pygame.Rect((50,650),self.perso.get_size())
		
	def sauter(self):
		if self.saut == True:
			return True

	def blit(self, fenetre):
		fenetre.blit(self.perso, (self.rectangle.x, self.rectangle.y))



pygame.display.init()

#ouverture de la fenêtre pygame.

fenetre = pygame.display.set_mode((0, 0))

fond = pygame.image.load("foret1.jpg").convert()
fond = pygame.transform.smoothscale(fond,(fond.get_width()//4,fond.get_height()//4)) 
fenetre = pygame.display.set_mode(fond.get_size(),RESIZABLE)

fenetre.blit(fond,(0,0))

# perso = pygame.image.load("dino.png").convert_alpha() 
# perso = pygame.transform.smoothscale(perso,(fond.get_width()//5,fond.get_height()//5))
# perso_x=50
# perso_y=680
perso = Dino(fond)
perso.blit(fenetre)

continuer=1
while continuer:

	pygame.time.Clock().tick(30)


	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0

		elif event.type == KEYDOWN:
			if event.key == K_SPACE:
				perso.rectangle.move_ip(0,-50)

	fenetre.blit(fond,(0,0))
	perso.blit(fenetre)
	pygame.display.flip()


pygame.display.quit()