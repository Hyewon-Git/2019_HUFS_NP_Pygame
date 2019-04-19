import pygame
import py_class
import Variables
import random
import threading
# import math

# 변수 class 선언
color = Variables.color()
display = Variables.display(800, 790, "3kim's game")
img = Variables.img()


# 이미지파일 저장
img.player.append('player1.png')
img.enemies.append('target1.png')
img.boss.append('center.png')
img.p_bullet.append('circle.png')
img.t_bullet.append('bullet3.png')
img.bullet.append('bullet2.png')
img.bg.append('bg4.png')
img.explosion.append('explosion.png')



# pygame 기본 선언
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("3kim's game")


# py_class class 선언 #
# player setting #
player = py_class.player(((display.display_W - 40) * 2 / 3), (display.display_H - 80), img.player[0])

# bullet setting #
bullet = []
for i in range(4):
    if i == 0:
        bullet.append(py_class.bullet(400, 395, 100, img.bullet[0]))
    elif i == 1:
        bullet.append(py_class.bullet(4, 3, 1,img.p_bullet[0]))
    elif i == 2:
        bullet.append(py_class.bullet(random.randrange(100, display.display_H - 100), 0, 11, img.t_bullet[0]))
    elif i == 3:
        bullet.append(py_class.bullet(0, random.randrange(100, display.display_H - 100), 11, img.bullet[0]))



background = py_class.back_g(img.bg[0], display.display_H)

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
    global level

    player.move()
    for i in range(level):
        if i == 0:
            bullet[i].pattern1()
        if i == 1:
            bullet[i].pattern2()
        if i == 2:
            bullet[i].pattern3()
        if i == 3:
            bullet[i].pattern4()


def collision():
    global game_over

    for count in range(len(bullet)):
        for count2 in range(len(bullet[count].bullet)):
            if py_class.Collision(player, bullet[count].bullet[count2]).Collision1():
                game_over = True


def end_game():
    if game_over:
        screen1 = pygame.display.set_mode([700,600])
        screen1.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 36)
        text = font.render("Victory", 50, [255,0,0])
        a = pygame.image.load(img.boss[0])
        screen1.blit(a, (350,350))

        pygame.display.update()



level = 0
def up_level():
    global level
    timer = threading.Timer(2, up_level)
    level += 1
    timer.start()

    if level == 4:
        timer.cancel()

up_level()

# main문 #
while running == True:
    background.back_move()
    event()
    move_all()
    collision()
    end_game()
    clock.tick(60)
    pygame.display.update()

pygame.quit()