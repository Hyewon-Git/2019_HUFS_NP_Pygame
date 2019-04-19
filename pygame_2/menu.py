# Import pygame and libraries
from pygame.locals import *
from random import randrange
import os
import pygame

import pygameMenu
from pygameMenu.locals import *

red=(255,0,0)
white=(255,255,255)
black=(0,0,0)
yellow=(255,255,0)
green=(0,238,60)
# FONT = pygame.font.Font(None, 50)
startbg = pygame.image.load('STARTBG.png')
backdrop = pygame.image.load('STARTBG.png')
howtoplaybg = pygame.image.load('howplay.png')
playbg =pygame.image.load('PLAYBG.png')

COLOR_BACKGROUND = (128, 0, 128)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (228, 55, 36)


# -----------------------------------------------------------------------------
# Init pygame
pygame.init()
# os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create pygame screen and objects
screen = pygame.display.set_mode([700,600])
pygame.display.set_caption('PygameMenu')
clock = pygame.time.Clock()
dt = 1 / FPS
# -----------------------------------------------------------------------------

#  Function used by menus, draw on background while menu is active.
def main_background():
    screen.blit(startbg,(0,0))
def about_background():
    screen.blit(howtoplaybg,(0,0))


# -----------------------------------------------------------------------------
# PLAY MENU

# play_menu.add_option('Return to main menu', PYGAME_MENU_BACK)
def play_function():
    # Reset main menu and disable
    # You also can set another menu, like a 'pause menu', or just use the same
    # main_menu as the menu that will check all your input.
    main_menu.disable()
    main_menu.reset(1)

    while True:
        # Clock tick
        clock.tick(60)
        # Application events
        import main
        playevents = pygame.event.get()
        for e in playevents:
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE and main_menu.is_disabled():
                    main_menu.enable()

                    # Quit this function, then skip to loop of main-menu on line 217
                    return

        # Pass events to main_menu
        main_menu.mainloop(playevents)

        # Continue playing
        screen.blit(playbg, (0,0))
        pygame.display.flip()

def how_function():
    main_menu.disable()
    main_menu.reset(1)

    while True:
        clock.tick(60)
        playevents = pygame.event.get()

        for e in playevents:
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE and main_menu.is_disabled():
                    main_menu.enable()
                    return

        # Pass events to main_menu
        main_menu.mainloop(playevents)
        # Continue playing
        screen.blit(howtoplaybg, (0, 0))
        pygame.display.flip()

# MAIN MENU
main_menu = pygameMenu.Menu(screen,
                            bgfun=main_background,
                            color_selected=red,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=black,
                            font_size=60,
                            menu_alpha=0,
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='',
                            window_height=800,
                            window_width=1100
                            )
main_menu.add_option('Play', play_function)
main_menu.add_option('About', how_function)
main_menu.add_option('Quit', PYGAME_MENU_EXIT)

BackMusic = pygame.mixer.Sound('PLAYSOUND.wav')
# -----------------------------------------------------------------------------
# Main loop
BackMusic.play()
while True:

    # Tick
    clock.tick(60)

    # Application events
    events = pygame.event.get()
    # for event in events:
    #     if event.type == QUIT:
    #         exit()

    # Main menu
    main_menu.mainloop(events)

    # Flip surface
    pygame.display.flip()