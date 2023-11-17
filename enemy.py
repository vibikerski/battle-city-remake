from sprites import *
from constants import *

class Enemy(CollidingObject):
    def __init__(self, screen, img, pos_x, pos_y, size_x, size_y, speed_x = SPEED_MAX, speed_y = SPEED_MIN):
        super().__init__(screen, img, pos_x, pos_y, size_x, size_y)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.direction = "up"
        
    def shoot(self):
        pass
    
    def run(self, player):
        self.render()
        return self.update(player)
    
    def update(self, player):
        if self.collide(player):
            return 'Lost'
        
        if self.direction == "up":
            self.rect.y += self.speed_y
        else:
            self.rect.y -= self.speed_y
        
        if self.rect.y <= 0:
            self.direction = "up"
        elif self.rect.y >= SCREEN_HEIGHT - self.rect.height:
            self.direction = "down"
        
        