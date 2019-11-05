import pygame
from pygame.locals import *

pygame.init()

#ouverture de la fenêtre pygame

fenetre = pygame.display.set_mode((0, 0))

fond = pygame.image.load("foret1.jpg").convert()
fond = pygame.transform.smoothscale(fond,(fond.get_width()//5,fond.get_height()//5)) 
fenetre = pygame.display.set_mode(fond.get_size(),RESIZABLE)

fenetre.blit(fond,(0,0))

perso = pygame.image.load("dino.png").convert_alpha() 
perso = pygame.transform.smoothscale(perso,(fond.get_width()//5,fond.get_height()//5))
perso_x=50
perso_y=550
fenetre.blit(perso, (perso_x,perso_y))

continuer=1
while continuer:

	pygame.time.Clock().tick(30)

	for event in pygame.event.get():
		if event.type==QUIT:
			continuer=0

	pygame.display.flip()

pygame.display.quit()