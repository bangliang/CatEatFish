#coding=utf-8 

"""
一个非常简单的猫吃鱼的游戏.
"""

import pygame

# 程序的入口
if __name__ == '__main__':
	
		# 创建一个长663高306的窗口
		screen = pygame.display.set_mode((663,306),0,32)

		bgImageFile = './photos/background.jpeg'

		background = pygame.image.load(bgImageFile).convert()

		# 通过while循环防止程序一闪而过
		while  True:
			
			# 显示背景
			screen.blit(background,(0,0))
		
			# 键盘键盘
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					print("exit")
					exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_a or event.key == pygame.K_LEFT:
						print("left")
					elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
						print("right")
					elif event.key == pygame.K_SPACE:
						print('space')

			pygame.display.update()

