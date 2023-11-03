from settings import *
from abc import ABC, abstractmethod

# абстрактний клас з методами кожної сцени
class Scene(ABC):
    @abstractmethod
    def update():
        pass
    
    @abstractmethod
    def render():
        pass

    @abstractmethod
    def handle_inputs():
        pass


# головне меню гри
class Menu(Scene):
    def __init__(self, screen):
        self.bg_colour = (34, 28, 51)
        self.text_colour = (212, 36, 36)
        self.screen = screen # з main.py
    
    def render(self):
        self.screen.fill(self.bg_colour) # замінити фоновою картинкою
        
        text = FONT.render("BATTLE CITY (remake)", True, self.text_colour)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.4)
        
        self.screen.blit(text, textRect)
        
    def update(self):
        pass
    
    def handle_inputs(self):
        pass # тимчасово


# class Game: ...
# class Death: ...
# class Win: ...