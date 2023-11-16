from sprites import *
from constants import *

class Enemy(CollidingObject):
    def __init__(self, screen, img, pos_x, pos_y, size_x, size_y, speed_x = SPEED_MIN, speed_y = SPEED_MAX):
        super().__init__(screen, img, pos_x, pos_y, size_x, size_y)
        self.speed_x = speed_x
        self.speed_y = speed_y
        
    def shoot(self):
        pass
        