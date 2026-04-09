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