import pygame
from pygame.locals import *
import math
import random

class Dino(pygame.sprite.Sprite):



	def __init__(self, fond):

		pygame.sprite.Sprite.__init__(self)		
		self.image = pygame.image.load("dino.png").convert_alpha() 
		self.image = pygame.transform.smoothscale(self.image,(200, 200))
		self.saut = False
		# self.perso_x = 50
		# self.perso_y = 680
		self.rect = pygame.Rect((50, 630), self.image.get_size())           #
		
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
		self.rect = pygame.Rect((50, 630), self.image.get_size())           #
		
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
		self.rect = pygame.Rect((50, 630), self.image.get_size())           #
		
	def sauter(self):
		if self.saut == True:
			return True

	def blit(self, fenetre):
		fenetre.blit(self.image, (self.rect.x, self.rect.y))

Dinos=[Dino, Dino2, Dino3]								#créer

 # renvoie un élément au hasard.



class Mur(pygame.sprite.Sprite):   #oeuf glissant

	def __init__(self):

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("carre.png").convert_alpha()
		self.image = pygame.transform.smoothscale(self.image,(self.image.get_width()//10, self.image.get_height()//10))
		self.rect = pygame.Rect((2000, 740), self.image.get_size())

	def mouvement(self):
		# fenetre.blit(self.image, (self.rect.x, self.rect.y))
		self.rect.x=self.rect.x-randomchoice1
		if self.rect.x<=0:
			self.rect.x=2000

		


	def reset(self):
		r1=random.random()
		self.rect.x = 2500+r1*1000
		self.rect.y = randomchoice3

class Mur2(pygame.sprite.Sprite):     #oeuf volant

	def __init__(self):

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("carre.png").convert_alpha()
		self.image = pygame.transform.smoothscale(self.image,(self.image.get_width()//10, self.image.get_height()//10))
		self.rect = pygame.Rect((2500,450), self.image.get_size())          

	def mouvement(self):
		# fenetre.blit(self.image, (self.rect.x, self.rect.y))
		
		self.rect.x=self.rect.x-randomchoice2
		
		self.rect.y=250*math.cos((self.rect.x)/150)+250

		# print((self.rect.x,self.rect.y)) # affiche les coordonnées du mur 2 à chaque frame
		if self.rect.x<=0:
			self.rect.x=2500	
    

	def reset(self):
		r2=random.random()
		self.rect.x=2000+r2*1000-randomchoice2


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

pygame.font.init()


#ouverture de la fenêtre pygame.

fenetre = pygame.display.set_mode((0, 0))

fond = pygame.image.load("foret2.jpg").convert()
fond = pygame.transform.smoothscale(fond, (fond.get_width()//4, fond.get_height()//4))
fenetre = pygame.display.set_mode(fond.get_size(), RESIZABLE)


fenetre.blit(fond,(0,0))

font=pygame.font.Font(pygame.font.get_default_font(),50)




# myfont = pygame.font.SysFont("monospace", 16)
# score_display = myfont.render(score, 1, (0,0,0))
# screen.blit(score_display, (100, 100))

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
randomchoice1 = 10
randomchoice2 = 10
randomchoice3 = 740
compteur_de_point=0



while continuer:
	
	pygame.time.Clock().tick(100)
	surface_font=font.render("Dinozoscore :" + str(compteur_de_point), True, (255,0,0))

	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0
		elif event.type == KEYUP:
			if event.key == K_SPACE:
				perso.sprite.rect.y=430
		elif event.type == KEYDOWN:
			if event.key == K_SPACE:
				perso.sprite.rect.move_ip(0,-400)
		
	

	fenetre.blit(fond,(0,0))
	
	# zozio.mouvement()
	# cactus.mouvement()
	# cactus.blit(fenetre)
	# zozio.blit(fenetre)

	cactus_groupe.draw(fenetre)
	for sprite in cactus_groupe.sprites():
		
			sprite.mouvement()
	test = pygame.sprite.spritecollide(perso.sprite,cactus_groupe,False) #test la collision entre le rect "perso" et le rect "cactus"
	# print(test)	

	#r=random.randint(0, 1)
																		#revoie une liste de sprite
	if len(test)>0:
		randomchoice1 = random.choice([5,10, 20])
		randomchoice2 = random.choice([5,10, 20])		
		randomchoice3 = random.choice([740,600,300,150])
		# print((randomchoice1, randomchoice2, randomchoice3))
		compteur_de_point+=1
		print(compteur_de_point)
		for oeuf in test:
			# chance=random.randint(0, 1)
			# print(chance)
			# if chance == 1:
			oeuf.reset()
		perso.add(Dinos[i](fond))
		i=i+1
		if i>2:
			i=0
	perso.draw(fenetre)

	fenetre.blit(surface_font,(0,0))
	pygame.display.flip()

	


pygame.display.quit()

# if rock.x < 0:
#     y = random.randint(0, 400)    #essai random
#     rock = Rock(640, y)

# rock.rock()