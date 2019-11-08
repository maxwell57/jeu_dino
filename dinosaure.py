import pygame
from pygame.locals import *
import math
import random

position_initial=(50,630)
taille_image=(200,200)

class Dino(pygame.sprite.Sprite):												#créaction de la classe Dino 



	def __init__(self, fond):													#attributs du Dino						

		pygame.sprite.Sprite.__init__(self)										#initialisation de sprite
		self.image = pygame.image.load("dino.png").convert_alpha() 				#choix de l'image
		self.image = pygame.transform.smoothscale(self.image, taille_image)		#dimensionne l'image
		self.rect = pygame.Rect(position_initial, self.image.get_size())        #création du rectangle de la taille de l'image
		
	def blit(self, fenetre):
		fenetre.blit(self.image, (self.rect.x, self.rect.y))

class Dino2(pygame.sprite.Sprite):

	def __init__(self, fond):

		pygame.sprite.Sprite.__init__(self)		

		self.image = pygame.image.load("dino2.png").convert_alpha() 
		self.image = pygame.transform.smoothscale(self.image, taille_image)
		self.saut = False
		self.rect = pygame.Rect(position_initial, self.image.get_size())          
		
	def blit(self, fenetre):
		fenetre.blit(self.image, (self.rect.x, self.rect.y))

class Dino3(pygame.sprite.Sprite):

	def __init__(self, fond):

		pygame.sprite.Sprite.__init__(self)	

		self.image = pygame.image.load("dino3.png").convert_alpha() 
		self.image = pygame.transform.smoothscale(self.image, taille_image)
		self.saut = False
		self.rect = pygame.Rect(position_initial, self.image.get_size())           #création du rectangle de la taille de l'image
		
	def blit(self, fenetre):
		fenetre.blit(self.image, (self.rect.x, self.rect.y))

Dinos=[Dino, Dino2, Dino3]															#création d'une liste de classes


