import sys
import pygame
from settings import Settings

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height  ))
        pygame.display.set_caption("self .name")

        self.bg_image = pygame.image.load(self.settings.bg_file)
        self.bg_image = pygame.transform.scale(self.bg_image, (self.settings.screen_width, self.settings.screen_height))

        self.running = True
        self.clock = pygame.time.Clock()

        self.ship = Ship(self)  

    def run_game(self):
        while self.running:
                    self._check_events()
                    self.update_screen()
                    self.clock.tick(self.settings.FpS)
    def _check_events(self):
            
                    self.ship.draw()
self.screen.blit(self.bg_image, (0, 0))

            pygame.display.flip()
            self.clock.tick(self.settings.FpS)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
    
