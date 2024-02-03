import pygame
attack_left = [
    pygame.image.load('imagee/player/attack/left/left11.png'),
    pygame.image.load('imagee/player/attack/left/left22.png'),
    pygame.image.load('imagee/player/attack/left/left33.png'),
    pygame.image.load('imagee/player/attack/left/left44.png')
    ]
attack_right = [
pygame.image.load('imagee/player/attack/right/right11.png'),
pygame.image.load('imagee/player/attack/right/right22.png'),
pygame.image.load('imagee/player/attack/right/right33.png'),
pygame.image.load('imagee/player/attack/right/right44.png')
]
attack_up = [
pygame.image.load('imagee/player/attack/up/up11.png'),
pygame.image.load('imagee/player/attack/up/up22.png'),
pygame.image.load('imagee/player/attack/up/up33.png'),
pygame.image.load('imagee/player/attack/up/up44.png')
]
attack_down = [
pygame.image.load('imagee/player/attack/down/down11.png'),
pygame.image.load('imagee/player/attack/down/down22.png'),
pygame.image.load('imagee/player/attack/down/down33.png'),
pygame.image.load('imagee/player/attack/down/down44.png')
]
walkright =[
pygame.image.load('imagee/player/walk/right/right1.png'),
pygame.image.load('imagee/player/walk/right/right2.png'),
pygame.image.load('imagee/player/walk/right/right1.png')
]
walkleft = [
pygame.image.load('imagee/player/walk/left/left1.png'),
pygame.image.load('imagee/player/walk/left/left2.png'),
pygame.image.load('imagee/player/walk/left/left1.png')
]
walkup = [
pygame.image.load('imagee/player/walk/up/up1.png'),
pygame.image.load('imagee/player/walk/up/up2.png'),
pygame.image.load('imagee/player/walk/up/up3.png')
]
walkdown = [
pygame.image.load('imagee/player/walk/down/down1.png'),
pygame.image.load('imagee/player/walk/down/down2.png'),
pygame.image.load('imagee/player/walk/down/down3.png')
]
screen = pygame.display.set_mode((800,640))
def base():
    enemy = pygame.image.load('imagee/enemy/Soldier1.png')
    heart = 3
    my_font = pygame.font.Font('font/impact2.ttf', 20)
    text_heart = my_font.render(f'heart: {heart}', False, 'Black')
    xa = 100
    ya = 100
    screen.fill((112, 211, 110))
    screen.blit(enemy, (xa, ya))
    screen.blit(text_heart, (50, 20))