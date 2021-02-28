import pygame, sys

from buttons.ButtonPy import Button

mainClock = pygame.time.Clock()
from pygame.locals import *

WHITE = (255,255,255)
BLACK = (  0,  0,  0)

RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)

YELLOW = (255,255, 0)

class Menu:
    def __init__(self, screen, font):
        self.click = False
        self.screen = screen
        self.font = font

    '''
    function that writes the message for the player
    :param: text - string, font - object of class Font, color, screen, x & y coordinates
    :return: a new surface
    '''
    def draw_text(self,text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, (255, 255, 255))
        return textSurface, textSurface.get_rect()

    def main_menu(self):
        while True:

            self.screen.fill((192, 192, 192))
            self.draw_text('Welcome, Player! Enjoy your game!', self.font, (255, 255, 255), self.screen, 80, 50)

            mx, my = pygame.mouse.get_pos()

            play = Button(75, 200, 'Play Again?', self.screen, self.font)
            quit = Button(325, 200, 'Quit?', self.screen, self.font)
            pause = Button(75, 350, 'Down', self.screen, self.font)

            if play.draw_button():
                print('Again')
                counter = 0
            if quit.draw_button():
                print('Quit')
            if pause.draw_button():
                print('Down')
                counter -= 1

            counter_img = self.font.render(str(counter), True, RED)
            self.screen.blit(counter_img, (280, 450))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()
            mainClock.tick(60)


    def game(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))

            self.draw_text('game', self.font, (255, 255, 255), self.screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            mainClock.tick(60)


    def options(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))

            self.draw_text('options', self.font, (255, 255, 255), self.screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            mainClock.tick(60)
