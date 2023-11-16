from constants import *
from abc import ABC, abstractmethod
import pygame.locals as pygame_inputs  # для input_handle
from hero import *


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
        self.bg_colour = (34, 28, 51)
        self.text_colour = (212, 36, 36)
        self.screen = screen  # з main.py
        self.manager = manager  # для керування зміною сцени
        self.builder = builder  # для створення сцени Game

    def render(self):
        self.screen.fill(self.bg_colour)  # замінити фоновою картинкою

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
        self.bg_colour = (34, 28, 51)
        self.screen = screen
        self.manager = manager
        self.main_character = Hero(self.screen, IMG_PATH + 'hero.png', 100, 100, 100, 100)

    def render(self):
        self.screen.fill(self.bg_colour)
        self.main_character.render()
       

    def update(self):
        pass

    def handle_events(self, events, keys):
        self.main_character.move(keys)

    # def generate_world(self):
    #     for y
    #         for x
    #             if block == 'p':
    #                 self.main_character = MainTank(IMG_PATH + 'hero.png', x, y)
    #             self.block.append


class Death(Scene):
    def __init__(self):
        pass

    def render(self):
        pass

    def update(self):
        pass

    def handle_events(self, events):
        pass


class Win(Scene):
    def __init__(self):
        pass

    def render(self):
        pass

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
