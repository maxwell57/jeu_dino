import pygame
from pygame.locals import *

class Dino(pygame.sprite.Sprite):

	def __init__(self, fond):

		pygame.sprite.Sprite.__init__(self)		
		self.image = pygame.image.load("dino.png").convert_alpha() 
		self.image = pygame.transform.smoothscale(self.image,(200, 200))
		self.saut = False
		# self.perso_x = 50
		# self.perso_y = 680
		self.rect = pygame.Rect((50, 650), self.image.get_size())           #
		
	def sauter(self):
		if self.saut == True:
			return True

	def blit(self, fenetre):
		fenetre.blit(self.image, (self.rect.x, self.rect.y))

class Dino2(pygame.sprite.Sprite):

	def __init__(self, fond):

		pygame.sprite.Sprite.__init__(self)		
		self.image = pygame.image.load("dino2.png").convert_alpha() 
		self.image = pygame.transform.smoothscale(self.image,(200, 200))
		self.saut = False
		# self.perso_x = 50
		# self.perso_y = 680
		self.rect = pygame.Rect((50, 650), self.image.get_size())           #
		
	def sauter(self):
		if self.saut == True:
			return True

	def blit(self, fenetre):
		fenetre.blit(self.image, (self.rect.x, self.rect.y))

class Dino3(pygame.sprite.Sprite):

	def __init__(self, fond):

		pygame.sprite.Sprite.__init__(self)		
		self.image = pygame.image.load("dino3.png").convert_alpha() 
		self.image = pygame.transform.smoothscale(self.image,(200, 200))
		self.saut = False
		# self.perso_x = 50
		# self.perso_y = 680
		self.rect = pygame.Rect((50, 650), self.image.get_size())           #
		
	def sauter(self):
		if self.saut == True:
			return True

	def blit(self, fenetre):
		fenetre.blit(self.image, (self.rect.x, self.rect.y))

Dinos=[Dino, Dino2, Dino3]								#créer



class Mur(pygame.sprite.Sprite):

	def __init__(self):

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("carre.png").convert_alpha()
		self.image = pygame.transform.smoothscale(self.image,(self.image.get_width()//10, self.image.get_height()//10))
		self.rect = pygame.Rect((2100,740),self.image.get_size())

	def mouvement(self):
		# fenetre.blit(self.image, (self.rect.x, self.rect.y))
		self.rect.x=self.rect.x-5
		if self.rect.x<=0:
			self.rect.x=1000


	def reset(self):
		self.rect.x=1000

class Mur2(pygame.sprite.Sprite):

	def __init__(self):

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("carre.png").convert_alpha()
		self.image = pygame.transform.smoothscale(self.image,(self.image.get_width()//10, self.image.get_height()//10))
		self.rect = pygame.Rect((2200,450),self.image.get_size())          

	def mouvement(self):
		# fenetre.blit(self.image, (self.rect.x, self.rect.y))
		self.rect.x=self.rect.x-10
		if self.rect.x<=0:
			self.rect.x=1333		
    

	def reset(self):
		self.rect.x=1333



# def collision(rect1, rect2):						#definition de collision
# 	if rect1.right < rect2.left:
# 		print("ok")
# 		test=0
# 	elif rect1.bottom < rect2.top:      
# 		print("ok")
# 		test=0
# 	elif rect1.left > rect2.right:
# 		print("ok")
# 		test=0
# 	elif rect1.top > rect2.bottom:
# 		print("ok")
# 		test=0
# 	else:
# 		print("collision !!")
# 		test=1
# 	return test


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
perso =  pygame.sprite.GroupSingle(Dino(fond))
cactus_groupe = pygame.sprite.Group()
cactus = Mur()
perso.draw(fenetre)
zozio = Mur2()
cactus_groupe.add(cactus, zozio)
continuer=1
i=1
while continuer:
	
	pygame.time.Clock().tick(120)

	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0
		elif event.type == KEYUP:
			if event.key == K_SPACE:
				perso.sprite.rect.y=650
		elif event.type == KEYDOWN:
			if event.key == K_SPACE:
				perso.sprite.rect.move_ip(0,-200)
		
	

	fenetre.blit(fond,(0,0))
	
	# zozio.mouvement()
	# cactus.mouvement()
	# cactus.blit(fenetre)
	# zozio.blit(fenetre)
	cactus_groupe.draw(fenetre)
	for sprite in cactus_groupe.sprites():
		sprite.mouvement()
	test = pygame.sprite.spritecollide(perso.sprite,cactus_groupe,False) #test la collision entre le rect "perso" et le rect "cactus"
	print(test)																		#revoie une liste de sprite
	if len(test)>0:
		for oeuf in test:
			oeuf.reset()
		perso.add(Dinos[i](fond))
		i=i+1
		if i>2:
			i=0
	perso.draw(fenetre)


	pygame.display.flip()



pygame.display.quit()