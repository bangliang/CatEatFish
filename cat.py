#coding=utf-8 

"""
一个非常简单的猫吃鱼的游戏.
"""

import pygame
import time


# 创建碗类
class PlayerBowl(object):

	# 初始化，完成碗的默认设置
	def __init__(self):

		# 碗的图片
		BowlImageName = './photos/bowl.png'
		self.image = pygame.image.load(BowlImageName).convert()

		# 设置默认坐标
		self.x = 295
		self.y = 240

		# 设置速度
		self.speed = 5

		# 设置碗的名字
		self.BowlName = 'player'
		

	# 显示碗
	def show(self,screen):
		screen.blit(self.image, (self.x,self.y))


	# 移动碗
	def move_left(self):
		self.x -= 10

	def move_right(self):
		self.x += 10


# 创建鱼类
class Fish(object):
	# 初始化
	def __init__(self, x=0, y=0):
		# 设置鱼的坐标
		self.x = x
		self.y = y

		# 鱼的图片
		FishImageName = './photos/fish.jpg'
		self.image = pygame.image.load(FishImageName).convert()

	#显示鱼
	def show(self,screen):
		screen.blit(self.image,(self.x,self.y))

	# 移动鱼
	def move(self):
		if self.y < 220:
			self.y += 5




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

def main():
		# 创建一个长663高306的窗口
	screen = pygame.display.set_mode((663,306),0,32)

	bgImageFile = './photos/background.jpeg'

	background = pygame.image.load(bgImageFile).convert()

	# 创建碗的对象
	player = PlayerBowl()

	# 创建鱼的对象
	fish = Fish()

	# 通过while循环防止程序一闪而过
	while  True:
		screen.blit(background,(0,0))
		player.show(screen)
		fish.show(screen)
		fish.move()
		pygame.display.update()
		Key_control(player)

		time.sleep(0.1)

# 程序的入口
if __name__ == '__main__':
	main()