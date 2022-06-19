# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 21:00:10 2022

@author: angel
수정
"""

import pygame
import random
def pygame0():
    pygame.init()
    screen_width = 800 
    screen_height = 530
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("pygame")
    background = pygame.image.load("gg.png")
    running0 = True
    #------------------------------------------------------------------------------
    while running0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running0 = False 
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: 
                    running0 = False
                    
# def a(x,y,z = False):
    #print(x)
    #print(y)
    #if z == True
    #return 100 

    # 배경
        screen.blit(background, (0, 0))
        pygame.display.update()
pygame.init()
pygame.mixer.init()

### 전체 화면 800 * 530 , 타일 100 * 70, 타일 간격 10 *70, 캐릭터 50 * 140
### 전투 화면 650*230, 외각 150/2 * 300/2
screen_width = 800 
screen_height = 530
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("tan")
clock = pygame.time.Clock()
background = pygame.image.load("back_ground.png")
bg = pygame.image.load("background_box.png")
bg_red = pygame.image.load("background_box_red.png")

character_main = pygame.image.load("player.png")
character_main_size = character_main.get_rect().size
character_main_width = character_main_size[0]
character_main_height = character_main_size[1]
character_main_x_pos = 185
character_main_y_pos = 230


monster_main = pygame.image.load("monster.png")
monster_main_size = monster_main.get_rect().size
monster_main_width = monster_main_size[0]
monster_main_height = monster_main_size[1]
monster_main_x_pos = 515
monster_main_y_pos = 230

s = pygame.image.load("store.png")
s_size = s.get_rect().size
s_width = s_size[0]
s_height = s_size[1]
sx = 515
sy = 150


weapon = pygame.image.load("weapon.png")
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]
weapons = []
weapon_speed = 15
weapon_damage = 15

weapon2 = pygame.image.load("weapon2.png")
weapon2_size = weapon2.get_rect().size
weapon2_width = weapon2_size[0]
weapon2_height = weapon_size[1]
weapons2 = []
weapon2_speed = 8
weapon2_damage = 28

boom = pygame.image.load("boom.png")
boom_0 = pygame.image.load("boom_0.png")
boom_0_size = boom_0.get_rect().size
boom_0_width = boom_0_size[0]
boom_0_height = boom_0_size[1]
boom_0s = []
boom_0_damage = 30

store =  pygame.image.load("store.png")

count = 0

RED = (255,0,0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)

red_HP = 100
blue_HP = 100
font = pygame.font.SysFont(None,30)
img_red = font.render(str(red_HP),True,WHITE)
img_blue = font.render(str(blue_HP),True,WHITE)
img_x = monster_main_x_pos 
img_y = monster_main_y_pos 

#시간
game_font = pygame.font.Font(None, 40)
total_time = 0
start_ticks = pygame.time.get_ticks()
stage = 1
stage_ = game_font.render(str(stage),True,(255,255,255))
stage_Rect = stage_.get_rect()

background_sound = pygame.mixer.Sound("peak.wav")
background_sound.set_volume(0.4)
attack = pygame.mixer.Sound("wing.wav")
attack.set_volume(1)
attack2 = pygame.mixer.Sound("attack2.wav")
attack2.set_volume(1)
adi = pygame.mixer.Sound("i.wav")
adi.set_volume(0.1)
background_sound.play(-1)
boom_sound = pygame.mixer.Sound("boom_sound.wav")
boom_sound.set_volume(1)
running = True
gie = 0
gie2 = 0
gie3 = 0
gie4 = 0

boom_x = 185
boom_y = 230

def boomx(a):
    if a == 1 or a == 4 or a == 7 :
        a = 0
    if a == 2 or a == 5 or a == 8 :
        a = 1
    if a == 3 or a == 6 or a == 9 :
        a = 2
    boom_x = 75+(a*110)
    return boom_x
def boomy(a):
    
    if a == 1 or a == 2 or a == 3 :
        a = 0
    if a == 4 or a == 5 or a == 6 :
        a = 1
    if a == 7 or a == 8 or a == 9 :
        a = 2
    boom_y = 150+(a*80)
    return boom_y

# 1 75 150
# 2 185 150
# 3 295 150
# 4 75 230
# 5 185 230
# 6 295 230
# 7 75 310
# 8 185 310
# 9 295 310
#------------------------------------------------------------------------------
while running:
    dt = clock.tick(30)
    elapsed_time = ((pygame.time.get_ticks() - gie) - start_ticks) / 100 + 40  # 경과 시간을 1000으로 나누어서 초 단위로 표시
    timer = game_font.render(str(int(total_time + elapsed_time)), True, (255,255,255))
    stage_ = game_font.render(str(int(stage)), True, (255,255,255))
    tm = int(elapsed_time)
    e_t = ((pygame.time.get_ticks() - gie2) - start_ticks) / 1000
    e_t3 = ((pygame.time.get_ticks() - gie3) - start_ticks) / 1000
    e_t4 = ((pygame.time.get_ticks() - gie4) - start_ticks) / 1000

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: 
                character_main_x_pos -= 110
                
            elif event.key == pygame.K_d: 
                character_main_x_pos += 110
           
            elif event.key == pygame.K_w: 
                character_main_y_pos -= 80
            
            elif event.key == pygame.K_s: 
                character_main_y_pos += 80
                
            elif event.key == pygame.K_p:
                pygame0()
            elif event.key == pygame.K_o:
                pass
                
            elif event.key == pygame.K_SPACE and tm >= 0.5 :
                gie = pygame.time.get_ticks()
                attack.play()
                weapon_x_pos = character_main_x_pos + 80
                weapon_y_pos = character_main_y_pos + 15
                weapons.append([weapon_x_pos, weapon_y_pos])
        
    # 제어 x y
    #if character_main_x_pos <= 75:
     #   character_main_x_pos = 75
    #if character_main_x_pos >= 295:
     #   character_main_x_pos = 295
        
    if character_main_y_pos <= 150:
        character_main_y_pos = 150
    if character_main_y_pos >= 310:
        character_main_y_pos = 310
    
    # 뼤다귀
    if stage <= 2 :
        if e_t > 2:
            weapon2_x_pos = monster_main_x_pos
            weapon2_y_pos = monster_main_y_pos + 10
            weapons2.append([weapon2_x_pos, weapon2_y_pos])
            attack2.play()
            gie2 = pygame.time.get_ticks()
            
    if stage == 2 :
        if e_t4 > 3:
            count = random.randint(0,30)
            if count > 0 and count < 10 :
                weapon2_x_pos = monster_main_x_pos
                weapon2_y_pos = 230 - 80 
                weapons2.append([weapon2_x_pos, weapon2_y_pos])
                weapon2_x_pos = monster_main_x_pos
                weapon2_y_pos = 230
                weapons2.append([weapon2_x_pos, weapon2_y_pos])
                attack2.play()
            elif count > 10 and count < 20 :
                weapon2_x_pos = monster_main_x_pos
                weapon2_y_pos = 230  
                weapons2.append([weapon2_x_pos, weapon2_y_pos])
                weapon2_x_pos = monster_main_x_pos
                weapon2_y_pos = 230 + 80 
                weapons2.append([weapon2_x_pos, weapon2_y_pos])
                attack2.play()
            elif count > 20 and count < 30 :
                weapon2_x_pos = monster_main_x_pos
                weapon2_y_pos = 230 + 80 
                weapons2.append([weapon2_x_pos, weapon2_y_pos])
                weapon2_x_pos = monster_main_x_pos
                weapon2_y_pos = 230 - 80 
                weapons2.append([weapon2_x_pos, weapon2_y_pos])
                attack2.play()
            gie4 = pygame.time.get_ticks()

    if e_t3 == 1:
        
        if character_main_y_pos == monster_main_y_pos :
            monster_main_y_pos = monster_main_y_pos
        
        elif character_main_y_pos > monster_main_y_pos :
            monster_main_y_pos += 80
        
        elif character_main_y_pos < monster_main_y_pos :
            monster_main_y_pos -= 80
        gie3 = pygame.time.get_ticks()
       
    if stage == 4:
        monster_main = pygame.image.load("monkey.png")
        if e_t > 3:
            a = random.randint(1,9)
            boom_x = boomx(a)
            boom_y = boomy(a)
            gie2 = pygame.time.get_ticks()
        if e_t3 > 4 :
            boom_0x = boom_x 
            boom_0y = boom_y 
            boom_0s.append([boom_0x, boom_0y])
            boom_0x = boom_x + 110 
            boom_0y = boom_y 
            boom_0s.append([boom_0x, boom_0y])
            boom_0x = boom_x - 110
            boom_0y = boom_y 
            boom_0s.append([boom_0x, boom_0y])
            boom_0x = boom_x 
            boom_0y = boom_y + 80
            boom_0s.append([boom_0x, boom_0y])
            boom_0x = boom_x 
            boom_0y = boom_y - 80
            boom_0s.append([boom_0x, boom_0y])
            boom_sound.play()
            gie3 = pygame.time.get_ticks()
 
    if red_HP <= 0 :
        red_HP = 100
        stage += 1
    
    if blue_HP <= 0:
        pass
    
    weapons = [ [w[0] + weapon_speed, w[1]] for w in weapons]
    weapons = [ [w[0], w[1]] for w in weapons if w[0] < 770 ]
    
    weapons2 = [ [w[0] - weapon2_speed, w[1]] for w in weapons2]
    weapons2 = [ [w[0], w[1]] for w in weapons2 if w[0] > 30 ]
    
    #boom_0s = [ [w[0], w[1]] for w in boom_0s if w[0] > 75 and w[0] < 295 and w[1] > 150 and w[1] < 310  ]
    #for w in boom_0s:
     #   if e_t4 > 2:
      #      print(e_t4)
       #     boom_0s.append(w)
        #    gie4 = pygame.time.get_ticks()
    boom_0s = [[w[0], w[1]] for w in boom_0s if e_t4 < 4 ]
    if e_t4 > 4 :
        gie4 = pygame.time.get_ticks()
        
    character_main_rect = character_main.get_rect()
    character_main_rect.left = character_main_x_pos
    character_main_rect.top = character_main_y_pos
    
    monster_main_rect = monster_main.get_rect()
    monster_main_rect.left = monster_main_x_pos
    monster_main_rect.top = monster_main_y_pos
    
    s_rect = s.get_rect()
    s_rect.left = sx
    s_rect.top = sy
    
    if character_main_rect.colliderect(s_rect):
        pygame0()
    
    # hp 이동
    img_red = font.render(str(red_HP),True,WHITE) # 레드
    img_x = monster_main_x_pos + 30
    img_y = monster_main_y_pos + 55
    if red_HP <= 99:
        img_x = monster_main_x_pos + 40
    if red_HP <= 9 :
        img_x = monster_main_x_pos + 45
        
    img_blue = font.render(str(blue_HP),True,WHITE) # 블루
    img_blue_x = character_main_x_pos + 30
    img_blue_y = character_main_y_pos + 55
    if blue_HP <= 99:
        img_blue_x = character_main_x_pos + 40
    if blue_HP <= 9 :
        img_blue_x = character_main_x_pos + 45
 
    
    for weapon_idx, weapon_val in enumerate(weapons):
        weapon_pos_x = weapon_val[0]
        weapon_pos_y = weapon_val[1]

        # 무기 정보
        weapon_rect = weapon.get_rect()
        weapon_rect.left = weapon_pos_x
        weapon_rect.top = weapon_pos_y
        #print(weapon_rect,("웨폰 박스"))
        #print(weapons,("웨폰스"))
        #print(weapon_x_pos)
        #print(weapon_y_pos)
        
        if stage == 3 :
            monster_main = store
            if weapon_rect.colliderect(monster_main_rect) :
                weapons.pop(weapon_idx)
                pygame0()
        
        elif weapon_rect.colliderect(monster_main_rect):
            #weapons.remove(weapon_val)
            weapons.pop(weapon_idx)
            red_HP -= weapon_damage
            adi.play()
            img_red = font.render(str(red_HP),True,RED)
         
            #weapons = [ [w[0], w[1]] for w in weapons if w[0] >= monster_x_pos and w[1] > 160 and w[1] < 280 ]
            #weapons = [ [w[0], w[1]] for w in weapons if w[0] != weapon_rect.left  ]

        
    for weapon2_idx, weapon2_val in enumerate(weapons2):
        weapon2_pos_x = weapon2_val[0]
        weapon2_pos_y = weapon2_val[1]

        # 무기 정보
        weapon2_rect = weapon2.get_rect()
        weapon2_rect.left = weapon2_pos_x
        weapon2_rect.top = weapon2_pos_y
        
        if weapon2_rect.colliderect(character_main_rect):
            #weapons.remove(weapon_val)
            weapons2.pop(weapon2_idx)
            blue_HP -= weapon2_damage
            attack2.stop()
            adi.play()
            img_blue = font.render(str(blue_HP),True,RED)
        
    for boom_0_idx, boom_0_val in enumerate(boom_0s):
        boom_0_pos_x = boom_0_val[0]
        boom_0_pos_y = boom_0_val[1]

        # 폭탄 정보
        boom_0_rect = boom_0.get_rect()
        boom_0_rect.left = boom_0_pos_x
        boom_0_rect.top = boom_0_pos_y
        
        if boom_0_rect.colliderect(character_main_rect):
            boom_0s.pop(boom_0_idx)
            blue_HP -= boom_0_damage
            img_blue = font.render(str(blue_HP),True,RED)
    
    
    # 배경
    screen.blit(background, (0, 0))
    
    # 타일
    for i in range(3):
        for a in range(3):
           screen.blit(bg,(75+(a*110),150+(i*80)))
           screen.blit(bg_red,(405+(a*110),150+(i*80)))
           
    if stage >= 4:
        screen.blit(boom,(boom_x,boom_y))
    
    
    # main    
    screen.blit(monster_main,(monster_main_x_pos,monster_main_y_pos))
    screen.blit(character_main,(character_main_x_pos,character_main_y_pos))
    screen.blit(s,(sx,sy))
    for boom_0x, boom_0y in boom_0s:
        screen.blit(boom_0,(boom_0x,boom_0y))
        
    for weapon2_x_pos, weapon2_y_pos in weapons2:
        screen.blit(weapon2,(weapon2_x_pos,weapon2_y_pos))
    
    # 무기
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    
    # hP
    screen.blit(img_blue,(img_blue_x,img_blue_y))
    screen.blit(img_red, (img_x,img_y))
    screen.blit(stage_,(700,10))
    screen.blit(timer, (10, 10))
    
    pygame.display.update()

pygame.quit()

