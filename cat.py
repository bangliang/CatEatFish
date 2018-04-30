#coding=utf-8 

"""
一个非常简单的猫吃鱼的游戏.
"""

import pygame
import time
import random


# 创建碗类
class PlayerBowl(object):

	# 初始化，完成碗的默认设置
	def __init__(self,screen):

		# 碗的图片
		BowlImageName = './photos/bowl.png'
		self.image = pygame.image.load(BowlImageName).convert()

		# 设置默认坐标
		self.x = 240
		self.y = 240

		# 设置速度
		self.speed = 5

		# 设置碗的名字
		self.BowlName = 'player'

		self.screen = screen

		self.counts = 0

		self.hp = 10

		self.level = 1
		

	# 显示碗
	def show(self):
		self.screen.blit(self.image, (self.x,self.y))


	# 移动碗
	def move_left(self):
		if self.x < 10:
			self.x += 10
		else:
			self.x -= 10

	def move_right(self):
		if self.x > 500:
			self.x -= 10
		else:
			self.x += 10

	def miss(self):
		self.hp -= 1

	def eat(self):
		self.counts +=1

	def win(self):
		self.hp = 10
		self.counts = 0
		self.level += 1

	def lose(self):
		self.hp = 10
		self.counts = 0
		self.level = 1



# 创建鱼类
class Fish(object):
	# 初始化
	def __init__(self,screen,speed=5):
		# 设置鱼的坐标
		self.x = 0
		self.y = 0

		self.screen = screen

		self.speed = speed

		# 鱼的图片
		FishImageName = './photos/fish.jpg'
		self.image = pygame.image.load(FishImageName).convert()

	# 显示鱼
	def show(self):
		self.screen.blit(self.image,(self.x,self.y))

	# 移动鱼
	def move(self):
		if self.y < 300:
			self.y += self.speed
		print(self.y)

def CatEatFish(bowl,fish):
	X = fish.x + 27 - bowl.x
	Y = bowl.y- fish.y
	if Y<=30:
		if 0<=X<=97:
			change(fish)
			bowl.eat()
		elif fish.y == 300:
			change(fish)
			bowl.miss()

def Key_control(bowl):

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			print("exit")
			exit()

		elif event.type == pygame.KEYDOWN:

			if event.key == pygame.K_a or event.key == pygame.K_LEFT:
				bowl.move_left()
				print("left")

			elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
				bowl.move_right()
				print("right")

			elif event.key == pygame.K_SPACE:
				print('space')

def change(fish_temp):
	fish_temp.x = random.randrange(40,550,10)
	fish_temp.y = random.randrange(0,50,5)

def over(bowl_temp,fish_temp):
	if bowl_temp.counts == 10:
		print('You win!Welcome next challenge!')
		fish_temp.speed += 1
		bowl_temp.win()
	elif bowl_temp.hp == 0:
		print('You lose!')
		bowl_temp.lose()
		time.sleep(1)

def main():

	pygame.init()

		# 创建一个长663高306的窗口
	screen = pygame.display.set_mode((600,306),0,32)

	bgImageFile = './photos/background.jpeg'

	background = pygame.image.load(bgImageFile).convert()

	pygame.display.set_caption("猫吃鱼大作战！")

	# 创建碗的对象
	player = PlayerBowl(screen)

	# 创建鱼的对象
	fish = Fish(screen)
	change(fish)


	# 通过while循环防止程序一闪而过
	while  True:
		screen.blit(background,(0,0))
		player.show()
		fish.show()
		fish.move()
		pygame.display.update()
		Key_control(player)
		
		CatEatFish(player,fish)
		over(player,fish)
		fish.show()

		print(player.counts,player.hp,player.level)

		time.sleep(0.1)

# 程序的入口
if __name__ == '__main__':
	main()