import pygame

pygame.init()
win = pygame.display.set_mode((500, 300))   # Задаём размеры окну нашей игры"

pygame.display.set_caption("Game")  # Даём назнавие нашему окну"

player_stand = pygame.image.load('player_stand.png')
player_right = [pygame.image.load(f'player_right_{i}.png') for i in range(1, 5)]
player_left = [pygame.image.load(f'player_left_{i}.png') for i in range(1, 5)]
player_up = [pygame.image.load(f'player_up_{i}.png') for i in range(1, 5)]
player_down = [pygame.image.load(f'player_down_{i}.png') for i in range(1, 5)]

player_stand_enemy = pygame.image.load('enemy_stand.png')
player_right_enemy = [pygame.image.load(f'enemy_right_{i}.png') for i in range(1, 5)]
player_left_enemy = [pygame.image.load(f'enemy_left_{i}.png') for i in range(1, 5)]
player_up_enemy = [pygame.image.load(f'enemy_up_{i}.png') for i in range(1, 5)]
player_down_enemy = [pygame.image.load(f'enemy_down_{i}.png') for i in range(1, 5)]

blood = pygame.image.load('blood.png')
bg = pygame.image.load('bg2.png')


clock = pygame.time.Clock()

x = 50  # Начальные координаты игрока
y = 190

x_new = x   # Будущие координаты курсора мыши пока равны координатам игрока
y_new = y

x_enemy = 490   # Будущие вражеского персонажа
y_enemy = 150

width_hp_player = 30
height_hp_player = 3

width_hp_enemy = 30
height_hp_enemy = 3



speed = 1   # Скорость перемещения персонажа

player_alive = True
enemy_alive = True

left = False
right = False
up = False
down = False
game = True
button_pressed = False

enemy_is_near = False   # Вражеский песонаж стоит на месте

animation_count = 0

bullets = []
bullets_enemy = []

class shooting_player():
    def __init__(self, x, y, radius, shot, facing):
        self.x = x
        self.y = y
        self.shot = shot
        self.radius = radius
        self.facing = facing
        self.vel = 15 * facing

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius)

class shooting_enemy():
    def __init__(self, x_enemy, y_enemy, radius, shot, facing):
        self.x_enemy = x_enemy
        self.y_enemy = y_enemy
        self.shot = shot
        self.radius = radius
        self.facing = facing
        self.vel = 15 * facing

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x_enemy, self.y_enemy), self.radius)

def player():
    # Все переменные, которые будут использоваться не только в этой функции, объявляем как глобальные
    global left
    global right
    global down
    global x
    global y
    global x_new
    global y_new
    global up
    global down
    global player_alive
    if player_alive:
        if x != x_new or y != y_new:
            '''Условие, если координата x игрока не равна координате x курсора 
            или координата y игрока не равна координате y курсора'''
            if x != x_new and y != y_new:
                '''Повторяется это условие, для того, чтобы под каждое перемещение персонажа 
                (вверх, вниз, влево, вправо) сделать анимацию'''
                if x > x_new and y > y_new:
                    '''Условие, если координата x игрока больше координаты x курсора 
                или координата y игрока больше координаты y курсора'''
                    left = True     # Отрисовываем анимацию перемещения влево
                    right = False
                    down = False
                    up = False
                    x -= speed  # Перемещаем персонажа влево
                    y -= speed  # И одновременно перемещаем его вверх
                elif x < x_new and y < y_new:
                    left = False
                    right = True    # Отрисовываем анимацию перемещения вправо
                    down = False
                    up = False
                    x += speed  # Перемещаем персонажа вправо
                    y += speed  # И одновременно перемещаем его вниз
                elif x < x_new and y > y_new:
                    left = False
                    right = True    # Отрисовываем анимацию перемещения вправо
                    down = False
                    up = False
                    x += speed  # Перемещаем персонажа вправо
                    y -= speed  # И одновременно перемещаем его вверх
                elif x > x_new and y < y_new:
                    left = True     # Отрисовываем анимацию перемещения влево
                    right = False
                    down = False
                    up = False
                    x -= speed  # Перемещаем персонажа влево
                    y += speed  # И одновременно перемещаем его вниз
            elif y != y_new:
                if y < y_new:
                    left = False
                    right = False
                    down = True # Отрисовываем анимацию перемещения вниз
                    up = False
                    y += speed  # Перемещаем персонажа вниз
                elif y > y_new:
                    left = False
                    right = False
                    down = False
                    up = True   # Отрисовываем анимацию перемещения вверх
                    y -= speed  # Перемещаем персонажа вверх
            elif x != x_new:
                if x < x_new:
                    x += speed  # Перемещаем персонажа вправо
                    left = False
                    right = True    # Отрисовываем анимацию перемещения вправо
                    down = False
                    up = False
                elif x > x_new:
                    x -= speed  # Перемещаем персонажа влево
                    left = True     # Отрисовываем анимацию перемещения влево
                    right = False
                    down = False
                    up = False
        else:
            left = False
            right = False
            down = False
            up = False

