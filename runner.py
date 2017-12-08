#!/usr/bin/env python

import sys, pygame, time, math, glob
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

screen_size = (800,600)
FPS = 60
gravity = (0.0, 3.0)

def add_vectors(vect1, vect2):
	""" Returns the sum of two vectors """
	(angle1, length1) = vect1
	(angle2, length2) = vect2
	x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
	y  = math.cos(angle1) * length1 + math.cos(angle2) * length2	
	angle  = 0.5 * math.pi - math.atan2(y, x)
	length = math.hypot(x, y)
	return (angle, length)


class World(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.background_images = self.running_images = glob.glob("resources/background/bg*.png")
		self.background_images.sort()
		self.background = []
		w,h = screen_size
		for b in self.background_images:
			img = pygame.image.load(b)
			r = img.get_rect()
			temp = [img,(0,r.height-h,w,r.height-h)]
			self.background.append(temp)
		self.rect = pygame.Rect((0,0,w,h))
		self.image = pygame.Surface(self.rect.size).convert()
		self.image.blit(self.background[0][0], (0,0), self.background[0][1])
		self.image.blit(self.background[1][0], (0,0), self.background[1][1])
		self.image.blit(self.background[2][0], (0,0), self.background[2][1])
		self.image.blit(self.background[3][0], (0,0), self.background[3][1])
		self.image.blit(self.background[4][0], (0,0), self.background[4][1])
	
	def update(self,speed):
		speedx,speedy = speed
		px,py = (0,0)
		w,h = screen_size		
		for i in range(0,len(self.background)):
			b = self.background[i]
			r = b[0].get_rect()
			(x1,y1,x2,y2) = b[1]
			x1 += px
			x2 += px
			y1 += py
			y2 += py
			while x1 < 0:
				x1 += w
				x2 += w
			while x2 > r.width:
				x1 -= w
				x2 -= w
			self.background[i][1] = (x1,y1,x2,y2)
			px += speedx
			py += speedy
		self.image.blit(self.background[0][0], (0,0), self.background[0][1])
		self.image.blit(self.background[1][0], (0,0), self.background[1][1])
		self.image.blit(self.background[2][0], (0,0), self.background[2][1])
		self.image.blit(self.background[3][0], (0,0), self.background[3][1])
		self.image.blit(self.background[4][0], (0,0), self.background[4][1])
		
		

class Player(pygame.sprite.Sprite):
	# sprite images are curtesy of Bevouliin (http://bevouliin.com)
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.running_images = glob.glob("resources/character/r_*.png")
		self.running_images.sort()
		self.running = []
		for r in self.running_images:
			temp = pygame.image.load(r)
			self.running.append(temp)
		self.running_frame = 0
		self.image = self.running[self.running_frame]
		self.rect = self.image.get_rect()
		self.rect.x = 50
		self.rect.y = 442
		self.speed = (5,0)
		self.falling = False
	
	def update(self):
		self.running_frame = (self.running_frame + 1) % len(self.running)
		self.image = self.running[self.running_frame]
		if self.falling:
			self.speed = add_vectors(self.speed,gravity)
	


def main():
	pygame.init()
	screen = pygame.display.set_mode(screen_size)
	clock = pygame.time.Clock()

	world = pygame.sprite.Group()
	world.add(World())
	player = Player()
	players = pygame.sprite.Group()
	players.add(player)

	while True:
		clock.tick(FPS)
		screen.fill((0,0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
			if event.type == pygame.MOUSEMOTION:
				pos = pygame.mouse.get_pos()
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
			if event.type == pygame.KEYDOWN:
				keys = pygame.key.get_pressed()

if event.type == pygame.KEYDOWN:
		key = pygame.key.get_pressed(up)
	def __init__(self):
			pygame.sprite.Sprite.__init__(self)
			self.jumping_images = glob.glob("resources/character/r_*.png")
			self.jumping_images.sort()		
			self.jumping = []
			for rj in self.jumping_images:
				temp = pygame.image.load(rj)
				self.jumping.append(temp)
			self.jumping_frame = 0
			self.image = self.jumping[self.jumping_frame]
			self.rect = self.image.get_rect()
			self.rect.x = 50
			self.rect.y = 442
			self.speed = (5,0)
			self.falling = False
				

		


		world.update(player.speed)
		world.draw(screen)

		players.update()
		players.draw(screen)

		pygame.display.flip()

if __name__ == '__main__':
	main()