class Mur(pygame.sprite.Sprite):   													#oeuf glissant (cactus) classe qui hérite de pygame.sprite.Sprite

	def __init__(self):

		pygame.sprite.Sprite.__init__(self)

		self.randomchoice1=random.choice([5, 10, 20])
		self.image = pygame.image.load("carre.png").convert_alpha()
		self.image = pygame.transform.smoothscale(self.image, (self.image.get_width()//10, self.image.get_height()//10))
		self.rect = pygame.Rect((2000, 740), self.image.get_size())

	def mouvement(self, randomchoice1, temps):
				
		self.rect.x=self.rect.x-randomchoice1
		if self.rect.x<=0:
			self.reset()
			return True
		return False
		
	def reset(self):															

		randomchoice3 = random.choice([740, 600, 300, 150])						#initialisation des valeurs possibles de "y" pour l'oeuf
		
		r1=random.random()
		self.randomchoice1=random.choice([5, 10, 20])							#initialisation des valeurs possibles de 
		self.rect.x = 2500+r1*1000
		self.rect.y = randomchoice3												#
				

class Mur2(pygame.sprite.Sprite):     											#oeuf volant (zozio) classe qui hérite de pygame.sprite.Sprite

	def __init__(self):

		pygame.sprite.Sprite.__init__(self)

		self.randomchoice2 = random.choice([5, 10, 20])
		self.image = pygame.image.load("carre.png").convert_alpha()
		self.image = pygame.transform.smoothscale(self.image,(self.image.get_width()//10, self.image.get_height()//10))
		self.rect = pygame.Rect((2500,450), self.image.get_size())          

	def mouvement(self, randomchoice2, temps):
		self.rect.x=self.rect.x-randomchoice2+math.cos(temps/1000)*math.cos(temps/1000)*10		#permet la variation du point de départ de l'oeuf et randomise son déplacement "x"
		self.rect.y=250*math.cos((self.rect.x)/150)+250											#permet le mouvement sinusoïdal de l'oeuf

		if self.rect.x<=0:																		#si le rectangle sort de l'écran  (abscisse rect.x inferieur à 0) 
			self.reset()																		#Alors on appelle reset() qui redéplace le rectangle a une position aléatoire
			return True
		return False
		
	def reset(self):

		self.randomchoice2 = random.choice([5,6,7,8,9,10])   #valeur que peut prendre le déplacement "x"
		r2=random.random()
		self.rect.x=2000+r2*1000-self.randomchoice2          #permet de décaler l'apparition de l'oeuf de façon aléatoire à son apparition

pygame.display.init()						                  #initialise tous mes modules pygame importés					
pygame.font.init()											  #initialisation du module font

fenetre = pygame.display.set_mode((0, 0))					#initialise une surface nommée fenetre avec set_mode(size=(0, 0), flags=0, depth=0, display=0) -> Surface
															#Si (0,0) est passé elle prend la résolution de l'écran courant

fond = pygame.image.load("foret2.jpg").convert()			#charge l'image et la converti dans un format spécifiqie à pygame
fond = pygame.transform.smoothscale(fond, (fond.get_width()//4, fond.get_height()//4))
fenetre = pygame.display.set_mode(fond.get_size(), RESIZABLE)	#création d'une fenêtre de la taille de l'image "fond"


fenetre.blit(fond, (0, 0))										#blit permet d'afficher la fenêtre fond à la position (0,0) (coin supérieur gauche)

font=pygame.font.Font(pygame.font.get_default_font(), 50)		#on instancie une objet de type pygame.font.Font avec comme paramètre pygame.font.get_default_font() qui renvoie un string de taille 50

perso =  pygame.sprite.GroupSingle()							#on instancie un container de type groupSingle qui ne peut contenir qu'un objet							
perso.add(Dino(fond))											#on ajoute Dino() qui prend le paramètre (fond)
perso.draw(fenetre)												#On dessine le Dino sur la surface fenetre

cactus = Mur()													#on instancie cactus de type Mur
zozio = Mur2()													#on instancie zozio de type Mur2

cactus_groupe = pygame.sprite.Group()     						#on instancie un container de type groupSingle qui ne peut contenir qu'une objet
cactus_groupe.add(cactus, zozio)    							#On ajoute cactus et zozio dans ce container

#initialisation des variables
i=1
compteur_de_point = 0
compteur_de_tour = 0
temps=0
surface_score=0
randomchoice1 = random.choice([5, 10, 20])					#initialisation des 2 random
randomchoice2 = random.choice([5, 10, 20])
fin = 30000+random.random()*100000							#temps de jeu aléatoire entre 30000ms et 120000ms
print(fin)
while temps<fin:											#Début de la boucle de jeu
	
	pygame.time.Clock().tick(75)							

	temps =  pygame.time.get_ticks()

	#Définitions des surfaces de textes
	surface_temps=font.render(str(temps),True,(0,0,0))
	surface_font=font.render("Dinozoscore :" + str(compteur_de_point) +"/"+ str(compteur_de_tour), True, (0,0,0))
	surface_score=font.render("Temps de jeu écoulé, Dinozoscore :" + str(compteur_de_point) +"/"+ str(compteur_de_tour)+" en "+str(temps/1000)+" secondes", True, (0,255,0))
	surface_message = font.render("PAS TERRIBLE !!", True, (0,0,0))

	for event in pygame.event.get():								#gestion des évènements
		if event.type == QUIT:
			pygame.display.quit()
		elif event.type == KEYUP:
			if event.key == K_SPACE:
				perso.sprite.rect.y=430
		elif event.type == KEYDOWN:
			if event.key == K_SPACE:
				perso.sprite.rect.move_ip(0,-400)
		
	fenetre.blit(fond,(0,0))            #affiche le fond
	
	cactus_groupe.draw(fenetre) 		#affiche les éléments du groupe sur la surface fenetre

	for sprite in cactus_groupe.sprites():
		
			if sprite.mouvement(randomchoice1, temps) == True:
				compteur_de_tour+=1
				print(compteur_de_tour)


	test = pygame.sprite.spritecollide(perso.sprite, cactus_groupe, False) #test la collision entre le rect "perso" et le rect "cactus"
																			
	if len(test)>0:
		
		randomchoice1 = random.choice([5, 10, 20])
		randomchoice2 = random.choice([5, 10, 20])			
		
		for oeuf in test:
			compteur_de_point+=1
			oeuf.reset()
			compteur_de_tour+=1
			
		perso.add(Dinos[i](fond))
		i=i+1
		if i>2:
			i=0
	perso.draw(fenetre)

	fenetre.blit(surface_font,(0, 0))
	fenetre.blit(surface_temps,(1000,0))

	pygame.display.flip()

	
fenetre.blit(surface_score, (200,200))
pygame.display.flip()

pygame.time.wait(2000)

fenetre.blit(surface_message,(800,400))
pygame.display.flip()

pygame.time.wait(3000)

pygame.display.quit()

