from sprites import *
from constants import *
from hero import *
from enemy import *
from copy import deepcopy

class Map:
    game_map = [
        ['w', 'p', 'w', 'e', '0', '0', 'w', '0'],
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
    
    def __init__(self, screen, bg_img):
        self.bg = GameSprite(screen, bg_img, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.player, self.enemies, self.walls = MapGenerator.generate(screen)
    
    def render_background(self):
        self.bg.render()
    
    def update(self):
        new_map = deepcopy(Map.clean_map)
        player_x, player_y = self.get_object_position(self.player, self.player.go_back)
        new_map[player_y][player_x] = 'p'
        
        #for enemy in self.enemies:
            #enemy_x, enemy_y = self.get_object_position(enemy, enemy.go_back)
            #new_map[enemy_y][enemy_x] = 'e' + .. enemy type
        
        Map.game_map = new_map
    
    def get_object_position(self, object, func = ''):
        rect_x = object.rect.x
        rect_y = object.rect.y
        object_x = round(rect_x * len(Map.game_map[0]) / SCREEN_WIDTH)
        object_y = round(rect_y * len(Map.game_map) / SCREEN_HEIGHT)
        if Map.clean_map[object_y][object_x] == 'w':
            func()
            return self.get_object_position(object, func)
        return object_x, object_y
        
    

class MapGenerator:
    @staticmethod
    def generate(screen):
        player = ''
        enemies = []
        walls = []
        for y in range(len(Map.game_map)):
            for x in range(len(Map.game_map[0])):
                pos_x = (SCREEN_WIDTH * x) // len(Map.game_map[0])
                pos_y = (SCREEN_HEIGHT * y) // len(Map.game_map)
                if Map.game_map[y][x] == "w":
                    walls.append(CollidingObject(screen, 'stone.png', pos_x, pos_y, 100, 100))
                elif Map.game_map[y][x] == 'e':
                    enemies.append(Enemy(screen, 'enemy.png', pos_x, pos_y, 100, 100))
                elif Map.game_map[y][x] == 'e1':
                    enemies.append(Enemy(screen, 'enemy1.png', pos_x, pos_y, 100, 100))
                elif Map.game_map[y][x] == 'p':
                    player = Hero(screen, 'hero.png', pos_x, pos_y, 80, 80)
        return player, enemies, walls