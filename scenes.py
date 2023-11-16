from constants import *
from abc import ABC, abstractmethod
import pygame.locals as pygame_inputs  # для input_handle
from hero import *
from maps import *


# абстрактний клас з методами кожної сцени
class Scene(ABC):
    @abstractmethod
    def update():
        pass

    @abstractmethod
    def render():
        pass

    @abstractmethod
    def handle_events():
        pass


# головне меню гри
class Menu(Scene):
    def __init__(self, screen, manager, builder):
        self.bg = GameSprite(screen, 'mainbackground.jpg', 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.text_colour = (212, 36, 36)
        self.screen = screen  # з main.py
        self.manager = manager  # для керування зміною сцени
        self.builder = builder  # для створення сцени Game

    def render(self):
        self.bg.render()

        text = FONT.render("BATTLE CITY (remake)", True, self.text_colour)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.4)

        self.screen.blit(text, textRect)

    def update(self):
        pass

    def handle_events(self, events, keys):
        for event in events:
            if event.type == pygame_inputs.MOUSEBUTTONDOWN:
                self.start_game()

    def start_game(self):
        game = self.builder.create_scene(GAME_STATE, self.screen, self.manager)
        self.manager.add_scene(GAME_STATE, game)
        self.manager.set_scene(GAME_STATE)


class Game(Scene):
    def __init__(self, screen, manager):
        self.map = Map(screen, 'background.jpg')
        self.screen = screen
        self.manager = manager
        self.player = self.map.player
        self.enemies = self.map.enemies
        self.walls = self.map.walls

    def render(self):
        self.map.render_background()
        self.player.render()
        for enemy in self.enemies:
            enemy.render()
        for wall in self.walls:
            wall.render()

    def update(self):
        pass

    def handle_events(self, events, keys):
        self.player.move(keys)


class Death(Scene):
    def __init__(self, screen):
        self.screen = screen
        self.bg = GameSprite(screen, 'lossbackground.jpg', 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

    def render(self):
        self.bg.render()

    def update(self):
        pass

    def handle_events(self, events, keys):
        pass


class Win(Scene):
    def __init__(self, screen):
        self.screen = screen
        self.bg = GameSprite(screen, 'victorybackground.jpg', 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

    def render(self):
        self.bg.render()

    def update(self):
        pass

    def handle_events(self, events):
        pass


def setup_scenes(builder, manager, screen):
    builder.register_scene(MENU_STATE, Menu)
    builder.register_scene(GAME_STATE, Game)
    builder.register_scene(DEATH_STATE, Death)
    builder.register_scene(WIN_STATE, Win)

    menu = builder.create_scene(MENU_STATE, screen, manager, builder)
    manager.add_scene(MENU_STATE, menu)
    manager.set_scene(MENU_STATE)
