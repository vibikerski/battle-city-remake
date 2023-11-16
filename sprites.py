from pygame import *
from constants import IMG_PATH

class GameSprite():
    def __init__(self, screen, img, pos_x, pos_y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(IMG_PATH + img),(size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.screen = screen
    
    def render(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

class CollidingObject(GameSprite):
    def collide(self, other):
        return self.rect.colliderect(other.rect)