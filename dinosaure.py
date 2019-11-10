import pygame
from pygame.locals import *
import math
import random

position_initial=(50,700)
taille_image=(100,100)
taille_ennemi=(700,500)
position_initial_ennemi=(1200,320)

class Dino(pygame.sprite.Sprite):												#créaction de la classe Dino 

	

	def __init__(self):													#attributs du Dino						

		pygame.sprite.Sprite.__init__(self)										#initialisation de sprite
		self.image = pygame.image.load("dino.png").convert_alpha() 				#choix de l'image
		self.image = pygame.transform.smoothscale(self.image, taille_image)		#dimensionne l'image
		self.rect = pygame.Rect(position_initial, self.image.get_size())        #création du rectangle de la taille de l'image
		
	def blit(self, fenetre):
		fenetre.blit(self.image, (self.rect.x, self.rect.y))

class Dino2(pygame.sprite.Sprite):

	def __init__(self):

		pygame.sprite.Sprite.__init__(self)		

		self.image = pygame.image.load("dino2.png").convert_alpha() 
		self.image = pygame.transform.smoothscale(self.image, taille_image)		
		self.rect = pygame.Rect(position_initial, self.image.get_size())          
		
	def blit(self, fenetre):
		fenetre.blit(self.image, (self.rect.x, self.rect.y))

class Dino3(pygame.sprite.Sprite):

	def __init__(self):

		pygame.sprite.Sprite.__init__(self)	

		self.image = pygame.image.load("dino3.png").convert_alpha() 
		self.image = pygame.transform.smoothscale(self.image, taille_image)
		self.rect = pygame.Rect(position_initial, self.image.get_size())           #création du rectangle de la taille de l'image
		
	def blit(self, fenetre):
		fenetre.blit(self.image, (self.rect.x, self.rect.y))

Dinos=[Dino, Dino2, Dino3]															#création d'une liste de classes


class Dino_ennemi(pygame.sprite.Sprite):											#créaction de la classe Dino_ennemi

	
	
	def __init__(self):																#attributs du Dino						

		pygame.sprite.Sprite.__init__(self)											#initialisation de sprite
		self.image = pygame.image.load("ennemi.png").convert_alpha() 				#choix de l'image
		self.image = pygame.transform.smoothscale(self.image, taille_ennemi)		#dimensionne l'image
		self.rect = pygame.Rect(position_initial_ennemi, self.image.get_size())     #création du rectangle de la taille de l'image
		
	def blit(self, fenetre):
		fenetre.blit(self.image, (self.rect.x, self.rect.y))


	def mouvement(self):
		
			
		self.rect.x=self.rect.x-1


class Mur(pygame.sprite.Sprite):   													#oeuf glissant (cactus) classe qui hérite de pygame.sprite.Sprite

	def __init__(self):

		pygame.sprite.Sprite.__init__(self)

		self.randomchoice1=random.choice([5, 10, 20])
		self.image = pygame.image.load("oeuf.png").convert_alpha()
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
		
		
		self.randomchoice1=random.choice([5, 10, 20])							#
		r1=random.random()
		self.rect.x = 2500+r1*1000
		self.rect.y = randomchoice3												#
				

