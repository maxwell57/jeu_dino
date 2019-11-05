import pygame
from pygame.locals import *

class Dino():

	def __init__(self, fond):
		
		self.perso = pygame.image.load("dino.png").convert_alpha() 
		self.perso = pygame.transform.smoothscale(self.perso,(self.perso.get_width()//5, self.perso.get_height()//5))
		self.saut = False
		# self.perso_x = 50
		# self.perso_y = 680
		self.rectangle = pygame.Rect((50, 650), self.perso.get_size())           #creation du rectangle de perso
		
	def sauter(self):
		if self.saut == True:
			return True

	def blit(self, fenetre):
		fenetre.blit(self.perso, (self.rectangle.x, self.rectangle.y))

class Mur():

	def __init__(self):

		self.cactus = pygame.image.load("carre.png").convert_alpha()
		self.cactus = pygame.transform.smoothscale(self.cactus,(self.cactus.get_width()//10, self.cactus.get_height()//10))
		self.taille_mur = pygame.Rect((1000,740),self.cactus.get_size())          #création du rectangle de cactus

	def blit(self, fenetre):
		fenetre.blit(self.cactus, (self.taille_mur.x, self.taille_mur.y))
		self.taille_mur.x=self.taille_mur.x-1
		if self.taille_mur.x<=0:
			self.taille_mur.x=1000

class Mur2():

	def __init__(self):

		self.zozio = pygame.image.load("carre.png").convert_alpha()
		self.zozio = pygame.transform.smoothscale(self.zozio,(self.zozio.get_width()//10, self.zozio.get_height()//10))
		self.taille_zozio = pygame.Rect((1500,450),self.zozio.get_size())          #création du rectangle de zozio

	def blit(self, fenetre):
		fenetre.blit(self.zozio, (self.taille_zozio.x, self.taille_zozio.y))
		self.taille_zozio.x=self.taille_zozio.x-1
		if self.taille_zozio.x<=0:
			self.taille_zozio.x=1500			

def collision(rectangle, taille_mur):	
	if rectangle.right < taille_mur.left:
		print("ok")
		test=0
	elif rectangle.bottom < taille_mur.top:
		print("ok")
		test=0
	elif rectangle.left > taille_mur.right:
		print("ok")
		test=0
	elif rectangle.top > taille_mur.bottom:
		print("ok")
		test=0
	else:
		print("collision !!")
		test=1
	return test

		


	



pygame.display.init()

#ouverture de la fenêtre pygame.

fenetre = pygame.display.set_mode((0, 0))

fond = pygame.image.load("foret2.jpg").convert()
fond = pygame.transform.smoothscale(fond, (fond.get_width()//4, fond.get_height()//4))
fenetre = pygame.display.set_mode(fond.get_size(), RESIZABLE)

fenetre.blit(fond,(0,0))

# perso = pygame.image.load("dino.png").convert_alpha() 
# perso = pygame.transform.smoothscale(perso,(fond.get_width()//5,fond.get_height()//5)).
# perso_x=50
# perso_y=680
perso = Dino(fond)
cactus = Mur()
perso.blit(fenetre)
zozio = Mur2()

continuer=1
while continuer:
	
	pygame.time.Clock().tick(1000)

	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0

		elif event.type == KEYDOWN:
			if event.key == K_SPACE:
				perso.rectangle.move_ip(0,-200)
		elif event.type == KEYUP:
			if event.key == K_SPACE:
				perso.rectangle.move_ip(0,+200)
	

	fenetre.blit(fond,(0,0))
	perso.blit(fenetre)
	cactus.blit(fenetre)
	zozio.blit(fenetre)
	test=collision(perso.rectangle, cactus.taille_mur) #test la collision entr le rectangle "perso" et le rectangle "cactus"
	
	# if test==1:
	# 	break
	



	pygame.display.flip()



pygame.display.quit()