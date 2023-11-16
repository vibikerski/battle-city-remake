import pygame
from constants import *
from scenes import *
from scenemanager import *
from scenebuilder import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Battle City Remake")

clock = pygame.time.Clock()

scene_manager = SceneManager()
scene_builder = SceneBuilder()

setup_scenes(scene_builder, scene_manager, screen)

IS_RUNNING = True
while IS_RUNNING:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            IS_RUNNING = False
    keys = pygame.key.get_pressed()

    scene_manager.run(events, keys)

    clock.tick(FPS)
    pygame.display.update()
