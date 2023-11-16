from sprites import *
from constants import *
from hero import *
from enemy import *

game_map = [
    ['w', 'p', 'w', '0', '0', '0', 'w', '0'],
    ['w', '0', 'w', '0', 'w', '0', '0', 'e'],
    ['w', '0', 'w', '0', 'w', '0', 'w', '0'],
    ['w', '0', 'w', '0', '0', '0', '0', 'e1'],
    ['w', '0', '0', '0', 'w', '0', 'w', '0'],
    ['w', '0', '0', '0', 'w', '0', '0', '0']
]

clean_map = [
    ['w', '0', 'w', '0', '0', '0', 'w', '0'],
    ['w', '0', 'w', '0', 'w', '0', '0', '0'],
    ['w', '0', 'w', '0', 'w', '0', 'w', '0'],
    ['w', '0', 'w', '0', '0', '0', '0', '0'],
    ['w', '0', '0', '0', 'w', '0', 'w', '0'],
    ['w', '0', '0', '0', 'w', '0', '0', '0']
]

class Map:
    def __init__(self, screen, bg_img):
        self.bg = GameSprite(screen, bg_img, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.player, self.enemies, self.walls = MapGenerator.generate(screen)
    
    def render_background(self):
        self.bg.render()
    
    def update(self):
        pass
    

class MapGenerator:
    @staticmethod
    def generate(screen):
        player = ''
        enemies = []
        walls = []
        for y in range(len(game_map)):
            for x in range(len(game_map[0])):
                pos_x = (SCREEN_WIDTH * x) // len(game_map[0])
                pos_y = (SCREEN_HEIGHT * y) // len(game_map[1])
                if game_map[y][x] == "w":
                    walls.append(CollidingObject(screen, 'stone.png', pos_x + 10, pos_y + 10, 80, 80))
                elif game_map[y][x] == 'e':
                    enemies.append(Enemy(screen, 'enemy.png', pos_x, pos_y, 100, 100))
                elif game_map[y][x] == 'e1':
                    enemies.append(Enemy(screen, 'enemy1.png', pos_x, pos_y, 100, 100))
                elif game_map[y][x] == 'p':
                    player = Hero(screen, 'hero.png', pos_x, pos_y, 80, 80)
        return player, enemies, walls