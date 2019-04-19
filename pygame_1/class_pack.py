import pygame
import random
import math
import Variables
import supergame_class

color = Variables.color()
display = Variables.display(800, 790, "3kim's game")


Sprite = supergame_class.Sprite
# class Sprite:
#     def __init__(self, xpos, ypos, filename):
#         self.img = filename
#         self.x = xpos
#         self.y = ypos
#         self.bitmap = pygame.image.load(filename)
#         self.bitmap.set_colorkey(color.black)
#
#     def set_position(self, xpos, ypos):
#         self.x = xpos
#         self.y = ypos
#
#     def render(self):
#         display.screen.blit(self.bitmap, [self.x, self.y])

Collision = supergame_class.Collision
# class Collision:
#     def __init__(self, target1, target2):
#         self.x1 = target1.x
#         self.x2 = target2.x
#         self.y1 = target1.y
#         self.y2 = target2.y
#
#     def Collision1(self):
#         if (self.x1 > self.x2 - 15) and (self.x1 < self.x2 + 15) and (self.y1 > self.y2 - 15) and (self.y1 < self.y2 + 15):
#             return True
#         else:
#             return False
#
#     def Collision2(self):
#         if (self.x1 > self.x2 - 25) and (self.x1 < self.x2 + 25) and (self.y1 > self.y2 - 25) and (self.y1 < self.y2 + 25):
#             return True
#         else:
#             return False
#
#     def Collision3(self):
#         if (self.x1 > self.x2 - 30) and (self.x1 < self.x2 + 70) and (self.y1 > self.y2 - 30) and (self.y1 < self.y2 + 70):
#             return True
#         else:
#             return False


class player(Sprite):
    px = 0
    mx = 0
    py = 0
    my = 0
    def move(self):
        # print(self.px, self.mx, self.py,self.my)
        if self.px == 1 and self.x < display.display_W - 40:
            self.x += 5

        elif self.mx == 1 and self.x > 10:
            self.x -= 5

        elif self.py == 1 and self.y < display.display_H - 40:
            self.y += 5

        elif self.my == 1 and self.y > 10:
            self.y -= 5


        self.render()


class target(Sprite):   #enemy
    def __init__(self, xpos, ypos, filename, speed):
        super().__init__(xpos, ypos, filename)
        self.t_speed = speed

    def move(self):
        self.x += self.t_speed
        if self.x > display.display_W - 40 or self.x < 40:
            self.t_speed *= -1
            self.y += 1
        self.y += 2

        if self.y > display.display_H:
            self.x = random.randrange(40, display.display_W - 40)
            self.y = 0

        self.render()

    def boss_appeal(self):
        self.render()

    def boss_move(self):
        self.x += self.t_speed
        if self.x > display.display_W - 40 or self.x < 40:
            self.t_speed *= -1

        self.render()


class p_bullet(player):
    def __init__(self, player, bullet_img):
        super().__init__(player.x, player.y, player.img)
        self.bullet = []
        self.img = bullet_img
        self.timer = 0

    def add(self, player):
        self.bullet.append(Sprite(player.x, player.y, self.img))

    def basic_move(self):
        remove = []
        for i in range(len(self.bullet)):
            self.bullet[i].y -= 5
            if self.bullet[i].y < 0:
                remove.append(i)
        for i in remove:
            del self.bullet[i]

        for i in range(len(self.bullet)):
            self.bullet[i].render()


class t_bullet(target):
    def __init__(self, target, b_num, bullet_img):
        super().__init__(target.x, target.y, target.img, target.t_speed)
        self.bullet = []
        for i in range(b_num):
            self.bullet.append(Sprite(self.x, self.y, bullet_img))

    def basic(self, target):
        for i in range(len(self.bullet)):
            self.bullet[i].y += 5
            if self.bullet[i].y >= display.display_H:
                self.bullet[i].x = target.x
                self.bullet[i].y = target.y
                # eFireSound.play()

        for count in range(len(self.bullet)):
            if self.bullet[count].y < 0:
                del self.bullet[count]
                break

        for i in range(len(self.bullet)):
            self.bullet[i].render()