def enemy():
    # Все переменные, которые будут использоваться не только в этой функции, объявляем как глобальные
    global left_enemy
    global right_enemy
    global down_enemy
    global x_enemy
    global y_enemy
    global x
    global y
    global up_enemy
    global enemy_is_near
    global enemy_alive

    if enemy_alive:
        if x_enemy == x+170 and y_enemy == y:   # Если вражеский персонаж находится на оптимальных для стрельбы координатах
            enemy_is_near = True    # Вражеский персонаж стоит на месте
            left_enemy = False
            right_enemy = False
            down_enemy = False
            up_enemy = False
        else:
            if x_enemy == x+210 or y_enemy == y+35 or x_enemy == x-210 or y_enemy == y-35:
                # Если игрок удаляется, враг его преследует
                enemy_is_near = False

        if enemy_is_near == False:  # Если вражеский персонаж не находится на оптимальных для стрельбы координатах
            if x_enemy != x+170 or y_enemy != y:
                '''Условие, если координата x вражеского персонажа не равна координате x игрока 
                или координата y вражеского персонажа не равна координате y игрока'''
                if x_enemy != x+170 and y_enemy != y:
                    '''Повторяется это условие, для того, чтобы под каждое перемещение вражеского игрока 
                    (вверх, вниз, влево, вправо) сделать анимацию'''
                    if x_enemy > x+170 and y_enemy > y:
                        '''Условие, если координата x вражеского персонажа больше координаты x игрока 
                    или координата y вражеского персонажа больше координаты y игрока'''
                        left_enemy = True     # Отрисовываем анимацию перемещения влево
                        right_enemy = False
                        down_enemy = False
                        up_enemy = False
                        x_enemy -= speed  # Перемещаем вражеского персонажа влево
                        y_enemy -= speed  # И одновременно перемещаем его вверх
                    elif x_enemy < x+170 and y_enemy < y:
                        left_enemy = False
                        right_enemy = True    # Отрисовываем анимацию перемещения вправо
                        down_enemy = False
                        up_enemy = False
                        x_enemy += speed  # Перемещаем вражеского персонажа вправо
                        y_enemy += speed  # И одновременно перемещаем его вниз
                    elif x_enemy < x+170 and y_enemy > y:
                        left_enemy = False
                        right_enemy = True    # Отрисовываем анимацию перемещения вправо
                        down_enemy = False
                        up_enemy = False
                        x_enemy += speed  # Перемещаем вражеского персонажа вправо
                        y_enemy -= speed  # И одновременно перемещаем его вверх
                    elif x_enemy > x+170 and y_enemy < y:
                        left_enemy = True     # Отрисовываем анимацию перемещения влево
                        right_enemy = False
                        down_enemy = False
                        up_enemy = False
                        x_enemy -= speed  # Перемещаем вражеского персонажа влево
                        y_enemy += speed  # И одновременно перемещаем его вниз
                elif y_enemy != y:
                    if y_enemy < y:
                        left_enemy = False
                        right_enemy = False
                        down_enemy = True # Отрисовываем анимацию перемещения вниз
                        up_enemy = False
                        y_enemy += speed  # Перемещаем вражеского персонажа вниз
                    elif y_enemy > y:
                        left_enemy = False
                        right_enemy = False
                        down_enemy = False
                        up_enemy = True   # Отрисовываем анимацию перемещения вверх
                        y_enemy -= speed  # Перемещаем вражеского персонажа вверх
                elif x_enemy != x+170:
                    if x_enemy < x+170:
                        x_enemy += speed  # Перемещаем вражеского персонажа вправо
                        left_enemy = False
                        right_enemy = True    # Отрисовываем анимацию перемещения вправо
                        down_enemy = False
                        up_enemy = False
                    elif x_enemy > x+170:
                        x_enemy -= speed  # Перемещаем вражеского персонажа влево
                        left_enemy = True     # Отрисовываем анимацию перемещения влево
                        right_enemy = False
                        down_enemy = False
                        up_enemy = False
            else:
                left_enemy = False
                right_enemy = False
                down_enemy = False
                up_enemy = False


