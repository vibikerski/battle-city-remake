import pygame
from settings import *
from scenes import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Battle City Remake")

clock = pygame.time.Clock()
menu = Menu(screen)

IS_RUNNING = True
while IS_RUNNING:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            IS_RUNNING = False
    
    if CURRENT_STATE == MENU_STATE:
        menu.render()
        # CURRENT_STATE = menu.handle(events) - можливо, зміна стану від інтеракції

    clock.tick(FPS)
    pygame.display.update()
    