class b_bullet(target):
    def __init__(self, target, b_num, bullet_img):
        super().__init__(target.x, target.y, target.img, target.t_speed)
        self.pangle = 0
        self.bullet = []
        for i in range(b_num):
            self.bullet.append(Sprite(self.x, self.y, bullet_img))

    def boss_pattern1(self, boss):
        for i in range(len(self.bullet)):
            self.bullet[i].render()
            self.bullet[i].y += 5
            self.bullet[i].x -= (5 - i)

        for i in range(len(self.bullet)):
            if self.bullet[i].y >= display.display_H:
                self.bullet[i].x = boss.x
                self.bullet[i].y = boss.y

        for i in range(len(self.bullet)):
            self.bullet[i].render()

    def boss_pattern2(self, boss):
        self.pangle+= 1 / 50
        for i in range(len(self.bullet)):
            if (i == 0):
                self.bullet[i].y += 5
                self.bullet[i].render()
            elif (i % 4) == 1:
                self.bullet[i].x = self.bullet[0].x + 80 * (int(i / 4) + 1) * math.cos(self.pangle)
                self.bullet[i].y = self.bullet[0].y + 80 * (int(i / 4) + 1) * math.sin(self.pangle) + 5
                self.bullet[i].render()
            elif (i % 4) == 2:
                self.bullet[i].x = self.bullet[0].x + 80 * (int(i / 4) + 1) * math.cos((math.pi / 2) + self.pangle)
                self.bullet[i].y = self.bullet[0].y + 80 * (int(i / 4) + 1) * math.sin((math.pi / 2) + self.pangle)
                self.bullet[i].render()
            elif (i % 4) == 3:
                self.bullet[i].x = self.bullet[0].x + 80 * (int(i / 4) + 1) * math.cos(math.pi + self.pangle)
                self.bullet[i].y = self.bullet[0].y + 80 * (int(i / 4) + 1) * math.sin(math.pi + self.pangle)
                self.bullet[i].render()
            elif (i % 4) == 0:
                self.bullet[i].x = self.bullet[0].x + 80 * (int(i / 4)) * math.cos((math.pi * 3 / 2) + self.pangle)
                self.bullet[i].y = self.bullet[0].y + 80 * (int(i / 4)) * math.sin((math.pi * 3 / 2) + self.pangle)
                self.bullet[i].render()

        for i in range(len(self.bullet)):
            if self.bullet[i].y >= display.display_H:
                self.bullet[i].x = boss.x
                self.bullet[i].y = boss.y

        for i in range(len(self.bullet)):
            self.bullet[i].render()

    def boss_pattern3(self, boss):
        for i in range(len(self.bullet)):
            if i <= 5:
                self.bullet[i].render()
                self.bullet[i].x += 5 - i
                self.bullet[i].y += 0 + i
            elif i > 5 and i <= 10:
                self.bullet[i].render()
                self.bullet[i].x += 5 - i
                self.bullet[i].y += 10 - i
            elif i > 10 and i <= 15:
                self.bullet[i].render()
                self.bullet[i].x += i - 15
                self.bullet[i].y += 10 - i
            else:
                self.bullet[i].render()
                self.bullet[i].x += i - 15
                self.bullet[i].y += i - 20

            if self.bullet[2].y >= display.display_H:
                for i in range(len(self.bullet)):
                    self.bullet[i].x = boss.x
                    self.bullet[i].y = boss.y

        for i in range(len(self.bullet)):
            self.bullet[i].render()


class back_g():
    def __init__(self, img, img_H):
        self.backdrop = pygame.image.load(img)
        self.backdrop2 = pygame.image.load(img)
        self.background_H = img_H
        self.backdrop_y = 0
        self.backdrop2_y = -self.background_H

    def back(self, img, x, y):
        display.screen.blit(img, (x, y))

    def back_move(self):
        self.backdrop_y += 2
        self.backdrop2_y += 2

        if self.backdrop_y == self.background_H:
            self.backdrop_y = 0
        if self.backdrop2_y == 0:
            self.backdrop2_y = -self.background_H

        self.back(self.backdrop, 0, self.backdrop_y)
        self.back(self.backdrop2, 0, self.backdrop2_y)

