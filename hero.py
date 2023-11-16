from sprites import *
from constants import *
import pygame.locals as inputs

class Hero(GameSprite):
    def __init__(self, screen, img, pos_x, pos_y, size_x, size_y, speed_x = SPEED_MID, speed_y = SPEED_MID):
        super().__init__(screen, img, pos_x, pos_y, size_x, size_y)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self, keys):
        self.old_x, self.old_y = self.rect.x, self.rect.y
        self.rect.x += self.speed_x * (keys[inputs.K_d] - keys[inputs.K_a])
        self.rect.y += self.speed_y * (keys[inputs.K_s] - keys[inputs.K_w])
        self.check_out_of_bounds()
    
    def go_back(self):
        self.rect.x = self.old_x
        self.rect.y = self.old_y
        
    def check_out_of_bounds(self):
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > SCREEN_WIDTH - self.rect.w:
            self.rect.x = SCREEN_WIDTH - self.rect.w
        
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > SCREEN_HEIGHT - self.rect.h:
            self.rect.y = SCREEN_HEIGHT - self.rect.h
