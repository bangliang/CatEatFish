#coding=utf-8 

"""
一个非常简单的猫吃鱼的游戏.
"""

import pygame

class PlayerBowl(object):

	# 初始化，完成碗的默认设置
	def __init__(self):

		# 存储鱼饵列表
		self.BaitList = []

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
	def move(self,type):
		if type == 'left':
			self.x -= 10
		elif type == 'right':
			self.x += 10


# 程序的入口
if __name__ == '__main__':
	
		# 创建一个长663高306的窗口
		screen = pygame.display.set_mode((663,306),0,32)

		bgImageFile = './photos/background.jpeg'

		background = pygame.image.load(bgImageFile).convert()

		# 创建碗的对象，并显示
		player = PlayerBowl()
		player.show(screen)

		# 通过while循环防止程序一闪而过
		while  True:
			
			# 显示背景
			screen.blit(background,(0,0))
			player.show(screen)
		
			# 键盘键盘
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					print("exit")
					exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_a or event.key == pygame.K_LEFT:
						player.move('left')
						print("left")
					elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
						player.move('right')
						print("right")
					elif event.key == pygame.K_SPACE:
						print('space')

			pygame.display.update()

