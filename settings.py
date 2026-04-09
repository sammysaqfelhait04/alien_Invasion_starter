import pathlib import path
class Settings:
    
    def __init__(self):
        self.name = "Alien Invasion"
        self.screen_width = 1200
        self.screen_height = 800
        self.FpS = 60
        self.bg_file = path.cwd() / 'assets' / 'images' / 'starbase.png'
        
        self.ship_file = path.cwd() / 'assets' / 'images' / 'ship2(no bg).png'
        self.ship_width = 40
        self.ship_height = 60
        self.ship_speed = 5

        self.bullet_file = path.cwd() / 'assets' / 'images' / 'laserBlast.png'
        self.laser_sound_file = path.cwd() / 'assets' / 'sounds' / 'laser.mp3'
        self.bullet_height = 80
        self.bullet_width = 25
        self.bullet_speed = 7
        self.bullet_amount = 5
        
