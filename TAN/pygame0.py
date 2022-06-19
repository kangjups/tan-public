# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 21:05:24 2022

@author: angel
"""

import pygame

def pygame0():
    pygame.init()
    screen_width = 800 
    screen_height = 530
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("pygame")
    background = pygame.image.load("back_ground.png")
    running0 = True
    #------------------------------------------------------------------------------
    while running0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running0 = False 
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: 
                    running0 = False
                    
     
        # 배경
        screen.blit(background, (0, 0))
        pygame.display.update()
    pygame.quit()

pygame0()