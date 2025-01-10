"""This is the settings file"""
import random


class Settings:
    """A class to store all settings for Alien Invasion"""
    pathway = [[
            (50, 400), (300, 400), (300, 200), (600, 200),
            (600, 600), (900, 600), (900, 300), (1150, 300)
            ],
            [ (50, 400), (100, 400), (200, 200), (600, 310),
            (400, 600), (900, 600), (900, 300), (1150, 300)
             ],
            [ (50, 300), (200, 400), (250, 600), (600, 310),
            (700, 600), (900, 500), (900, 350), (1050, 300)
             ]]

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.rows = 10
        self.cols = 15
        self.grid_size = (64, 64)

        self.tower_cost = 100
        self.tower_upgrade_cost = 150
        self.tower_sell_percentage = 0.75

        

        self.tower_sprites = {
            'basic': 'assets/towers/basic_tower.png',
            'sniper': 'assets/towers/sniper_tower.png',
            
        }
       
        self.bullet_sprite = 'assets/bullets/basic_bullet.png'
        self.background_image = 'assets/backgrounds/game_background.png'

        self.shoot_sound = 'assets/sounds/shoot.wav'
        self.upgrade_sound = 'assets/sounds/upgrade.wav'
        self.sell_sound = 'assets/sounds/sell.wav'
        self.enemy_hit_sound = 'assets/sounds/enemy_hit.wav'
        self.background_music = 'assets/sounds/background_music.mp3'

        
        self.lives = 20

        self.tower_positions = [(x * self.grid_size[0] + self.grid_size[0] // 2, y * self.grid_size[1] + self.grid_size[1] // 2)
                                for x in range(1, self.cols) for y in range(3, self.rows)]

    
