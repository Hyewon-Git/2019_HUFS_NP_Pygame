import pygame
import class_pack
import Variables
import random


# 변수 class 선언
color = Variables.color()
display = Variables.display(800, 790, "3kim's game")
img = Variables.img()

# 이미지파일 저장
img.player.append('player1.png')
img.enemies.append('target1.png')
img.boss.append('boss.png')
img.p_bullet.append('p_bullet_b.png')
img.p_bullet.append('p_bullet_p.png')
img.t_bullet.append('t_bullet.png')
img.b_bullet.append('b_bullet.png')
img.bg.append('bg.png')
img.explosion.append('explosion.png')

# pygame 기본 선언
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("3kim's game")

# class_pack class 선언 #
# player, enemies, boss, bullet setting #
player = class_pack.player(((display.display_W - 40) / 2), (display.display_H - 80), img.player[0])
boss = class_pack.target(200, 50, img.boss[0], 2)
enemy = class_pack.target(random.randrange(10, display.display_H - 10), 0, img.enemies[0], 2)
enemies = []
for i in range(2):
    enemies.append(enemy)

player_bullet = []
for i in range(2):
    player_bullet.append(class_pack.p_bullet(player, img.p_bullet[i]))
enemy_bullet = []
for i in range(len(enemies)):
    enemy_bullet.append(class_pack.t_bullet(enemies[i], 1, img.t_bullet[0]))
boss_bullet = []
for i in range(3):
    if i == 0:
        boss_bullet.append(class_pack.b_bullet(boss, 11, img.b_bullet[0]))
    elif i == 1:
        boss_bullet.append(class_pack.b_bullet(boss, 13, img.b_bullet[0]))
    elif i ==2:
        boss_bullet.append(class_pack.b_bullet(boss, 20, img.b_bullet[0]))

background = class_pack.back_g(img.bg[0], display.display_H)


running = True
game_over = False
def event():
    global running ,game_over

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.px = 1
                player.mx = 0

            if event.key == pygame.K_LEFT:
                player.mx = 1
                player.px = 0

            if event.key == pygame.K_DOWN:
                player.py = 1
                player.my = 0

            if event.key == pygame.K_UP:
                player.my = 1
                player.py = 0

            if event.key == pygame.K_SPACE:
                if  player_bullet[1].timer == 0:
                    if not game_over:
                        player_bullet[1].add(player)
                        player_bullet[1].timer = 20
                        # FireSound.play()

            if event.key == pygame.K_LCTRL:
                if not game_over:
                    player_bullet[0].add(player)
                    # eFireSound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.px = 0

            if event.key == pygame.K_LEFT:
                player.mx = 0

            if event.key == pygame.K_DOWN:
                player.py = 0

            if event.key == pygame.K_UP:
                player.my = 0


def move_all():
    player.move()
    boss.boss_move()
    for i in range(len(enemies)):
        enemies[i].move()

    for i in range(len(player_bullet)):
        player_bullet[i].basic_move()
    for i in range(len(enemies)):
        for j in range(len(enemy_bullet)):
            enemy_bullet[j].basic(enemies[i])
    for i in range(len(boss_bullet)):
        if i == 0:
            boss_bullet[i].boss_pattern1(boss)
        if i == 1:
            boss_bullet[i].boss_pattern2(boss)
        if i == 2:
            boss_bullet[i].boss_pattern3(boss)


def collision():
    for count in range(len(player_bullet[0])):
        if class_pack.Collision1(player_bullet[0][count], enemies[0]):
            enemies[0].x = random.randrange(40, display.display_W-40)
            enemies[0].y = 0
            del player_bullet[0][count]
            break

    for count in range(len(player_bullet[0])):
        if class_pack.Collision2(player_bullet[0][count], enemies[1]):
            enemies[1].x = random.randrange(40, display.display_W-40)
            enemies[1].y = 0
            del player_bullet[0][count]
            break

    for count in range(len(player_bullet[1])):
        if class_pack.Collision1(player_bullet[1][count], enemies[0]):
            enemies[0].x = random.randrange(40, display.display_W-40)
            enemies[0].y = 0
            del player_bullet[1][count]
            break

    for count in range(len(player_bullet[1])):
        if class_pack.Collision2(player_bullet[1][count], enemies[1]):
            enemies[1].x = random.randrange(40, display.display_W-40)
            enemies[1].y = 0
            del player_bullet[1][count]
            break

    if class_pack.Collision1(player, enemy_bullet[0]):
        ...

    if class_pack.Collision1(player, enemy_bullet[1]):
        ...





# main
while running == True:
    background.back_move()
    event()
    # print(player.px, player.mx, player.py, player.my)

    # 충돌등 여러 가지
    move_all()

    clock.tick(60)
    pygame.display.update()
    if player_bullet[1].timer > 0:
        player_bullet[1].timer -= 1

pygame.quit()