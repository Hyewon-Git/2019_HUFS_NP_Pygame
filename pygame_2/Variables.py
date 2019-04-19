import pygame

class color:
    def __init__(self):
        self.white = [255, 255, 255]
        self.black = [0, 0, 0]


class display:
    def __init__(self, Width, Height, name):
        self.display_W = Width
        self.display_H = Height
        self.name = name
        self.screen = pygame.display.set_mode([self.display_W, self.display_H])
        # self.pygame.display.set_caption(self.name)


class sounds:
    def __init__(self):
        self.BackMusic = pygame.mixer.Sound('background.wav')
        self.FireSound = pygame.mixer.Sound('fire.wav')
        self.eFireSound = pygame.mixer.Sound('efire.wav')
        self.DefeatSound = pygame.mixer.Sound('Defeat.wav')
        self.VictorySound = pygame.mixer.Sound('Victory.wav')
        self.DeathSound = pygame.mixer.Sound('death.wav')


class img:
    def __init__(self):
        self.bg = []
        self.player= []
        self.enemies = []
        self.boss = []
        self.p_bullet = []
        self.t_bullet = []
        self.bullet = []
        self.explosion = []
        self.hart = []