def draw_window():
    global player_alive
    global enemy_alive
    global width_hp_enemy
    global width_hp_player
    global animation_count
    global bullet_1

    win.blit(bg, (0, 0))


    if animation_count + 1 >= 40:
        animation_count = 0

    if player_alive:
        pygame.draw.rect(win, (255, 0, 0), (x, y - 5, width_hp_player, height_hp_player))
        if left:   # Анимация перемещения влево
            win.blit(player_left[animation_count // 4], (x, y))
            animation_count += 1
            if animation_count == 8:
                animation_count = 0
        elif right:     # Анимация перемещения вправо
            win.blit(player_right[animation_count // 4], (x, y))
            animation_count += 1
            if animation_count == 8:
                animation_count = 0
        elif up:    # Анимация перемещения вверх
            win.blit(player_up[animation_count // 4], (x, y))
            animation_count += 1
            if animation_count == 8:
                animation_count = 0
        elif down:  # Анимация перемещения вниз
            win.blit(player_down[animation_count // 4], (x, y))
            animation_count += 1
            if animation_count == 8:
                animation_count = 0
        else:
            win.blit(player_stand, (x, y))  # Всегда отрисовываем персонажа, когда он не перемещается

    if enemy_alive:
        pygame.draw.rect(win, (255, 0, 0), (x_enemy, y_enemy - 5, width_hp_enemy, height_hp_enemy))
        if left_enemy:   # Анимация перемещения влево
            win.blit(player_left_enemy[animation_count // 4], (x_enemy, y_enemy))
            animation_count += 1
            if animation_count == 8:
                animation_count = 0
        elif right_enemy:     # Анимация перемещения вправо
            win.blit(player_right_enemy[animation_count // 4], (x_enemy, y_enemy))
            animation_count += 1
            if animation_count == 8:
                animation_count = 0
        elif up_enemy:    # Анимация перемещения вверх
            win.blit(player_up_enemy[animation_count // 4], (x_enemy, y_enemy))
            animation_count += 1
            if animation_count == 8:
                animation_count = 0
        elif down_enemy:  # Анимация перемещения вниз
            win.blit(player_down_enemy[animation_count // 4], (x_enemy, y_enemy))
            animation_count += 1
            if animation_count == 8:
                animation_count = 0
        else:
            win.blit(player_stand_enemy, (x_enemy, y_enemy))    # Всегда отрисовываем персонажа, когда он не перемещается

    if player_alive:
        for bullet in bullets:
                bullet.draw(win)
                for i in range(1, 31):
                    if bullet.x == x_enemy+i:
                        width_hp_enemy -= 10
                        bullets.pop(bullets.index(bullet))
                        if enemy_alive:
                            win.blit(blood, (x_enemy, y_enemy))
                        if width_hp_enemy == 0:
                            enemy_alive = False
    if enemy_alive:
        for bullet_enemy in bullets_enemy:
            bullet_enemy.draw(win)
            for i in range(1, 31):
                if bullet_enemy.x_enemy == x + i:
                    width_hp_player -= 1
                    bullets_enemy.pop(bullets_enemy.index(bullet_enemy))
                    if player_alive:
                        win.blit(blood, (x, y))
                    if width_hp_player == 0:
                        player_alive = False


    pygame.display.update()




while game:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()  # Выход при нажатии "выход"
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:   # 1 - означает левую кнопку мыши
                x_new, y_new = event.pos    # Координаты точки, где находиться курсор
                button_pressed = True   # Левая кнопка мыши нажата
            if event.button == 3:
                facing = 1
                bullet_1 = 0
                if len(bullets) <= 1:
                    bullets.append(shooting_player(round(x),
                                          round(y+30), 2, (0, 0 ,0), facing))

    if x_enemy <= x + 170 and y_enemy == y:     # Если враг находится на оптимальном расстоянии для стельбы
        facing = -1
        if len(bullets_enemy) < 1:
            bullets_enemy.append(shooting_enemy(round(x_enemy),
                                           round(y_enemy + 30), 2, (0, 0, 0), facing))
            # Добавляем пули

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    for bullet_enemy in bullets_enemy:
        if bullet_enemy.x_enemy < 500 and bullet_enemy.x_enemy > 0:
            bullet_enemy.x_enemy += bullet_enemy.vel
        else:
            bullets_enemy.pop(bullets_enemy.index(bullet_enemy))

    if button_pressed:
        player()
    enemy()     # Вызываем функциию игрока
    draw_window()   # Отрисовываем все наше окно игры



pygame.quit()

