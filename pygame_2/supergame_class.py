import pygame
import Variables

display = Variables.display(800, 790, "3kim's game")

class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.img = filename
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey(Variables.color().black)

    def set_position(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    def render(self):
        display.screen.blit(self.bitmap, [self.x, self.y])


class Collision:
    def __init__(self, target1, target2):
        self.x1 = target1.x
        self.x2 = target2.x
        self.y1 = target1.y
        self.y2 = target2.y

    def Collision1(self):
        if (self.x1 > self.x2 - 15) and (self.x1 < self.x2 + 15) and (self.y1 > self.y2 - 15) and (self.y1 < self.y2 + 15):
            return True
        else:
            return False

    def Collision2(self):
        if (self.x1 > self.x2 - 25) and (self.x1 < self.x2 + 25) and (self.y1 > self.y2 - 25) and (self.y1 < self.y2 + 25):
            return True
        else:
            return False

    def Collision3(self):
        if (self.x1 > self.x2 - 30) and (self.x1 < self.x2 + 70) and (self.y1 > self.y2 - 30) and (self.y1 < self.y2 + 70):
            return True
        else:
            return False


class back_g:
    def __init__(self, img, img_H):
        self.backdrop = pygame.image.load(img)
        self.backdrop2 = pygame.image.load(img)
        self.background_H = img_H
        self.backdrop_y = 0
        self.backdrop2_y = -self.background_H

    def back(self, img, x, y):
        Variables.display.screen.blit(img, (x, y))

    def back_move(self):
        self.backdrop_y += 2
        self.backdrop2_y += 2

        if self.backdrop_y == self.background_H:
            self.backdrop_y = 0
        if self.backdrop2_y == 0:
            self.backdrop2_y = -self.background_H

        self.back(self.backdrop, 0, self.backdrop_y)
        self.back(self.backdrop2, 0, self.backdrop2_y)


class Event:
    running = True

    def end_program(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def keyboard(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ...

                if event.key == pygame.K_DOWN:
                    ...

                if event.key == pygame.K_LEFT:
                    ...

                if event.key == pygame.K_RIGHT:
                    ...
