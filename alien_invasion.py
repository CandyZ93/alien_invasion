#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  alien_invasion.py
#

import sys
import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# 创建Play按钮
	play_button = Button(ai_settings, screen, "Play")
		
	# 创建一个用于存储游戏统计信息的实例,并创建记分牌
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	# 创建一艘飞船、一个子弹编组和一个外星人编组
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	
	# 创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	# 开始游戏的主循环
	while True:
		# 先检测键盘事件再更新飞船、子弹编组状态，传入子弹编组！
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
			aliens, bullets)
		# check_events用于退出游戏，不受非活动状态影响
		if stats.game_active:
			ship.update() # 先更新飞船状态再绘制
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
				bullets)
			gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens,
				bullets)
		# 即使处于非活动状态也应维持屏幕的输出
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, 
			play_button)
		
run_game()