class Mur2(pygame.sprite.Sprite):     											#oeuf volant (zozio) classe qui hérite de pygame.sprite.Sprite

	def __init__(self):

		pygame.sprite.Sprite.__init__(self)

		self.randomchoice2 = random.choice([2,2,3,5,5,6,7,10,20])
		self.image = pygame.image.load("oeuf.png").convert_alpha()
		self.image = pygame.transform.smoothscale(self.image,(self.image.get_width()//10, self.image.get_height()//10))
		self.rect = pygame.Rect((3000,450), self.image.get_size())          

	def mouvement(self, randomchoice2, temps):
		self.rect.x=self.rect.x-randomchoice2+1.5*math.cos(temps/500)*math.cos(temps/1000)*10		#permet la variation du point de départ de l'oeuf et randomise son déplacement "x"
		self.rect.y=250*math.cos((self.rect.x)/150)+250											#permet le mouvement sinusoïdal de l'oeuf

		if self.rect.x<=0:																		#si le rectangle sort de l'écran  (abscisse rect.x inferieur à 0) 
			self.reset()																		#Alors on appelle reset() qui redéplace le rectangle a une position aléatoire
			return True
		return False
		
	def reset(self):

		self.randomchoice2 = random.choice([2,2,3,5,5,6,7,10,20])   #valeur que peut prendre le déplacement "x"
		r2=random.random()
		self.rect.x=2000+r2*1000-self.randomchoice2          #permet de décaler l'apparition de l'oeuf de façon aléatoire à son apparition

class Mur3(pygame.sprite.Sprite):     											#oeuf volant (zozio) classe qui hérite de pygame.sprite.Sprite

	def __init__(self):

		pygame.sprite.Sprite.__init__(self)

		self.randomchoice3 = random.choice([2,2,3,5,5,6,7,10,20])
		self.image = pygame.image.load("oeuf.png").convert_alpha()
		self.image = pygame.transform.smoothscale(self.image,(self.image.get_width()//10, self.image.get_height()//10))
		self.rect = pygame.Rect((5000,450), self.image.get_size())          

	def mouvement(self, randomchoice3, temps):
		self.rect.x=self.rect.x-randomchoice3+2*math.sin(temps/1000)*math.cos(temps/500)*10		#permet la variation du point de départ de l'oeuf et randomise son déplacement "x"
		self.rect.y=250*math.sin((self.rect.x)/150)+450											#permet le mouvement sinusoïdal de l'oeuf

		if self.rect.x<=0:																		#si le rectangle sort de l'écran  (abscisse rect.x inferieur à 0) 
			self.reset()																		#Alors on appelle reset() qui redéplace le rectangle a une position aléatoire
			return True
		return False
		
	def reset(self):

		self.randomchoice3 = random.choice([2,2,3,5,5,6,7,10,20])   #valeur que peut prendre le déplacement "x"
		r3=random.random()
		self.rect.x=2000+r3*2000-self.randomchoice3          	#permet de décaler l'apparition de l'oeuf de façon aléatoire à son apparition

pygame.display.init()						                 	 #initialise tous mes modules pygame importés					
pygame.font.init()											 	 #initialisation du module font

fenetre = pygame.display.set_mode((0, 0))						#initialise une surface nommée fenetre avec set_mode(size=(0, 0), flags=0, depth=0, display=0) -> Surface
																#Si (0,0) est passé elle prend la résolution de l'écran courant

fond = pygame.image.load("foret2.jpg").convert()				#charge l'image et la converti dans un format spécifiqie à pygame
fond = pygame.transform.smoothscale(fond, (fond.get_width()//4, fond.get_height()//4))
fenetre = pygame.display.set_mode(fond.get_size(), RESIZABLE)	#création d'une fenêtre de la taille de l'image "fond"


fenetre.blit(fond, (0, 0))										#blit permet d'afficher la fenêtre fond à la position (0,0) (coin supérieur gauche)

font=pygame.font.Font(pygame.font.get_default_font(), 50)		#on instancie une objet de type pygame.font.Font avec comme paramètre pygame.font.get_default_font() qui renvoie un string de taille 50

perso =  pygame.sprite.GroupSingle()							#on instancie un container de type groupSingle qui ne peut contenir qu'un objet							
perso.add(Dino())												#on ajoute Dino() qui prend le paramètre (fond)
perso.draw(fenetre)												#On dessine le Dino sur la surface fenetre

cactus = Mur()													#on instancie cactus de type Mur
zozio = Mur2()													#on instancie zozio de type Mur2
zozio2 = Mur3()													#on instancie zozio2 de type Mur3
cactus_groupe = pygame.sprite.Group()     						#on instancie un container de type groupSingle qui ne peut contenir qu'une objet
cactus_groupe.add(cactus, zozio, zozio2)    					#On ajoute cactus et zozio dans ce container

ennemi = pygame.sprite.GroupSingle()										#on instancie l'ennemi
ennemi.add(Dino_ennemi())


#initialisation des variables
deplacement_vertical=10
i=1
compteur_de_point = 0
compteur_de_tour = 0
temps=0
surface_score=0
randomchoice1 = 10											#initialisation des 3 random
randomchoice2 = 10
randomchoice3 = 10
fin =  10000 + random.random()*100000						#temps de jeu aléatoire entre 10000ms et 110000ms
recul_ennemi=100
print(fin)


pygame.mixer.init()

sond_fond = pygame.mixer.Sound("9162.ogg")



sond_fond.play(100,0)								#100 loops, débute à t=0

pygame.key.set_repeat(40,10)								#répète l'event lorsque la touche est enfoncée

while temps<10000000:										#Début de la boucle de jeu
	
	pygame.time.Clock().tick(50)		

	

	temps =  pygame.time.get_ticks()

	#Définitions des surfaces de textes
	surface_temps = font.render(str(temps),True,(0,0,0))
	surface_font = font.render("Dinozoscore :" + str(compteur_de_point) +"/"+ str(compteur_de_tour), True, (0,0,0))
	surface_score = font.render("Temps de jeu écoulé, Dinozoscore :" + str(compteur_de_point) +"/"+ str(compteur_de_tour)+" en "+str(temps/1000)+" secondes", True, (0,0,0))
	surface_message1 = font.render("PAS TERRIBLE !!", True, (0,0,0))
	surface_message2 = font.render("BIEN JOUE !!", True, (0,0,0))
	surface_message3 = font.render("MOYEN !!", True, (0,0,0))
	surface_message4 = font.render("GAME OVER", True, (0,0,0))
	surface_message5 = font.render("Tu as quand même tenu " +str(temps/1000)+" secondes", True, (0,0,0))
	
	for event in pygame.event.get():						#gestion des évènements
		if event.type == QUIT:
			pygame.display.quit()
		elif event.type == KEYDOWN:
			if event.key == K_UP:
				perso.sprite.rect.y = perso.sprite.rect.y - deplacement_vertical
				if perso.sprite.rect.y<=0:
					perso.sprite.rect.y=0
			if event.key == K_DOWN:
				perso.sprite.rect.y = perso.sprite.rect.y + deplacement_vertical
				if perso.sprite.rect.y>=700:
					perso.sprite.rect.y=700
				# print(perso.sprite.rect.y)	
		
	fenetre.blit(fond,(0,0))            #affiche le fond
	
	cactus_groupe.draw(fenetre) 		#affiche les éléments du groupe sur la surface fenetre
	ennemi.draw(fenetre)				#affiche le dino ennemi

	for sprite in ennemi.sprites():
		if sprite.mouvement() == True:
			True

	for sprite in cactus_groupe.sprites():
		
			if sprite.mouvement(randomchoice1, temps) == True:
				compteur_de_tour+=1
				# print(compteur_de_tour)


	test = pygame.sprite.spritecollide(perso.sprite, cactus_groupe, False) #test la collision entre le rect "perso" et le rect "cactus"
	test_game_over = pygame.sprite.spritecollide(perso.sprite, ennemi, True) #test la collision entre le rect "perso" et le rect "ennemi"

	if len(test_game_over)>0:
		fenetre.blit(surface_message4,(600,400))          #affiche game over
		fenetre.blit(surface_message5,(300,500)) 
		pygame.display.flip()
		pygame.mixer.music.load("12468.ogg")				
		pygame.mixer.music.play()						#envoi la musique game over
		pygame.time.wait(5000)
		pygame.mixer.quit()
		pygame.display.quit()

	elif ennemi.sprite.rect.x<-100:
		fenetre.blit(surface_message4,(600,400)) 
		fenetre.blit(surface_message5,(300,500))          #affiche game over
		pygame.display.flip()
		pygame.mixer.music.load("12468.ogg")				
		pygame.mixer.music.play()						#envoi la musique game over
		pygame.time.wait(5000)
		pygame.mixer.quit()
		pygame.display.quit()

																	
	elif len(test)>0:
		choix_aleatoire_son=random.choice(["3739.ogg", "3739.ogg","3739.ogg" , "16925.ogg"])
												
		
		randomchoice1 = random.choice([5, 10, 20])
		randomchoice2 = random.choice([2,2,3,5,5,6,7,10,20])	
		randomchoice3 = random.choice([2,2,3,5,5,6,7,10,20])		
		
		for oeuf in test:
			compteur_de_point+=1
			compteur_de_tour+=1
			oeuf.reset()
			sond_oeuf = pygame.mixer.Sound(choix_aleatoire_son)
			sond_oeuf.play()
			# pygame.mixer.quit()
			# pygame.mixer.init()
			# pygame.mixer.music.load(choix_aleatoire_son)
			# print(randomchoice1,randomchoice2,randomchoice3)			
			# pygame.mixer.music.play()
			
			# pygame.time.Clock().tick(1000)

			# sond_fond = pygame.mixer.music.load("9162.mp3")
			# pygame.mixer.music.play(100,0)								#100 loops, débute à t=0



			ennemi.sprite.rect.x+=recul_ennemi
		perso.add(Dinos[2]())
		# perso.add(Dinos[i]())					#fait passer de dino à dino2 puis dino3
		# i=i+1
		# if i>2:
		# 	i=0										#retour à dino
	perso.draw(fenetre)

	fenetre.blit(surface_font,(0, 0))
	fenetre.blit(surface_temps,(1500,0))

	pygame.display.flip()

	
fenetre.blit(surface_score, (100,200))
pygame.display.flip()

pygame.time.wait(2000)
if compteur_de_point/compteur_de_tour>7/10:
	fenetre.blit(surface_message2,(600,400))
	pygame.display.flip()
elif compteur_de_point/compteur_de_tour<=1/2:
	fenetre.blit(surface_message1,(600,400))
	pygame.display.flip()
else:
	fenetre.blit(surface_message3,(600,400))
	pygame.display.flip()

pygame.time.wait(3000)
pygame.mixer.quit()
pygame.display.quit()

