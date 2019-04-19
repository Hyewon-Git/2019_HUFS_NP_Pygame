import pygame
import supergame_class
import Variables
import math
import random

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

class player(supergame_class.Sprite):
    px = 0
    mx = 0
    py = 0
    my = 0
    def move(self):
        # print(self.px, self.mx, self.py,self.my)
        if self.px == 1 and self.x < supergame_class.display.display_W - 40:
            self.x += 5

        elif self.mx == 1 and self.x > 10:
            self.x -= 5

        elif self.py == 1 and self.y < supergame_class.display.display_H - 40:
            self.y += 5

        elif self.my == 1 and self.y > 10:
            self.y -= 5

        self.render()

0
class bullet(supergame_class.Sprite):
    def __init__(self, xpos, ypos, b_num, bullet_img):
        super().__init__(xpos, ypos, bullet_img)
        self.pangle = 0
        self.bullet = []
        for i in range(b_num):
            self.bullet.append(supergame_class.Sprite(self.x, self.y, bullet_img))


    def pattern1(self):
        self.pangle+= 1/100
        for i in range(len(self.bullet)):
            if (i == 0):
                self.bullet[i].set_position(400,395)
                self.bullet[i].y += 0
                self.bullet[i].render()
            elif (i % 4) == 1:
                self.bullet[i].x = self.bullet[0].x + 20 * (int(i / 4) + 1) * math.cos(self.pangle)
                self.bullet[i].y = self.bullet[0].y + 20 * (int(i / 4) + 1) * math.sin(self.pangle)
                self.bullet[i].render()
            elif (i % 4) == 2:
                self.bullet[i].x = self.bullet[0].x + 20 * (int(i / 4) + 1) * math.cos((math.pi / 2) + self.pangle)
                self.bullet[i].y = self.bullet[0].y + 20 * (int(i / 4) + 1) * math.sin((math.pi / 2) + self.pangle)
                self.bullet[i].render()
            elif (i % 4) == 3:
                self.bullet[i].x = self.bullet[0].x + 20 * (int(i / 4) + 1) * math.cos(math.pi + self.pangle)
                self.bullet[i].y = self.bullet[0].y + 20 * (int(i / 4) + 1) * math.sin(math.pi + self.pangle)
                self.bullet[i].render()
            elif (i % 4) == 0:
                self.bullet[i].x = self.bullet[0].x + 20 * (int(i / 4)) * math.cos((math.pi * 3 / 2) + self.pangle)
                self.bullet[i].y = self.bullet[0].y + 20 * (int(i / 4)) * math.sin((math.pi * 3 / 2) + self.pangle)
                self.bullet[i].render()

    def pattern2(self):
        # global a, b
        self.bullet[0].render()
        self.bullet[0].x += self.x
        self.bullet[0].y += self.y
        if self.bullet[0].x > 700:
            self.x *= -1
        if self.bullet[0].y > 700:
            self.y *= -1
        if self.bullet[0].x < 0:
            self.x *= -1
        if self.bullet[0].y < 0:
            self.y *= -1

    def pattern3(self):
        for i in range(len(self.bullet)):
           self.bullet[i].render()
           self.bullet[i].y += 5
           self.bullet[i].x -= (5 - i)

        for i in range(len(self.bullet)):
            if self.bullet[i].y >= supergame_class.display.display_H:
                self.bullet[i].x = random.randrange(100, supergame_class.display.display_H - 100)
                self.bullet[i].y = 0

        for i in range(len(self.bullet)):
           self.bullet[i].render()


    def pattern4(self):
        for i in range(len(self.bullet)):
            self.bullet[i].render()
            self.bullet[i].x += 5
            self.bullet[i].y -= (5 - i)

        for i in range(len(self.bullet)):
            if self.bullet[i].x >= supergame_class.display.display_W:
                self.bullet[i].y = 0
                self.bullet[i].x = random.randrange(100, supergame_class.display.display_W - 100)

        for i in range(len(self.bullet)):
            self.bullet[i].render()


# back_g = supergame_class.back_g
class back_g():
    def __init__(self, img, img_H):
        self.backdrop = pygame.image.load(img)
        self.backdrop2 = pygame.image.load(img)
        self.background_H = img_H
        self.backdrop_y = 0
        self.backdrop2_y = -self.background_H

    def back(self, img, x, y):
        supergame_class.display.screen.blit(img, (x, y))

    def back_move(self):
        self.backdrop_y += 2
        self.backdrop2_y += 2

        if self.backdrop_y == self.background_H:
            self.backdrop_y = 0
        if self.backdrop2_y == 0:
            self.backdrop2_y = -self.background_H

        self.back(self.backdrop, 0, self.backdrop_y)
        self.back(self.backdrop2, 0, self.backdrop2_y)