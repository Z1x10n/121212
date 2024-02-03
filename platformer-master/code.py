# hello commit
import pygame
from test import *
b = 0
a = 0
y = 0
x = 0
xa = 100
ya = 100

move_speed = 10
damag =5
heart = 3

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((800,640))
enemy = pygame.image.load('imagee/enemy/Soldier1.png')
player = pygame.image.load('imagee/player/walk/down/down1.png')
shadow = pygame.image.load('imagee/player/shadow/CharacterShadow.png')

#анимация боя
player_attac = 0
attac_left = attack_left
attac_right = attack_right
attac_up = attack_up
attac_down = attack_down
#анимации ходьбы
player_walk = 0
walk_right = walkright
walk_left = walkleft
walk_up = walkup
walk_down = walkdown
#текст,кнопки
button = pygame.image.load('imagee/(36) Pinterest.png')
my_font = pygame.font.Font('font/impact2.ttf', 20)


running = True
while running == True:
    text_heart = my_font.render(f'heart: {heart}', False, 'Black')



    def base():
        screen.fill((112, 211, 110))
        screen.blit(text_heart, (50, 20))
        screen.blit(enemy,(xa,ya))


    if x>xa-30 and x<xa+30 and y>ya-30 and y<ya+30:
        heart -=1



    if b == 0:
        base()
        screen.blit(player, (x, y))



        if a == 0:
            player = pygame.image.load('imagee/player/walk/down/down1.png')
        if a == 1:
            player = pygame.image.load('imagee/player/walk/left/left1.png')
        if a == 2:
            player = pygame.image.load('imagee/player/walk/right/right1.png')
        if a == 3:
            player = pygame.image.load('imagee/player/walk/up/up1.png')
        if pygame.mouse.get_pressed()[0]:
            if a == 0:
                base()
                screen.blit(attac_down[player_attac], (x, y))
            if a == 1:
                base()
                screen.blit(attac_left[player_attac],(x,y))
            if a == 2:
                base()
                screen.blit(attac_right[player_attac], (x, y))
            if a == 3:
                base()
                screen.blit(attac_up[player_attac], (x, y))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            y-=move_speed
            base()
            screen.blit(walk_up[player_walk],(x,y))

            a = 3
        if keys[pygame.K_s]:
            y+=move_speed
            base()
            screen.blit(walk_down[player_walk], (x, y))
            a = 0
        if keys[pygame.K_a]:
            x-=move_speed
            base()
            screen.blit(walk_left[player_walk], (x, y))
            a = 1
        if keys[pygame.K_d]:
            x+=move_speed
            base()
            screen.blit(walk_right[player_walk], (x, y))
            a = 2
        if player_walk == 2:
            player_walk = 0
        else:
            player_walk +=1
        if player_attac == 3:
            player_attac = 0
        else:
            player_attac+=1
        if keys[pygame.K_ESCAPE]:
            b = 1
    if b == 1:
        screen.fill(('Grey'))
        start_rect = pygame.Rect(100, 100, 136, 39)
        pygame.draw.rect(screen, pygame.Color("Grey"), start_rect)
        screen.blit(button,(100,100))
        text_start = my_font.render('START', False, 'Black')
        screen.blit(text_start, (145, 107))
        if start_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            b = 0


        settings_rect = pygame.Rect(100, 200, 136, 39)
        pygame.draw.rect(screen, pygame.Color("Grey"), settings_rect)
        screen.blit(button, (100, 200))
        text_start = my_font.render('SETTINGS', False, 'Black')
        screen.blit(text_start, (145, 207))


        exit_rect = pygame.Rect(100, 300, 136, 39)
        pygame.draw.rect(screen, pygame.Color("Grey"), exit_rect)
        screen.blit(button, (100, 300))
        text_start = my_font.render('EXIT', False, 'Black')
        screen.blit(text_start, (145, 307))
        if exit_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            pygame.quit()






    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    clock.tick(10)