from pygame_menu.Menu import Menu
import pygame, sys
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Menu')
screen = pygame.display.set_mode((500, 500), 0, 32)

font = pygame.font.SysFont(None, 32)

if __name__ == "__main__":
    menu = Menu(screen, font)
    menu.main_menu()

